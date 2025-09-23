from rest_framework import generics

from employee_table.serializers import EmployeeTableSerializer
from employee_table.models import EmployeeTable

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
