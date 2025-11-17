import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv

from handlers.employee_handlers import router as employee_router
from handlers.task_handlers import router as task_router

load_dotenv()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

dp.include_router(employee_router)
dp.include_router(task_router)


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("" "Добро пожаловать в чат-бот трекера задач сотрудника.")
    kb = [
        [
            types.KeyboardButton(text="Список задач сотрудников"),
            types.KeyboardButton(text="Список блокирующих задач"),
        ],
        [
            types.KeyboardButton(text="Список сотрудников"),
            types.KeyboardButton(text="Список приоритетных сотрудников"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите для себя нужную функцию",
    )
    await message.answer("Какую функцию хотите выбрать ?", reply_markup=keyboard)


# Запускаем всё
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
