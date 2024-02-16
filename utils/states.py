from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    title = State()
    description = State()
    link = State()
