import telebot
from telebot import types

KEYBOARD_LANGUGE = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
RU_BUTTON= types.KeyboardButton(text='Русский язык')
BY_BUTTON= types.KeyboardButton(text= 'Беларуская мова')
KEYBOARD_LANGUGE.add(RU_BUTTON, BY_BUTTON)

KEYBOARD_GET_WEATHER_RU = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
GET_WEATHER_RU_BUTTON = types.KeyboardButton(text='Узнать погоду ☁', request_location=True)
KEYBOARD_GET_WEATHER_RU.add(GET_WEATHER_RU_BUTTON)

KEYBOARD_GET_WEATHER_BY = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
GET_WEATHER_BY_BUTTON = types.KeyboardButton(text="Даведацца надвор'е ☁", request_location=True)
KEYBOARD_GET_WEATHER_BY.add(GET_WEATHER_BY_BUTTON)

