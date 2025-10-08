import unittest
from unittest.mock import AsyncMock, patch

from aiogram.types import Message

from handlers.task_handlers import view_spec_endpoint_tasks, view_tasks_list


class TestTaskHandlers(unittest.TestCase):
    """Тесты для обработчиков задач с unittest"""

    def setUp(self):
        """Выполняется перед каждым тестом"""
        # Создаем mock сообщения
        self.message = AsyncMock(spec=Message)
        self.message.text = "Список задач сотрудников"
        self.message.answer = AsyncMock()

        # Создаем патчер для aiohttp
        self.mock_get_patcher = patch("aiohttp.ClientSession.get")
        self.mock_get = self.mock_get_patcher.start()

        # Настраиваем стандартный успешный ответ
        self.mock_response = AsyncMock()
        self.mock_response.status = 200
        self.mock_get.return_value.__aenter__.return_value = self.mock_response

    def tearDown(self):
        """Выполняется после каждого теста"""
        self.mock_get_patcher.stop()

    def test_view_tasks_list_success_with_data(self):
        """Тест успешного получения задач с данными"""

        async def run_test():
            self.mock_response.json.return_value = [
                {
                    "name": "Тестовая задача 1",
                    "employee_full_name": "Иван Иванов",
                    "term": 5,
                    "status": True,
                },
                {
                    "name": "Тестовая задача 2",
                    "employee_full_name": "Петр Петров",
                    "term": None,
                    "status": False,
                },
            ]

            await view_tasks_list(self.message)

            self.message.answer.assert_called_once()
            call_args = self.message.answer.call_args[0][0]
            self.assertIn("🎯 Задачи сотрудников", call_args)
            self.assertIn("Тестовая задача 1", call_args)
            self.assertIn("Тестовая задача 2", call_args)

        # Запускаем асинхронный тест
        import asyncio

        asyncio.run(run_test())


class TestSpecEndpointTasks(unittest.TestCase):
    """Тесты для спец endpoint'а блокирующих задач"""

    def setUp(self):
        self.message = AsyncMock(spec=Message)
        self.message.text = "Список блокирующих задач"
        self.message.answer = AsyncMock()

        self.mock_get_patcher = patch("aiohttp.ClientSession.get")
        self.mock_get = self.mock_get_patcher.start()

        self.mock_response = AsyncMock()
        self.mock_response.status = 200
        self.mock_get.return_value.__aenter__.return_value = self.mock_response

    def tearDown(self):
        self.mock_get_patcher.stop()

    def test_view_spec_endpoint_tasks_success(self):
        """Тест успешного получения блокирующих задач"""

        async def run_test():
            self.mock_response.json.return_value = [
                {
                    "name": "Блокирующая задача",
                    "employee_full_name": "Василий Блокирующий",
                    "term": 7,
                    "status": False,
                }
            ]

            await view_spec_endpoint_tasks(self.message)

            self.message.answer.assert_called_once()
            call_args = self.message.answer.call_args[0][0]
            self.assertIn("🎯 Задачи сотрудников", call_args)
            self.assertIn("Блокирующая задача", call_args)

        import asyncio

        asyncio.run(run_test())


if __name__ == "__main__":
    unittest.main()
