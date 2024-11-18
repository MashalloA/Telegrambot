import asyncio

from handlers.random import random_router
from bot_config import bot, dp, database
from handlers.echo import echo_router
from handlers.reg import reg_router
from handlers.review_dialog import review_router
from handlers.start import start_router
from handlers.info import info_router

async def on_startup():
    database.create_tables()

async def main():
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(random_router)
    dp.include_router(review_router)
    dp.include_router(reg_router)

    dp.include_router(echo_router)

    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())