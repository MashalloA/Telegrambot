from aiogram.filters import Command
from aiogram import Router, types
from random import choice

rnd_router = Router()

@rnd_router.message(Command('random'))
async def start_handler(message: types.Message):
    names = ["alex", "edward", "max", "daniel"]
    name = choice(names)
    await message.answer(f"random name in list: {name}")

