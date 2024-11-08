from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from handlers.rewiew_dialog import RestaurantReview

dialogue_router = Router()

@dialogue_router.message(Command("opros"))
async def user_name(message: types.Message, state: FSMContext):
    await state.set_state(RestaurantReview.name)
    await message.answer("как вас зовут?")

@dialogue_router.message(RestaurantReview.name)
async def visit_date(message: types.Message, state: FSMContext):
    await state.set_state(RestaurantReview.visit)
    await message.answer("ваш инстаграм")

@dialogue_router.message(RestaurantReview.visit)
async def user_inst(message: types.Message, state: FSMContext):
    await state.set_state(RestaurantReview.inst)
    await message.answer("дата вашего посещения заведения")

@dialogue_router.message(RestaurantReview.inst)
async def food_rating(message: types.Message, state: FSMContext):
    await state.set_state(RestaurantReview.rating)
    await message.answer("ваша оценка еды?")

@dialogue_router.message(RestaurantReview.rating)
async def cleanliness_rating(message: types.Message, state: FSMContext):
    await state.set_state(RestaurantReview.cl_rating)
    await message.answer("как оцениваете чистоту заведения?")

@dialogue_router.message(RestaurantReview.cl_rating)
async def extra_comments(message: types.Message, state: FSMContext):
    await state.set_state(RestaurantReview.comments)
    await message.answer("доп комментарии/жалобы")

@dialogue_router.message(RestaurantReview.comments)
async def thx_rating(message: types.Message, state: FSMContext):
    await message.answer("спасибо за отзыв!")
    await state.clear()