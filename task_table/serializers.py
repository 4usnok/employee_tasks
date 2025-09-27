from rest_framework import serializers

from task_table.models import TaskTable


class TaskTableSerializer(serializers.ModelSerializer):
    """Сериализатор для приложения `task_table`"""
    class Meta:
        model = TaskTable
        fields = '__all__'  # Все поля модели
