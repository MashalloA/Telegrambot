from aiogram import Router, types, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import items.kb as kb

review_router = Router()


class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    day = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()
    thanks = State()


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
async def ask_phone(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("пожалуйста введите дату вашего посещения:")
    await message.answer("выберите месяц", reply_markup=kb.month_kb())
    await state.set_state(RestaurantReview.day)


@review_router.message(RestaurantReview.day)
async def ask_visit_date(message: Message, state: FSMContext):
    await state.update_data(visit_date=message.text)
    await message.answer("число: (от 1 до 31)", reply_markup=ReplyKeyboardRemove())
    await state.set_state(RestaurantReview.food_rating)


@review_router.message(RestaurantReview.food_rating)
async def ask_food(message: Message, state: FSMContext):
    day = message.text
    if not day.isdigit():
        await message.answer("введите число!")
        return
    day = int(day)
    if day < 1 or day > 31:
        await message.answer("пожалуйста, введите правильное число")
        return
    await state.update_data(food_rating=message.text)
    await message.answer("оцените качество еды", reply_markup=kb.rating_kb())
    await state.set_state(RestaurantReview.cleanliness_rating)


@review_router.message(RestaurantReview.cleanliness_rating, F.text.in_(["плохо", "хорошо", "отлично"]))
async def ask_cleanliness_rating(message: Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await message.answer("оцените качество чистоты", reply_markup=kb.rating_kb())
    await state.set_state(RestaurantReview.extra_comments)


@review_router.message(RestaurantReview.extra_comments, F.text.in_(["плохо", "хорошо", "отлично"]))
async def ask_extra_comments(message: Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    await message.answer("дополнительные комментарии:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(RestaurantReview.thanks)


@review_router.message(RestaurantReview.thanks)
async def ask_thanks(message: Message, state: FSMContext):
    await state.update_data(thanks=message.text)
    await message.answer("спасибо за отзыв")
