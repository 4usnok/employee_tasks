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

    def test_list_view_task_table(self):
        """Тестирование просмотра всех таблиц задач"""
        urls_list_view = reverse("task_table:list-views")
        response = self.client.get(urls_list_view)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task_table(self):
        """Тестирование создания таблицы задач"""
        data_from_create = {
            "name": "test",
            "performer": self.employee_table.id,
            "status": True,
            "work": True,
        }
        urls_create = reverse("task_table:tables-create")

        response = self.client.post(urls_create, data=data_from_create, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task_table(self):
        """Тестирование редактирования таблицы задач"""
        data_from_update = {
            "name": "test",
            "performer": self.employee_table.id,
            "status": True,
            "work": True,
        }
        urls_create = reverse(
            "task_table:tables-update", kwargs={"pk": self.task_table.pk}
        )

        response = self.client.patch(urls_create, data=data_from_update, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_task_table(self):
        """Тестирование просмотра конкретной таблицы задач"""

        urls_from_detail = reverse(
            "task_table:tables-detail", kwargs={"pk": self.task_table.pk}
        )

        response = self.client.get(urls_from_detail, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_task_table(self):
        """Тестирование удаления таблицы задач"""
        urls_from_delete = reverse(
            "task_table:tables-destroy", kwargs={"pk": self.task_table.pk}
        )

        response = self.client.delete(urls_from_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_task_list_not_work(self):
        """Тестирование специального энд-поинта"""
        # Создаем родительскую задачу НЕ в работе
        parent_task = TaskTable.objects.create(  # noqa: F841
            name="Parent Task Not in Work",
            performer=self.employee_table,
            status=False,  # НЕ в работе
            work=True,
        )

        # Создаем дочернюю задачу В работе
        child_task = TaskTable.objects.create(  # noqa: F841
            name="Child Task in Work",
            performer=self.employee_table,
            parent_task=parent_task,  # связываем с родительской
            status=True,  # В работе
            work=True,
        )

        # Создаем другую задачу НЕ в работе без дочерних (не должна попасть в результат)
        standalone_task = TaskTable.objects.create(  # noqa: F841
            name="Standalone Task Not in Work",
            performer=self.employee_table,
            status=False,  # НЕ в работе
            work=True,
        )

        url = reverse("task_table:active-task")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Parent Task Not in Work")
