from django.db import models

from config import settings
from employee_table.models import EmployeeTable


class TaskTable(models.Model):
    """Модель для таблицы задач"""
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=70,
        help_text="название таблицы"
    )
    link_to_parent_task = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="child_tasks",
        help_text="ссылка на родительскую задачу"
    )
    performer = models.ForeignKey(
        EmployeeTable,
        on_delete=models.CASCADE,
        help_text="исполнитель"
    )
    term = models.IntegerField(
        null=True,
        blank=True,
        help_text="срок"
    )
    status = models.BooleanField(
        default=True,
        help_text="статус"
    )
    work = models.BooleanField(
        default=True,
        help_text="взять в работу задачу"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['owner', 'name']
