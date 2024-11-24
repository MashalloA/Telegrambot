from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot_config import database

admin_router = Router()

class AddDish(StatesGroup):
    name = State()
    description = State()
    price = State()

@admin_router.message(Command("add_dish"))
async def start_add_dish(message: Message, state: FSMContext):
    await message.answer("Введите название блюда:")
    await state.set_state(AddDish.name)

@admin_router.message(StateFilter(AddDish.name))
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите описание блюда:")
    await state.set_state(AddDish.description)

@admin_router.message(StateFilter(AddDish.description))
async def process_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите цену блюда:")
    await state.set_state(AddDish.price)

@admin_router.message(StateFilter(AddDish.price))
async def process_price(message: Message, state: FSMContext):
    try:
        price = float(message.text)
    except ValueError:
        await message.answer("Цена должна быть числом. Попробуйте снова.")
        return

    data = await state.get_data()
    database.execute(
        query="INSERT INTO dishes (food_name, description, price) VALUES (?, ?, ?)",
        params=(data["name"], data["description"], price)
    )
    await message.answer("Блюдо успешно добавлено!")
    await state.clear()