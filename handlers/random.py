from aiogram import Router, types
from aiogram.filters import Command
import random

random_router = Router()

names = ["Алексей", "Мария", "Иван", "Елена", "Сергей"]

@random_router.message(Command("random"))  # Декоратор должен быть перед функцией
async def random_command(message: types.Message):
    random_name = random.choice(names)
    await message.reply(f"Случайное имя: {random_name}")