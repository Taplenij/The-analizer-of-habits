from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton,
                           ReplyKeyboardMarkup, KeyboardButton)

keyboard = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='Начать', callback_data='start')
        ],
        [
            InlineKeyboardButton(text='Получить результаты', callback_data='info')
        ]
])

types = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='За один день', callback_data='day'),
        InlineKeyboardButton(text='За неделю', callback_data='week')
    ],
])

weekend = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='По дням', callback_data='week_d'),
        InlineKeyboardButton(text='По категориям', callback_data='week_c')
    ]
])

stop = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='СТОП', callback_data='stop')
        ],
])