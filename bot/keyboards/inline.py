from aiogram.utils.keyboard import InlineKeyboardBuilder


def select_start():
    menu = InlineKeyboardBuilder()
    menu.button(
        text='Меню',
        callback_data='menu'
    )
    menu.button(
        text='Помощь',
        callback_data='help'
    )
    return menu


def select_menu():
    menu = InlineKeyboardBuilder()
    menu.button(
        text='Погода',
        callback_data='weather'
    )
    return menu


def select_weather():
    menu = InlineKeyboardBuilder()
    city = 'Санкт-Петербург'
    menu.button(
        text=city,
        callback_data=f'weather_api {city}'
    )
    return menu
