from aiogram import Router, types
from aiogram.filters import Command

info_router = Router()

@info_router.message(Command('myinfo'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    us_id = message.from_user.id
    us_name = message.from_user.username
    await message.answer(f"your id is: {us_id}, your name is: {name}, your username is: {us_name}")

