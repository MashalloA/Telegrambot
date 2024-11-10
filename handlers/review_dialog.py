from aiogram import Router, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command

review_router = Router()


class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@review_router.callback_query(F.data == "review")
async def start_review(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Как вас зовут?")
    await state.set_state(RestaurantReview.name)
    await callback_query.answer()


@review_router.message(RestaurantReview.name)
async def ask_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Ваш номер телефона или Instagram:")
    await state.set_state(RestaurantReview.phone_number)


@review_router.message(RestaurantReview.phone_number)
async def ask_phone_or_instagram(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("Дата вашего посещения (в формате ДД.ММ.ГГГГ):")
    await state.set_state(RestaurantReview.visit_date)


@review_router.message(RestaurantReview.visit_date)
async def ask_visit_date(message: Message, state: FSMContext):
    await state.update_data(visit_date=message.text)

    food_rating_kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3")],
            [KeyboardButton(text="4"), KeyboardButton(text="5")]
        ], resize_keyboard=True, one_time_keyboard=True
    )
    await message.answer("Как оцениваете качество еды?", reply_markup=food_rating_kb)
    await state.set_state(RestaurantReview.food_rating)


@review_router.message(RestaurantReview.food_rating)
async def ask_food_rating(message: Message, state: FSMContext):
    await state.update_data(food_rating=message.text)

    cleanliness_rating_kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3")],
            [KeyboardButton(text="4"), KeyboardButton(text="5")]
        ],
    )
    await message.answer("Как оцениваете чистоту заведения?", reply_markup=cleanliness_rating_kb)
    await state.set_state(RestaurantReview.cleanliness_rating)


@review_router.message(RestaurantReview.cleanliness_rating)
async def ask_cleanliness_rating(message: Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await message.answer("Дополнительные комментарии или жалобы:")
    await state.set_state(RestaurantReview.extra_comments)


@review_router.message(RestaurantReview.extra_comments)
async def receive_extra_comments(message: Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)

    user_data = await state.get_data()
    review_text = (
        f"Спасибо за отзыв!\n\n"
        f"Имя: {user_data['name']}\n"
        f"Контакт: {user_data['phone_number']}\n"
        f"Дата посещения: {user_data['visit_date']}\n"
        f"Оценка еды: {user_data['food_rating']}\n"
        f"Оценка чистоты: {user_data['cleanliness_rating']}\n"
        f"Комментарии: {user_data['extra_comments']}")
    await message.answer(review_text)
    await state.clear()