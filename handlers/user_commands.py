from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import reply

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text="Добро пожаловать! Вы можете посмотреть и создать пост на сайте",
        reply_markup=reply.main_keyboard,
    )
