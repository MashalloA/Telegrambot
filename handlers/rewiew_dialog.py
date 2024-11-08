from aiogram.fsm.state import State, StatesGroup

class RestaurantReview(StatesGroup):
    name = State()
    visit = State()
    inst = State()
    rating = State()
    cl_rating = State()
    comments = State()