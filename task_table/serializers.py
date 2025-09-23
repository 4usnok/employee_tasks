from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from task_table.models import TaskTable


class TaskTableSerializer(serializers.Serializer):
    """Сериализатор для приложения `task_table`"""
    class Meta:
        model = TaskTable
        fields = '__all__'  # Все поля модели
        permission_classes = [IsAuthenticated]  # права доступа
