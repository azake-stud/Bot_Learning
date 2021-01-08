from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton

start_ = InlineKeyboardButton('Начать', callback_data='starting')
start_btn = InlineKeyboardMarkup().add(start_)

registartion = InlineKeyboardButton("Регистрация", callback_data='reg')
info = InlineKeyboardButton("Подробнее", callback_data='info')
reg_btns = InlineKeyboardMarkup().row(registartion, info)

