from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

bot_commands = (
    ('start', 'Начало работы с ботом'),
    ('help', 'Помошь с ботом'),
    ('menu', 'Список функционала бота'),
    ('weather_api', 'Узнать текущую погоду'),
)


async def set_commands(bot: Bot):
    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    await bot.set_my_commands(commands_for_bot, BotCommandScopeDefault())
