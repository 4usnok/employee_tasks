from rest_framework import serializers

from employee_table.models import EmployeeTable
from task_table.models import TaskTable


class EmployeeTableSerializer(serializers.ModelSerializer):
    """Сериализатор для приложения `employee_table`"""
    class Meta:
        model = EmployeeTable
        fields = '__all__'  # Все поля модели

