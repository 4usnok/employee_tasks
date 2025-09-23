from django.db import models

from config import settings


class EmployeeTable(models.Model):
    """Модель для таблицы сотрудников"""
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    full_name = models.CharField(
        max_length=70
    )
    job_title = models.CharField(
        max_length=70
    )

    def __str__(self):
        return self.full_name
