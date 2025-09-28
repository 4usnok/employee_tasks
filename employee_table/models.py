from django.db import models


class EmployeeTable(models.Model):
    """Модель для таблицы сотрудников"""

    full_name = models.CharField(max_length=70, help_text="ФИО")
    job_title = models.CharField(max_length=70, help_text="Должность")

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ["full_name"]
