from aiogram import types
from bot.keyboards import select_start


async def start(msg: types.Message):
    await msg.answer(
        text=f'Привет {msg.from_user.first_name}.\n'
        'Впервые у нас?\n'
        'Для того, чтобы получить информацию о функционале, используйте /help\n',
        reply_markup=select_start().as_markup()
    )
