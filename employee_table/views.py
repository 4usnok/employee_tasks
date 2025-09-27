from django.db.models import Count
from rest_framework import generics

from employee_table.serializers import EmployeeTableSerializer
from employee_table.models import EmployeeTable
from task_table.models import TaskTable
from task_table.serializers import TaskWithEmployeeSerializer


class EmployeeTableList(generics.ListAPIView):
    """Просмотр списка таблиц сотрудников"""
    queryset = EmployeeTable.objects.all()
    serializer_class = EmployeeTableSerializer


class EmployeeTableCreate(generics.ListCreateAPIView):
    """Создание таблицы сотрудников"""
    queryset = EmployeeTable.objects.all()
    serializer_class = EmployeeTableSerializer


class EmployeeTableDestroy(generics.DestroyAPIView):
    """Удаление таблицы сотрудников"""
    queryset = EmployeeTable.objects.all()
    serializer_class = EmployeeTableSerializer


class EmployeeTableUpdate(generics.UpdateAPIView):
    """Редактирование таблицы сотрудников"""
    queryset = EmployeeTable.objects.all()
    serializer_class = EmployeeTableSerializer


class EmployeeTableRetrieve(generics.RetrieveAPIView):
    """Просмотр одной таблицы сотрудников"""
    queryset = EmployeeTable.objects.all()
    serializer_class = EmployeeTableSerializer


class EmployeeListWithActiveTasks(generics.ListAPIView):
    """Просмотр списка таблиц сотрудников с активными задачами"""
    serializer_class = EmployeeTableSerializer

    def get_queryset(self):
        return (TaskTable.objects.filter(status=True) # фильтрация по активному статусу задач
         .values('owner') # группировка по владельцу
         .annotate(total_owner=Count('id')) # количество задач у каждого владельца
         .order_by('-total_owner') # сортировка
         )

class FindEmployee(generics.ListAPIView):
    """
    Реализует поиск по сотрудникам, которые могут взять такие задачи
    (наименее загруженный сотрудник или сотрудник,
    выполняющий родительскую задачу, если ему назначено максимум на 2 задачи больше,
    чем у наименее загруженного сотрудника).
    """
    serializer_class = TaskWithEmployeeSerializer

    def get_queryset(self):
        # Шаг 1. Определяем наименее загруженного сотрудника
        employees_with_load = EmployeeTable.objects.annotate(
            task_count=Count('task_table')
        )
        least_loaded = employees_with_load.order_by('task_count').first()

        # Шаг 2. Определяем сотрудников выполняющего родительскую задачу
        parent_employees = EmployeeTable.objects.filter(
            task_table__parent_task__isnull=False
        ).annotate(
        task_count=Count('task_table')
        ).distinct()

        # Шаг 3. если сотруднику назначено максимум на 2 задачи больше, чем у наименее загруженного сотрудника
        if least_loaded:
            for parent_emp in parent_employees:
                if parent_emp.task_count <= least_loaded.task_count + 2:
                    return TaskTable.objects.filter(performer=parent_emp)
            # Если цикл завершился и не нашел подходящего - возвращаем наименее загруженного
            return TaskTable.objects.filter(performer=least_loaded)
        else:
            return TaskTable.objects.none()  # если вообще нет сотрудников
