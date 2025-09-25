from django.db import models

from employee_table.models import EmployeeTable


class ParentTaskTable(models.Model):
    """Модель для таблицы задач"""
    name = models.CharField(
        max_length=70,
        help_text="название таблицы"
    )

    performer = models.ForeignKey(
        EmployeeTable,
        on_delete=models.CASCADE,
        help_text="исполнитель"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class TaskTable(models.Model):
    """Модель для таблицы задач"""
    name = models.CharField(
        max_length=70,
        help_text="название таблицы"
    )
    parent_task = models.ForeignKey(
        ParentTaskTable,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="child_tasks",
        help_text="родительская задача"
    )
    performer = models.ForeignKey(
        EmployeeTable,
        on_delete=models.CASCADE,
        help_text="исполнитель",
        related_name="task_table"
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
        ordering = ['name']
