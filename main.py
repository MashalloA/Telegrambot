import asyncio

from handlers.random import rnd_router
from bot_config import bot, dp
from handlers.echo import echo_router
from handlers.start import start_router
from handlers.info import info_router


async def main():
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(echo_router)
    dp.include_router(rnd_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())