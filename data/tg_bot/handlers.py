from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from data.tg_bot.requests import DBC
import keyboards as kb

router = Router()

req = DBC()


@router.message(Command('start'))
async def com_start(message: Message):
    await message.answer('Привет,'
                         ' я - бот, который занимается анализом твоих действий на компьютере.'
                         ' Нажми кнопку "Начать", чтобы я приступил к работе. Также ты можешь'
                         ' изменить что-либо в настройках', reply_markup=kb.keyboard)
    await req.create_pool()
    await req.record_id(message.from_user.id)


@router.message(F.text.lower() == 'сосал?')  # Sexy secret
async def sosal(message: Message):
    await message.reply('Да')
