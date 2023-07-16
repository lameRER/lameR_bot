from typing import Union
from aiogram import types
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db import check_user
from bot.keyboards import select_menu


async def menu(msg: Union[types.Message, types.CallbackQuery], session: AsyncSession):
    await check_user(msg, session)
    msg = msg.answer if type(msg) == types.Message else msg.message.edit_text
    await msg(
        text='Меню',
        reply_markup=select_menu().as_markup()
    )
