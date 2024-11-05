from dotenv import dotenv_values
from aiogram import Bot, Dispatcher

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()