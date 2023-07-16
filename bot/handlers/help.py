from typing import Union

from aiogram import types
from aiogram.filters import CommandObject

from bot.utils.commands import bot_commands


async def help_func(msg: Union[types.Message, types.CallbackQuery]):
    msg = msg.answer if type(msg) == types.Message else msg.message.edit_text
    return await msg(
        'Помощь и справка о боте\n'
        'Для того, чтобы получить информацию о команде, используйте /help <команда>\n'
    )


async def help_command(msg: types.Message, command: CommandObject):
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await msg.answer(f'{cmd[0]} - {cmd[1]}')
        return await msg.answer('Команда не найдена')
    else:
        await help_func(msg)
