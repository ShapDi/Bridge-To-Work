from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.k_main import get_k_main

router = Router()



@router.message(CommandStart())
async def start(message:Message):
    # Проверка аккаунта
    await message.answer("", reply_markup = get_k_main())

@router.message(F.text.lower() == '#')
async def search(message:Message):
    pass