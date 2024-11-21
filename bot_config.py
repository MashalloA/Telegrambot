from dotenv import dotenv_values
from aiogram import Bot, Dispatcher
from database.table import Database
from database.food_database import DishesDatabase

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

database = Database("database.db")
dishes = DishesDatabase("dishes.db")