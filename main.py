import telebot
import time
import requests

BOT_TOKEN = '6581797741:AAGBiA9z1s_qh_3qBCZH7m_CuGlbhx3N6lM'
WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=a57925d395bac1fd44567afaad416712'

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.reply_to(message, "Bizning ilk botimizga hush kelibsiz!")

@bot.message_handler(commands=['weather'])
def get_weather(message):
    city = message.text[9:]
    data = get_full_data(city)
    temp = round(data.get("main", {}).get('temp', 0) - 273.15)
    main = data.get("weather")[0].get('main')
    bot.send_message(message.chat.id, f"Hozirda {city}da havo harorati {temp} va {main} bo'lishi kutulmoqda!")

@bot.message_handler(func = lambda message: True)
def reply_msg(message):
    bot.send_message(message.chat.id, message.text)

    bot.send_message(message.chat.id, "Sleep tugadi!")

def get_full_data(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=a57925d395bac1fd44567afaad416712'.format(city)
    response = requests.get(url)
    return response.json()


bot.infinity_polling()