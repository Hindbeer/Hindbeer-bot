from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config import ADMIN_ID
from utils.states import Form
from services.server import add_post

router = Router()


@router.message(F.text == "Создать")
async def fill_profile(message: Message, state: FSMContext):
    if message.from_user.username != ADMIN_ID:
        await message.answer("Извините, но данный функционал вам не доступен")
    else:
        await state.set_state(Form.title)
        await message.answer("Введите оглавление поста")


@router.message(Form.title)
async def form_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(Form.description)
    await message.answer("Введите описание")


@router.message(Form.description)
async def form_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(Form.link)
    await message.answer("Введите ссылку на проект")


@router.message(Form.link)
async def form_link(message: Message, state: FSMContext):
    await state.update_data(links=message.text)
    await state.set_state(Form.link)
    data = await state.get_data()
    print(data)
    await state.clear()

    print(add_post(data=data))
    await message.answer(f"Пост успешно отправлен")
