from aiogram import Router, F, Bot
from aiogram.types import Message

router = Router()


@router.message(F.text == "Посты")
async def show_posts(message: Message, bot: Bot) -> None:
    await message.answer("Все посты на данный момент:")
