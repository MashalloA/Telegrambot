from aiogram import Router, types, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import items.kb as kb
from bot_config import (
    database,
    reg_users,
    reg_account,
    registered_users,
    reviewed_users
)

review_router = Router()


class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
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
    await message.answer("Ваш номер телефона:")
    await state.set_state(RestaurantReview.phone_number)


@review_router.message(RestaurantReview.phone_number)
async def ask_phone(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("пожалуйста введите дату вашего посещения:")
    await message.answer("введите дату вашего посещения (в формате ДД,ММ,ГГГГ)")
    await state.set_state(RestaurantReview.food_rating)


@review_router.message(RestaurantReview.food_rating)
async def ask_food(message: Message, state: FSMContext):
    await state.update_data(food_rating=message.text)
    await message.answer("оцените качество еды", reply_markup=kb.rating_kb())
    await state.set_state(RestaurantReview.cleanliness_rating)


@review_router.message(RestaurantReview.cleanliness_rating, F.text.in_(["1", "2", "3", "4", "5"]))
async def ask_cleanliness_rating(message: Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await message.answer("оцените качество чистоты", reply_markup=kb.rating_kb())
    await state.set_state(RestaurantReview.extra_comments)


@review_router.message(RestaurantReview.extra_comments, F.text.in_(["1", "2", "3", "4", "5"]))
async def ask_extra_comments(message: Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    await message.answer("дополнительные комментарии:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(RestaurantReview.thanks)


@review_router.message(RestaurantReview.thanks)
async def ask_thanks(message: Message, state: FSMContext):
    await state.update_data(thanks=message.text)
    id_user = message.from_user.id
    if message.text.lower() == "подтвердить":
        data = await state.get_data()
        database.execute(
            query="""
                  INSERT INTO reviews (name, phone_number, visit_date, food_rating, cleanliness_rating, extra_comments, total_rating)
                  VALUES (?,?,?,?,?,?,?)      
                """,
            params=(
                data["name"],
                data["phone_number"],
                data["visit_date"],
                data["food_rating"],
                data["cleanliness_rating"],
                data["extra_comments"],
                data["total_rating"],
            ),
        )
        await message.answer(
            "Ваш отзыв был принят. Спасибо!", reply_markup=types.ReplyKeyboardRemove()
        )
        await state.clear()

    elif message.text.lower() == "отклонить":
        if id_user in reviewed_users:
            reviewed_users.remove(id_user)

        await message.answer(
            "Отзыв отменен",
            reply_markup=types.ReplyKeyboardRemove(),
        )
        await state.clear()
    else:
        await message.answer("Пожалуйста, выберите 'Подтвердить' или 'Отклонить'.")
