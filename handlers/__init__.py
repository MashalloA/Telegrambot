from aiogram import Router, F

from .add_category import category_router
from .admin import admin_router
from .dishes import dishes_router
from .random import random_router
from .review_dialog import review_router
from .start import start_router
from .info import info_router

private_router = Router()
private_router.include_router(start_router)
private_router.include_router(admin_router)
private_router.include_router(info_router)
private_router.include_router(dishes_router)
private_router.include_router(category_router)
private_router.include_router(review_router)
private_router.include_router(random_router)

