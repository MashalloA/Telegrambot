from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import items.kb as kb
import sqlite3

from bot_config import database

review_router = Router()


class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

@review_router.message(Command("stop"))
@review_router.message(F.text == "стоп")
async def stop_dialog(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("опрос остановлен")


@review_router.callback_query(F.data == "review")
async def start_review(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Как вас зовут?")
    await state.set_state(RestaurantReview.name)
    await callback_query.answer()


@review_router.message(RestaurantReview.name)
async def ask_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Ваш номер телефона:")
    await state.set_state(RestaurantReview.phone_number)


@review_router.message(RestaurantReview.phone_number)
async def ask_phone(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("введите дату вашего посещения (в формате ДД,ММ,ГГГГ)")
    await state.set_state(RestaurantReview.visit_date)


@review_router.message(RestaurantReview.visit_date)
async def ask_visit_date(message: Message, state: FSMContext):
    await state.update_data(food_rating=message.text)
    await message.answer("оцените качество еды", reply_markup=kb.rating_kb())
    await state.set_state(RestaurantReview.food_rating)


@review_router.message(RestaurantReview.food_rating, F.text.in_(["1", "2", "3", "4", "5"]))
async def ask_food_rating(message: Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await message.answer("оцените качество чистоты", reply_markup=kb.rating_kb())
    await state.set_state(RestaurantReview.cleanliness_rating)


@review_router.message(RestaurantReview.cleanliness_rating, F.text.in_(["1", "2", "3", "4", "5"]))
async def ask_cleanliness_rating(message: Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    await message.answer("дополнительные комментарии:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(RestaurantReview.extra_comments)


@review_router.message(RestaurantReview.extra_comments)
async def ask_extra_comments(message: Message, state: FSMContext):
    await state.update_data(thanks=message.text)
    await message.answer("спасибо за пройденный опрос")
    data = await state.get_data()
    print(data)
    database.execute(
        query="""
    INSERT INTO reviews (name, phone_number, visit_date, food_rating, cleanliness_rating, extra_comments)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
        params=(data["name"], data["phone_number"], data["visit_date"], data["food_rating"], data["cleanliness_rating"], data["extra_comments"])
    )
    await state.clear()
