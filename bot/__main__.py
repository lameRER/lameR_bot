import asyncio
import logging
import os

from aiogram import Dispatcher, Bot
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from bot.middlewares.db import DbSessionMiddleware
from bot.handlers import register_user_commands
from bot.utils.commands.command import set_commands


async def main():
    logging.basicConfig(level=logging.DEBUG)

    mysql_url = URL.create(
        drivername="mysql+aiomysql",
        username=os.getenv('db_user'),
        password=os.getenv('db_password'),
        host=os.getenv('db_host'),
        database=os.getenv('database')
    )
    engine = create_async_engine(mysql_url, echo=True)
    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    token = os.getenv('token_api')
    print(f'token: {token}')
    dp = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(session_pool=session_maker))
    dp.callback_query.middleware(CallbackAnswerMiddleware())
    register_user_commands(dp)

    bot = Bot(token)
    await set_commands(bot)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())
