# import os
# import pip
# from background import keep_alive
# pip.main(['install','pytelegrambotapi'])
import telebot
import datetime
import json
from telebot import types
from req import req
from db import create_db, insert_db
from keys import *
from messages import *
from keyboards import *

bot = telebot.TeleBot(TELEGRAM_BOT_API, parse_mode="html")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, text=HELP_MESSAGE)
    
    
@bot.message_handler(commands=['language', 'lang', 'l'])
def change_language(message):
    bot.send_message(message.chat.id, text=CHANGE_LANGUAGE,
                     reply_markup=KEYBOARD_LANGUGE)
    
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text=START_MESSAGE_RU.format(
        message.from_user.first_name), reply_markup=KEYBOARD_GET_WEATHER_RU)
    
@bot.message_handler(content_types=['text'])
def choose_language(message):
    if message.text == 'Русский язык':
        bot.send_message(message.chat.id, text=CHOSEN_RU,
                         reply_markup=KEYBOARD_GET_WEATHER_RU)
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text == "Беларуская мова":
        bot.send_message(message.chat.id, text=CHOSEN_BY,
                         reply_markup=KEYBOARD_GET_WEATHER_BY)
        bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(content_types=['location'])
def location(message):

    create_db()

    insert_db(user_id=message.from_user.id,
              user_name=message.from_user.first_name,
              user_nickname=message.from_user.username)
    print(message.location.longitude, message.location.latitude)
    coord = {'coord': []}
    coord['coord'].append({
        "lat": message.location.latitude,
        "lon": message.location.longitude
    })

    with open('coord.json', 'w', encoding='utf-8') as file:
        json.dump(coord, file, indent=4, ensure_ascii=False)

    req()

    with open('resp_to_print.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

    with open('resp_to_print.json', 'w', encoding='utf-8') as file:
        pass

    if message.location is not None and data['main']['status'] == 'true':

        bot.send_message(message.chat.id, text=LOADING_MESSAGE_RU)

        bot.send_message(message.chat.id,
                         text=DATA_MESSAGE_RU.format(
                             data['main']['country'],
                             data['main']['city'],
                             datetime.datetime.fromtimestamp(
                                 int(message.date + 10800)).strftime('%d-%m %H:%M'),
                             str(data['main']['rise'])[10:],
                             str(data['main']['set'])[10:],
                             str(data['now']['weather']).capitalize(),
                             round(data['now']['temp'], 1),
                             data['now']['humidity'],
                             round(data['now']['wind'], 1),
                             str(data['d1']['weather']).capitalize(),
                             round(data['d1']['temp'], 1),
                             data['d1']['humidity'],
                             round(data['d1']['wind'], 1),
                             str(data['d2']['weather']).capitalize(),
                             round(data['d2']['temp'], 1),
                             data['d2']['humidity'],
                             round(data['d2']['wind'], 1)))
    else:
        bot.send_message(message.chat.id, text=ERROR_MESSAGE_RU)














def main():
    try:
        print("Running...")
        
        # keep_alive()
        bot.polling(none_stop=True)
    except:
        bot.polling(none_stop=True)


if __name__ == "__main__":
    main()
