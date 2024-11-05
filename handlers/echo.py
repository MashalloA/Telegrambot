from aiogram import Router, types

echo_router = Router()

@echo_router.message()
async def echo(message: types.Message):
    msg = "i don't understand you("
    await message.answer(msg)