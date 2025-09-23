from rest_framework import serializers

from employee_table.models import EmployeeTable


class EmployeeTableSerializer(serializers.Serializer):
    """Сериализатор для приложения `employee_table`"""
    class Meta:
        model = EmployeeTable
        fields = '__all__'  # Все поля модели
