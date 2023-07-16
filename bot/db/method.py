import datetime
from typing import Union

from aiogram import types
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User


async def check_user(msg: Union[types.Message, types.CallbackQuery], session: AsyncSession):
    user: User = (await session.execute(select(User).where(User.user_id == msg.from_user.id))).scalar()
    if user:
        await registry_user(msg, session)
    else:
        await update_user(msg, session)
    return user


async def registry_user(msg: Union[types.Message, types.CallbackQuery], session: AsyncSession):
    await session.merge(User(
        user_id=msg.from_user.id,
        username=msg.from_user.username,
        upp_date=datetime.datetime.now()
    ))
    await session.commit()


async def update_user(msg: Union[types.Message, types.CallbackQuery], session: AsyncSession):
    await session.merge(User(
        user_id=msg.from_user.id,
        username=msg.from_user.username))
    await session.commit()
