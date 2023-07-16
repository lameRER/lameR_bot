import asyncio
import logging
import os

from aiogram import Dispatcher, Bot
from handlers import register_user_commands
from utils.commands.command import set_commands


async def main():
    logging.basicConfig(level=logging.DEBUG)
    token = os.getenv('token_api')
    dp = Dispatcher()
    register_user_commands(dp)
    bot = Bot(token)
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
