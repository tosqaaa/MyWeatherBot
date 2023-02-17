# import os
# import pip
# from background import keep_alive
# pip.main(['install','pytelegrambotapi'])
import logging
from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram import types
from aiogram.utils import executor
import datetime, json
import time
from req import req
from db import *
from keys import *
from messages import *
from keyboards import *
from translate import trans_to_be

bot = Bot(token=TELEGRAM_BOT_API, parse_mode="html")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, text=START_MESSAGE_RU.format(message.from_user.first_name), reply_markup=KEYBOARD_LANGUGE)
    
    create_db()

    insert_db(user_id=message.from_user.id,
              user_name=message.from_user.first_name,
              user_nickname=message.from_user.username)
    
@dp.message_handler(commands=['my_lang'])
async def get_language(message: types.Message):
    await bot.send_message(message.chat.id, text=get_language_from_user(user_id= message.from_user.id))
    
@dp.message_handler(commands=['language', 'lang', 'l'])
async def change_language(message):
    await bot.send_message(message.chat.id, text=CHANGE_LANGUAGE,
                     reply_markup=KEYBOARD_LANGUGE)
    
@dp.message_handler(commands=['time'])
async def get_date(message: types.Message):
    await bot.send_message (message.from_user.id, text=message.date)
    
    
@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    await message.answer(HELP_MESSAGE)
    
    
@dp.message_handler(content_types=['text'])
async def choose_language(message: types.Message):
    if message.text == 'Русский язык':
        await bot.send_message(message.chat.id, text=CHOSEN_RU,
                         reply_markup=KEYBOARD_GET_WEATHER_RU)
        await message.delete()
        
        change_language_in_db(user_language="ru", user_id=message.from_user.id)
        
    elif message.text == "Беларуская мова":
        await bot.send_message(message.chat.id, text=CHOSEN_BY,
                         reply_markup=KEYBOARD_GET_WEATHER_BY)
        await message.delete()
        
        change_language_in_db(user_language="by", user_id=message.from_user.id)
        


@dp.message_handler(content_types=['location', 'text'])
async def location(message):
        
    # print(message.location.longitude, message.location.latitude)
    
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

        if get_language_from_user(message.from_user.id) == "by":
            await bot.send_message(message.chat.id, text=LOADING_MESSAGE_BY)

            await bot.send_message(message.chat.id,
                             DATA_MESSAGE_BY.format(
                                 data['main']['country'],
                                 trans_to_be(data['main']['city']),
                                 message.date.strftime('%d.%m.%Y'), 
                                 str(data['main']['rise'])[10:],
                                 str(data['main']['set'])[10:],
                                 trans_to_be(
                                     str(data['now']['weather']).capitalize()),
                                 round(data['now']['temp'], 1),
                                 data['now']['humidity'],
                                 round(data['now']['wind'], 1),
                                 trans_to_be(
                                     str(data['d1']['weather']).capitalize()),
                                 round(data['d1']['temp'], 1),
                                 data['d1']['humidity'],
                                 round(data['d1']['wind'], 1),
                                 trans_to_be(
                                     str(data['d2']['weather']).capitalize()),
                                 round(data['d2']['temp'], 1),
                                 data['d2']['humidity'],
                                 round(data['d2']['wind'], 1)), reply_markup=KEYBOARD_LANGUGE)
        else:
            await bot.send_message(message.chat.id, text=LOADING_MESSAGE_RU)

            await bot.send_message(message.chat.id,
                             DATA_MESSAGE_RU.format(
                                 data['main']['country'],
                                 data['main']['city'],
                                 message.date.strftime('%d.%m.%Y'),    
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
                                 round(data['d2']['wind'], 1)), reply_markup=KEYBOARD_LANGUGE)
    else:
        await bot.send_message(message.chat.id, text=ERROR_MESSAGE_RU)
        
    with open('lang.json', 'w') as file:
        pass



    

    


def main():
    try:
        print("Running")
        # keep_alive()
        executor.start_polling(dp,  skip_updates=True)
    except Exception() as ex:
        print(type(ex))

        
        
        
if __name__ == "__main__":
    main()
    
        
    
