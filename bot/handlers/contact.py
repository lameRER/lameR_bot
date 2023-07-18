from typing import Union

from aiogram import types
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db import check_user


async def contact(msg: Union[types.Message, types.CallbackQuery], session: AsyncSession):
    await check_user(msg, session)
    msg = msg.answer if type(msg) == types.Message else msg.message.edit_text
    await msg(
        'Discodr: https://discord.gg/KWEwUtYQaX'
    )