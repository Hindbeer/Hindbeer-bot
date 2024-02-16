from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Создать"), KeyboardButton(text="Посты")]],
    resize_keyboard=True,
    selective=True,
)
