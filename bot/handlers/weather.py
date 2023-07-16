from aiogram import types
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db import check_user
from bot.handlers import help_func
from bot.keyboards import select_weather
from bot.utils.weather import weather_api


async def weather(call: types.CallbackQuery, session: AsyncSession):
    await check_user(call, session)
    await call.message.edit_text(
        text='Выберите город',
        reply_markup=select_weather().as_markup()
    )


async def message_weather_api(msg: types.Message, session: AsyncSession):
    await check_user(msg, session)
    if len(msg.text.split()) > 1:
        await msg.answer(await weather_api(msg.text.split()[1]))
    else:
        await help_func(msg, session)


async def call_weather_api(call: types.CallbackQuery, session: AsyncSession):
    await check_user(call, session)
    await call.message.edit_text(await weather_api(call.data.split()[1]))
