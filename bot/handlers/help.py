from typing import Union

from aiogram import types
from aiogram.filters import CommandObject
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db import check_user
from bot.keyboards import select_contact
from bot.utils import bot_commands


async def help_func(msg: Union[types.Message, types.CallbackQuery], session: AsyncSession):
    await check_user(msg, session)
    msg = msg.answer if type(msg) == types.Message else msg.message.edit_text
    await msg(
        text='Помощь и справка о боте\n'
        'Для того, чтобы получить информацию о команде, используйте /help <команда>\n',
        reply_markup=select_contact().as_markup()
    )


async def help_command(msg: types.Message, command: CommandObject, session: AsyncSession):
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await msg.answer(f'{cmd[0]} - {cmd[1]}')
        return await msg.answer('Команда не найдена')
    else:
        await help_func(msg, session)
