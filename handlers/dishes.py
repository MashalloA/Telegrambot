from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from bot_config import database
from aiogram import Router


dishes_router = Router()


class AddDish(StatesGroup):
    name = State()
    description = State()
    price = State()

@dishes_router.message(Command("show_dishes"))
async def show_dishes(message: types.Message):
    rows = database.execute("SELECT name, description, price FROM dishes").fetchall()
    if not rows:
        await message.answer("Список блюд пуст.")
        return

    text = "".join([f"Название: {row[0]}\nОписание: {row[1]}\nЦена: {row[2]}" for row in rows])
    await message.answer(text)


@dishes_router.message(Command("add_dish"))
async def start_add_dish(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer("Введите название блюда:")
    await state.set_state(AddDish.name)

@dishes_router.message(AddDish.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите описание блюда:")
    await state.set_state(AddDish.description)

@dishes_router.message(AddDish.description)
async def process_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите цену блюда:")
    await state.set_state(AddDish.price)

@dishes_router.message(AddDish.price)
async def process_price(message: types.Message, state: FSMContext):
    try:
        price = float(message.text)
    except ValueError:
        await message.answer("Цена должна быть числом. Попробуйте снова.")
        return

    data = await state.get_data()
    database.execute(
        query="INSERT INTO dishes (name, description, price)"
        " VALUES (?, ?, ?)",
        params=(data["name"], data["description"], data["price"])
    )
    await message.answer("Блюдо успешно добавлено!")
    await state.clear()