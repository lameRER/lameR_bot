__all__ = ['register_user_commands']

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram import F

from .contact import contact
from .help import help_func, help_command
from .menu import menu
from .start import start
from .weather import weather, call_weather_api, message_weather_api


def register_user_commands(router: Router):
    router.message.register(start, CommandStart())
    router.callback_query.register(help_func, F.data == 'help')
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(menu, Command(commands='menu'))
    router.message.register(message_weather_api, Command(commands=['weather_api']))
    router.callback_query.register(menu, F.data == 'menu')
    router.callback_query.register(call_weather_api, F.data.startswith('weather_api'))
    router.callback_query.register(weather, F.data == 'weather')
    router.message.register(contact, Command(commands='contact'))
    router.callback_query.register(contact, F.data == 'contact')

