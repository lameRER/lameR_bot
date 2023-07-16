__all__ = ['register_user_commands']

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram import F

from .help import help_func, help_command
from .start import start


def register_user_commands(router: Router):
    router.message.register(start, CommandStart())
    router.callback_query.register(help_func, F.data == 'help')
    router.message.register(help_command, Command(commands=['help']))
