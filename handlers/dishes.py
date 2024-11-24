from aiogram import F
from aiogram.types import CallbackQuery
from bot_config import database
from aiogram import Router

dishes_router = Router()

@dishes_router.callback_query(F.data == "show_dishes")
async def show_menu(callback: CallbackQuery):
    dishes = database.execute1("SELECT food_name, description, price FROM dishes").fetchall()
    if not dishes:
        await callback.message.edit_text("Меню пока пусто.")
        return

    menu_text = "Меню:\n\n"
    for dish in dishes:
        menu_text += f" {dish[0]}\nОписание: {dish[1]}\nЦена: {dish[2]} руб.\n\n"

    await callback.message.edit_text(menu_text)