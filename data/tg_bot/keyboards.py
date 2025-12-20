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
        InlineKeyboardButton(text='За один день', callback_data='one'),
        InlineKeyboardButton(text='За неделю', callback_data='weeknd')
    ],
    [
        InlineKeyboardButton(text='Получить все результаты', callback_data='all')
    ]
])

weekend = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Общий', callback_data='weeknd_genrl'),
        InlineKeyboardButton(text='Подробный', callback_data='weekend_detld')
    ]
])
