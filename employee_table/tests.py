from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employee_table.models import EmployeeTable
from task_table.models import TaskTable
from user.models import User


class TaskApiTestCase(APITestCase):
    def setUp(self):
        """Подготовка данных перед каждым тестом"""
        self.user = User.objects.create_user(  # создание пользователя
            username="testuser", password="testpass123", email="test@example.com"
        )
        self.employee_table = (
            EmployeeTable.objects.create(  # создание таблицы сотрудника
                full_name="Test",
                job_title="Test",
            )
        )
        self.task_table = TaskTable.objects.create(  # создание таблицы задач
            name="Test", performer=self.employee_table, status=True, work=True
        )

    def test_list_view_employee_table(self):
        """Тестирование просмотра всех таблиц сотрудников"""
        urls_list_view = reverse("employee_table:list-views")
        response = self.client.get(urls_list_view)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee_table(self):
        """Тестирование создания таблицы сотрудников"""
        data_from_create = {
            "full_name": "Test",
            "job_title": "Test",
        }
        urls_create = reverse("employee_table:tables-create")

        response = self.client.post(urls_create, data=data_from_create, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_employee_table(self):
        """Тестирование редактирования таблицы сотрудников"""
        data_from_update = {
            "full_name": "Test",
            "job_title": "Test",
        }
        urls_create = reverse(
            "employee_table:tables-update", kwargs={"pk": self.employee_table.pk}
        )

        response = self.client.patch(urls_create, data=data_from_update, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_employee_table(self):
        """Тестирование просмотра конкретной таблицы сотрудников"""

        urls_from_detail = reverse(
            "employee_table:tables-detail", kwargs={"pk": self.employee_table.pk}
        )

        response = self.client.get(urls_from_detail, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_employee_table(self):
        """Тестирование удаления таблицы сотрудников"""
        urls_from_delete = reverse(
            "employee_table:tables-destroy", kwargs={"pk": self.employee_table.pk}
        )

        response = self.client.delete(urls_from_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
