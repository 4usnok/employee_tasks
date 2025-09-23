from django.db import models

from config import settings


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
    link_to_parent_task = models.URLField(
        max_length=200,
        help_text="ссылка на родительскую задачу"
    )
    performer = models.CharField(
        max_length=70,
        help_text="испольнитель"
    )
    term = models.IntegerField(
        max_length=5,
        help_text="срок"
    )
    status = models.BooleanField(
        default=True,
        help_text="статус"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['owner', 'name']
