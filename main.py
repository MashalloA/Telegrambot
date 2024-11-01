import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
from random import choice

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
id_list = []

@dp.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Привет {name}")
    us_id = message.from_user.id
    if us_id not in id_list:
        id_list.append(us_id)
    await message.answer(f"my bot was used by {len(id_list)} users")

@dp.message(Command('myinfo'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    us_id = message.from_user.id
    us_name = message.from_user.username
    await message.answer(f"your id is: {us_id}, your name is: {name}, your username is: {us_name}")

@dp.message(Command('random'))
async def start_handler(message: types.Message):
    names = ["alex", "edward", "max", "daniel"]
    name = choice(names)
    await message.answer(f"random name in list: {name}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())