from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, Message


def month_kb():
    kb_visit_month = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Январь"),
                KeyboardButton(text="Февраль")
            ],
            [
                KeyboardButton(text="Март"),
                KeyboardButton(text="Апрель")
            ],
            [
                KeyboardButton(text="Май"),
                KeyboardButton(text="Июнь")
            ],
            [
                KeyboardButton(text="Июль"),
                KeyboardButton(text="Август")
            ],
            [
                KeyboardButton(text="Сентябрь"),
                KeyboardButton(text="Октябрь")
            ],
            [
                KeyboardButton(text="Ноябрь"),
                KeyboardButton(text="Декабрь")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="месяц:"
    )
    return kb_visit_month


def rating_kb():
    kb_visit_rating = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="плохо")
            ],
            [
                KeyboardButton(text="хорошо"),
                KeyboardButton(text="отлично")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return kb_visit_rating
