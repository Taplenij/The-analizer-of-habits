from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardMarkup, KeyboardButton)

keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Начать', callback_data='start'),
    InlineKeyboardButton(text='Настройки', callback_data='settings')]])
