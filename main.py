import asyncio
import logging
import os

from aiogram import Dispatcher, Bot


async def main():
    logging.basicConfig(level=logging.DEBUG)
    token = os.getenv('token_api')
    dp = Dispatcher()
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
