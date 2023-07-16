from aiogram.utils.keyboard import InlineKeyboardBuilder


def select_start():
    menu = InlineKeyboardBuilder()
    menu.button(
        text='Помощь',
        callback_data='help'
    )
    return menu
