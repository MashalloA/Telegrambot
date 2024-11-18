from dotenv import dotenv_values
from aiogram import Bot, Dispatcher
from database.table import Database

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
reviewed_users = set()
reg_account = set()
registered_users = {}
reg_users = {}
database = Database("database.sqlite")