from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.types import Message
from bot_config import database
from aiogram.filters import Command

category_router = Router()

class AddCategory(StatesGroup):
    waiting_for_category = State()

@category_router.message(Command("add_category"))
async def start_adding_category(message: Message, state: FSMContext):
    await message.answer("Введите название новой категории:")
    await state.set_state(AddCategory.waiting_for_category)

@category_router.message(AddCategory.waiting_for_category)
async def save_category(message: Message, state: FSMContext):
    category_name = message.text
    database.execute("INSERT INTO dish_categories (category_name) VALUES (?)", (category_name,))
    await message.answer(f"Категория '{category_name}' добавлена!")
    await state.clear()
