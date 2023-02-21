
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

KEYBOARD_LANGUGE = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
RU_BUTTON = InlineKeyboardButton(text='Русский язык')
BY_BUTTON = InlineKeyboardButton(text='Беларуская мова')
KEYBOARD_LANGUGE.add(RU_BUTTON, BY_BUTTON)

KEYBOARD_GET_WEATHER_RU = ReplyKeyboardMarkup(
    resize_keyboard=True, row_width=1)
GET_WEATHER_RU_BUTTON = KeyboardButton(
    text='Узнать погоду ☁', request_location=True)
KEYBOARD_GET_WEATHER_RU.add(GET_WEATHER_RU_BUTTON)

KEYBOARD_GET_WEATHER_BY = ReplyKeyboardMarkup(
    resize_keyboard=True, row_width=1)
GET_WEATHER_BY_BUTTON = KeyboardButton(
    text="Даведацца надвор'е ☁", request_location=True)
KEYBOARD_GET_WEATHER_BY.add(GET_WEATHER_BY_BUTTON)
