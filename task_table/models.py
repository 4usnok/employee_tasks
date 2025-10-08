from django.db import models

from employee_table.models import EmployeeTable


class TaskTable(models.Model):
    """Модель для таблицы задач"""

    name: models.CharField = models.CharField(
        max_length=70, help_text="название таблицы"
    )
    parent_task: models.ForeignKey = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="child_tasks",
        help_text="родительская задача",
    )
    performer: models.ForeignKey = models.ForeignKey(
        EmployeeTable,
        on_delete=models.CASCADE,
        help_text="исполнитель",
        related_name="task_table",
    )
    term: models.IntegerField = models.IntegerField(
        null=True, blank=True, help_text="срок"
    )
    status: models.BooleanField = models.BooleanField(default=True, help_text="статус")
    work: models.BooleanField = models.BooleanField(
        default=True, help_text="взять в работу задачу"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
