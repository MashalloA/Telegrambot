import asyncio

from dialog import dialogue_router
from handlers.random import random_router
from bot_config import bot, dp
from handlers.echo import echo_router
from handlers.start import start_router
from handlers.info import info_router


async def main():
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(random_router)
    dp.include_router(dialogue_router)
    dp.include_router(echo_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())