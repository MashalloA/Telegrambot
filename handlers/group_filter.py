from aiogram import Router, F, types
from aiogram.filters import Command
from datetime import timedelta

group_router = Router()

BAD_WORDS = ("тупой", "дурак")

@group_router.message(Command("ban", prefix="!"))
async def ban(message: types.Message):
    if not message.reply_to_message:
        await message.answer("надо ответить на чье то сообщение")
    else:
        banned = message.reply_to_message.from_user.id
        await message.bot.ban_chat_member(
            chat_id=message.from_user.id,
            user_id=banned,
        )

@group_router.message(F.text.startswith("бан"))
async def ban_on_day(message: types.Message):
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("использование бана: бан *сколько дней*")
        return
    try:
        if message.reply_to_message:
            days = int(parts[1])
            name = message.reply_to_message.from_user.first_name
            user = message.reply_to_message.from_user
            await message.chat.ban(
                user_id=user.id,
                until_date=message.date + timedelta(days=days)
            )
            msg = f"пользоывтель: {name}- был забанен на: {days} дня"
            await message.answer(msg)
    except ValueError:
        await message.answer("Неверный формат: использование бана: бан *сколько дней*")



@group_router.message(F.text)
async def group_echo(message: types.Message):
    for word in BAD_WORDS:
        if word in message.text.lower():
            await message.answer("это плохое слово")
            await message.delete()
            break
