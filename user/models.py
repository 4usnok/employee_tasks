from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Модель для пользователей"""
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'  # авторизация по email
    REQUIRED_FIELDS =["username"]

    def __str__(self):
        return self.email
