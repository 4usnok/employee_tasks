from django.db.models import Count
from rest_framework import generics

from employee_table.serializers import EmployeeTableSerializer
from employee_table.models import EmployeeTable
from task_table.models import TaskTable


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
         .annotate(total=Count('id')) # количество задач у каждого владельца
         .order_by('-total') # сортировка
         )
