import asyncio
import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command

from data.tg_bot.requests import DBC
import keyboards as kb
from data.user_activity import UserActivity
from data.display_statistics import Statistic

log = logging.getLogger('handlers')
log.setLevel(logging.DEBUG)
sh = logging.StreamHandler()

formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

sh.setFormatter(formatter)
log.addHandler(sh)

router = Router()

req = DBC()
stat = Statistic()

active_trackers = {}
@router.message(Command('start'))
async def com_start(message: Message):
    await message.answer('Привет,'
                         ' я - бот, который занимается анализом твоих действий на компьютере.'
                         ' Нажми кнопку "Начать", чтобы я приступил к работе. Также ты можешь'
                         ' изменить что-либо в настройках.', reply_markup=kb.keyboard)
    await req.create_pool()
    await req.record_id(message.from_user.id)


@router.callback_query(F.data == 'start')
async def first_stp(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id in active_trackers:
        await callback.answer('Трекер уже запущен')
        return
    else:
        user_act = UserActivity(user_id)
        active_trackers[user_id] = user_act

        await callback.answer('Отлично!👏 Теперь я буду за тобой наблюдать😈')
        log.info('Start tracker')

        await callback.message.answer('Вы можете остановить работу программы, если хотите.',
                                      reply_markup=kb.stop)

        asyncio.create_task(active_trackers[user_id].monitor_window())



@router.callback_query(F.data=='stop')
async def stop(callback: CallbackQuery):
    user_id = callback.from_user.id

    if user_id in active_trackers:
        user_act = active_trackers[user_id]
        user_act.WORKER = False

        del active_trackers[user_id]
        await callback.answer(' ')
        await callback.message.answer('Программа была остановлена🛑')
    else:
        await callback.answer('Трекер и так не запущен', show_alert=True)


@router.callback_query(F.data=='info')
async def second_stp(callback: CallbackQuery):
    await callback.answer(' ')
    await callback.message.answer('Выберите тип выводимых результатов:',
                                  reply_markup=kb.types)


@router.callback_query(F.data=='day')
async def day(callback:CallbackQuery):
    await callback.answer(' ')
    await stat.top10(callback.from_user.id)
    await callback.message.answer('Вот что мне удалось записать:')
    photo = FSInputFile('t10.png')
    await callback.message.answer_photo(photo)


@router.callback_query(F.data=='week')
async def week(callback: CallbackQuery):
    await callback.answer(' ')
    await callback.message.answer('Выберите, в каком виде хотите получить результат:',
                                  reply_markup=kb.weekend)

@router.callback_query(F.data=='week_d')
async def week_d(callback: CallbackQuery):
    await callback.answer(' ')
    await stat.week_d(callback.from_user.id)
    await callback.message.answer('Дневная статистика:')
    photo = FSInputFile('week_d.png')
    await callback.message.answer_photo(photo)