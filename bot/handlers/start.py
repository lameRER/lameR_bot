from aiogram import types
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db import check_user
from bot.keyboards import select_start


async def start(msg: types.Message, session: AsyncSession):
    user = await check_user(msg, session)
    if user:
        await msg.answer(text=f'Привет {msg.from_user.first_name}.\n')
    else:
        await msg.answer(
            text=f'Привет {msg.from_user.first_name}.\n'
            'Впервые у нас?\n'
            'Для того, чтобы получить информацию о функционале, используйте /help\n',
            reply_markup=select_start().as_markup()
        )
