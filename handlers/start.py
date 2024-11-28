from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup

start_router = Router()
id_list = []

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    print(f"Message, chat type: {message.chat.type}")
    name = message.from_user.first_name
    msg = f"Привет {name}, {message.from_user.id}"
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text="my profile inst",
                url="https://instagram.com/lllsuccesslll",
            )
        ],
        [
            types.InlineKeyboardButton(
                text="my tg channel",
                url="t.me/+1pVI9RuurtQzY2Qy",
            )
        ],
        [
            types.InlineKeyboardButton(
                text="leave feedback",
                callback_data="review"
            ),
            types.InlineKeyboardButton(
                text="show dishes",
                callback_data="show_dishes"
            )
        ]

    ]
)
    await message.answer(msg, reply_markup=kb)
    us_id = message.from_user.id
    if us_id not in id_list:
        id_list.append(us_id)
    await message.answer(f"my bot was used by {len(id_list)} users")
