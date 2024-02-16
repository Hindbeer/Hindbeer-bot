import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import bot_messages, user_commands, post_form
from config import TELEGRAM_TOKEN


async def main() -> None:
    bot = Bot(TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_routers(user_commands.router, post_form.router, bot_messages.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
