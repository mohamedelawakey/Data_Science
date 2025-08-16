import requests
import os
from dotenv import load_dotenv

load_dotenv()
my_key = os.getenv('API_KEY')

def display_weather(data_dic):
    for key, value in data_dic.items():
        print(f'{key.title()} : {value}')
  
def get_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_key}&units=metric&lang=ar'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == '404':
        print('city not found')
        return
    else:
        print('* data of weather * ')
        return display_weather(data['main'])

city = input('enter the city name: ')
get_weather_data(city)
