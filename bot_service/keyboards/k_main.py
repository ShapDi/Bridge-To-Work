from aiogram.types import (KeyboardButton,
                           ReplyKeyboardMarkup,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup)

from models.get_methods import get_k_main

def get_k_main():
    pass

def k_main():
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard = True,
        one_time_keyboard = True,
        input_field_placeholder = "Выберете опцию"
    )

    for i in get_k_main():
        pass
    return keyboard