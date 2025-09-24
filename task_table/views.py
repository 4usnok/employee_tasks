from django.db.models import Count
from rest_framework import generics

from task_table.models import TaskTable
from task_table.serializers import TaskTableSerializer


class TaskList(generics.ListAPIView):
    """Просмотр списка таблиц задач"""
    queryset = TaskTable.objects.all()
    serializer_class = TaskTableSerializer


class TaskTableCreate(generics.ListCreateAPIView):
    """Создание таблицы задач"""
    queryset = TaskTable.objects.all()
    serializer_class = TaskTableSerializer


class TaskTableDestroy(generics.DestroyAPIView):
    """Удаление таблицы задач"""
    queryset = TaskTable.objects.all()
    serializer_class = TaskTableSerializer


class TaskTableUpdate(generics.UpdateAPIView):
    """Редактирование таблицы задач"""
    queryset = TaskTable.objects.all()
    serializer_class = TaskTableSerializer


class TaskTableRetrieve(generics.RetrieveAPIView):
    """Просмотр одной таблицы задач"""
    queryset = TaskTable.objects.all()
    serializer_class = TaskTableSerializer

class TaskListNotWork(generics.ListAPIView):
    """
    Запрашивает из БД задачи, которые не взяты в работу,
    но от которых зависят другие задачи, взятые в работу
    """
    serializer_class = TaskTableSerializer

    def get_queryset(self):
        tasks_in_work = TaskTable.objects.filter(
            status=False,
            child_tasks__status=True
        )
        return tasks_in_work.distinct()