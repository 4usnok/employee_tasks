import unittest
from unittest.mock import AsyncMock, patch

from aiogram.types import Message

from handlers.employee_handlers import (view_employees_list,
                                        view_spec_endpoint_employee)


class TestTaskHandlers(unittest.TestCase):
    """Тесты для обработчиков задач с unittest"""

    def setUp(self):
        """Выполняется перед каждым тестом"""
        # Создаем mock сообщения
        self.message = AsyncMock(spec=Message)
        self.message.text = "Список сотрудников"
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

    def test_view_employees_list(self):
        """Тест успешного получения задач с данными"""

        async def run_test():
            self.mock_response.json.return_value = [
                {
                    "full_name": "test",
                    "job_title": "test",
                },
                {
                    "full_name": "test2",
                    "job_title": "test2",
                },
            ]

            await view_employees_list(self.message)

            self.message.answer.assert_called_once()
            call_args = self.message.answer.call_args[0][0]
            self.assertIn("👥 Сотрудники:", call_args)
            self.assertIn("test", call_args)
            self.assertIn("test2", call_args)

        # Запускаем асинхронный тест
        import asyncio

        asyncio.run(run_test())


class TestSpecEndpointEmployee(unittest.TestCase):
    """Тесты для спец endpoint'а блокирующих задач"""

    def setUp(self):
        self.message = AsyncMock(spec=Message)
        self.message.text = "Список приоритетных сотрудников"
        self.message.answer = AsyncMock()

        self.mock_get_patcher = patch("aiohttp.ClientSession.get")
        self.mock_get = self.mock_get_patcher.start()

        self.mock_response = AsyncMock()
        self.mock_response.status = 200
        self.mock_get.return_value.__aenter__.return_value = self.mock_response

    def tearDown(self):
        self.mock_get_patcher.stop()

    def test_view_spec_endpoint_employee(self):
        """Тест успешного получения блокирующих задач"""

        async def run_test():
            self.mock_response.json.return_value = [
                {
                    "full_name": "test",
                    "job_title": "test",
                }
            ]

            await view_spec_endpoint_employee(self.message)

            self.message.answer.assert_called_once()
            call_args = self.message.answer.call_args[0][0]
            self.assertIn("👥 Сотрудники:", call_args)
            self.assertIn("test", call_args)

        import asyncio

        asyncio.run(run_test())


if __name__ == "__main__":
    unittest.main()
