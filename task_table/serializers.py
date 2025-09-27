from rest_framework import serializers

from task_table.models import TaskTable


class TaskTableSerializer(serializers.ModelSerializer):
    """Сериализатор для приложения `task_table`"""
    class Meta:
        model = TaskTable
        fields = '__all__'  # Все поля модели

class TaskWithEmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода списка объектов в формате: {Важная задача, Срок, [ФИО сотрудника]}"""
    employee_full_name = serializers.CharField(source='performer.full_name', read_only=True)

    class Meta:
        # "Важная задача" - это поле name
        # "Срок" - это поле term
        # "ФИО сотрудника" - берем из связанной модели через performer
        model = TaskTable
        fields = ['name', 'term', 'employee_full_name']  # Соответствует формату из задания