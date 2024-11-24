import asyncio

from handlers.admin import admin_router
from handlers.dishes import dishes_router
from handlers.random import random_router
from bot_config import bot, dp, database, dishes
from handlers.echo import echo_router
from handlers.review_dialog import review_router
from handlers.start import start_router
from handlers.info import info_router

async def on_startup(bot):
    database.create_table()
    await bot.send_message(chat_id=5634438231, text="я онлайн")

async def main():
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(random_router)
    dp.include_router(review_router)
    dp.include_router(admin_router)
    dp.include_router(dishes_router)

    dp.include_router(echo_router)

    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())