import asyncio
import logging

from handlers import private_router
from bot_config import bot, dp, database
from handlers.group_filter import group_router
from handlers.echo import echo_router

async def on_startup(bot):
    database.create_table()
    await bot.send_message(chat_id=5634438231, text="я онлайн")

async def main():
    dp.include_router(private_router)
    dp.include_router(group_router)

    dp.include_router(echo_router)

    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # подключаем логи
    asyncio.run(main())