__all__ = [
    'set_commands',
    'bot_commands',
    'weather_api'
]

from .commands.command import set_commands, bot_commands
from .weather.weather_api import weather_api
