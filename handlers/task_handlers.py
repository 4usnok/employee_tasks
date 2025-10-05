import logging
import os

import aiohttp

from aiogram import types, Bot, Router
from dotenv import load_dotenv

load_dotenv()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=os.getenv('BOT_TOKEN'))
# Диспетчер
router = Router()

@router.message(lambda message: message.text == "Список задач сотрудников")
async def view_tasks_list(message: types.Message):
    """Асинхронная функция для получения задач из БД"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://localhost:8000/task_table/tables/") as response:
                if response.status == 200:
                    tasks = await response.json()
                    if tasks:
                        text = "🎯 Задачи сотрудников:\n\n"
                        for task in tasks:
                            if task.get('status') == True:
                                if task.get('term', 'No name') == None:
                                    text += (f"📔 Название задачи: {task.get('name', '❌')}\n"
                                             f"👨🏻‍💼 Исполнитель: {task.get('employee_full_name', '❌')}\n"
                                             f"🗓 Дней на выполнение: ❌\n"
                                             f"☑️ Статус: ✅\n\n"
                                            )
                                elif task.get('term', 'No name') != None:
                                    text += (f"📔 Название задачи: {task.get('name', '❌')}\n"
                                             f"👨🏻‍💼 Исполнитель: {task.get('employee_full_name', '❌')}\n"
                                             f"🗓 Дней на выполнение: {task.get('term', '❌')}\n"
                                             f"☑️ Статус: ✅\n\n"
                                            )
                            else:
                                if task.get('term', 'No name') == None:
                                    text += (f"📔 Название задачи: {task.get('name', '❌')}\n"
                                             f"👨🏻‍💼 Исполнитель: {task.get('employee_full_name', '❌')}\n"
                                             f"🗓 Дней на выполнение: ❌\n"
                                             f"☑️ Статус: ❌\n\n"
                                             )
                                elif task.get('term', 'No name') != None:
                                    text += (f"📔 Название задачи: {task.get('name', '❌')}\n"
                                             f"👨🏻‍💼 Исполнитель: {task.get('employee_full_name', '❌')}\n"
                                             f"🗓 Дней на выполнение: {task.get('term', '❌')}\n"
                                             f"☑️ Статус: ❌\n\n"
                                             )
                        await message.answer(text)
                    else:
                        await message.answer("📭 Нет задач")
                else:
                    await message.answer("❌ Ошибка сервера")

    except Exception as e:
        await message.answer("❌ Не удалось получить задачи")
        print(f"Error: {e}")

@router.message(lambda message: message.text == "Список блокирующих задач")
async def view_spec_endpoint_tasks(message: types.Message):
    """Асинхронная функция для получения блокирующих задач"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://localhost:8000/task_table/tables/active_task/") as response:
                if response.status == 200:
                    active_tasks = await response.json()
                    if active_tasks:
                        text = "🎯 Задачи сотрудников:\n\n"
                        for task in active_tasks:
                            if task.get('status') == True:
                                if task.get('term', 'No name') == None:
                                    text += (f"📔 Название задачи: {task.get('name', 'No name')}\n"
                                             f"👨🏻‍💼 Исполнитель: {task.get('employee_full_name', 'No name')}\n"
                                             f"🗓 Дней на выполнение: ❌\n"
                                             f" Статус: ✅\n\n"
                                             )
                                elif task.get('term', 'No name') != None:
                                    text += (f"📔 Название задачи: {task.get('name', 'No name')}\n"
                                             f"👨🏻‍💼 Исполнитель: {task.get('employee_full_name', 'No name')}\n"
                                             f"🗓 Дней на выполнение: {task.get('term', 'No name')}\n"
                                             f" Статус: ✅\n\n"
                                             )
                            else:
                                if task.get('term', 'No name') == None:
                                    text += (f"📔 Название задачи: {task.get('name', 'No name')}\n"
                                             f"👨🏻‍💼 Исполнитель: {task.get('employee_full_name', 'No name')}\n"
                                             f"🗓 Дней на выполнение: ❌\n"
                                             f" Статус: ❌\n\n"
                                             )
                                elif task.get('term', 'No name') != None:
                                    text += (f"📔 Название задачи: {task.get('name', 'No name')}\n"
                                             f"👨🏻‍💼 Исполнитель: {task.get('employee_full_name', 'No name')}\n"
                                             f"🗓 Дней на выполнение: {task.get('term', 'No name')}\n"
                                             f" Статус: ❌\n\n"
                                             )
                        await message.answer(text)
                    else:
                        await message.answer("📭 Нет задач")
                else:
                    await message.answer("❌ Ошибка сервера")

    except Exception as e:
        await message.answer("❌ Не удалось получить сотрудников")
        print(f"Error: {e}")
