import logging
import os

import aiohttp
from aiogram import Bot, Router, types
from dotenv import load_dotenv

load_dotenv()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Диспетчер
router = Router()


@router.message(lambda message: message.text == "Список сотрудников")
async def view_employees_list(message: types.Message):
    """Асинхронная функция для получения сотрудников из БД"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "http://localhost:8000/employee_table/tables/"
            ) as response:
                if response.status == 200:
                    employees = await response.json()
                    if employees:
                        text = "👥 Сотрудники:\n\n"
                        for emp in employees:
                            text += (
                                f"👨🏻‍💼 ФИО: {emp.get('full_name', 'No name')}\n"
                                f"👔 Должность: {emp.get('job_title', 'No name')}\n\n"
                            )
                        await message.answer(text)
                    else:
                        await message.answer("📭 Нет сотрудников")
                else:
                    await message.answer("❌ Ошибка сервера")

    except Exception as e:
        await message.answer("❌ Не удалось получить сотрудников")
        print(f"Error: {e}")


@router.message(lambda message: message.text == "Список приоритетных сотрудников")
async def view_spec_endpoint_employee(message: types.Message):
    """Асинхронная функция для спец энд-поинта: получения приоритетных исполнителей"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "http://localhost:8000/employee_table/tables/find-employee/"
            ) as response:
                if response.status == 200:
                    employees = await response.json()
                    if employees:
                        text = "👥 Сотрудники:\n\n"
                        for emp in employees:
                            text += (
                                f"👨🏻‍💼 ФИО: {emp.get('full_name', 'No name')}\n"
                                f"👔 Должность: {emp.get('job_title', 'No name')}\n\n"
                            )
                        await message.answer(text)
                    else:
                        await message.answer("📭 Нет сотрудников")
                else:
                    await message.answer("❌ Ошибка сервера")

    except Exception as e:
        await message.answer("❌ Не удалось получить сотрудников")
        print(f"Error: {e}")
