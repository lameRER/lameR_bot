import os

import requests as requests


async def weather_api(city: str):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={os.getenv("weather_api")}'
    weather_data = requests.get(url).json()
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    description = weather_data['weather'][0]['description']
    result = \
        f'Сейчас в городе {city} {str(temperature)}°C\n'\
        f'{description}\n\n'\
        f'Ощущается как {str(temperature_feels)}°C\n'
    return result
