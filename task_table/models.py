from django.db import models

from config import settings


class TaskTable(models.Model):
    """Модель для таблицы задач"""
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=70
    )
    link_to_parent_task = models.URLField(
        max_length=200
    )
    performer = models.CharField(
        max_length=70
    )
    term = models.IntegerField(
        max_length=5
    )
    status = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name
