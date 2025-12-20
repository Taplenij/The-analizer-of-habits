import asyncio
import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from data.tg_bot.requests import DBC
import keyboards as kb
from data.user_activity import UserActivity

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
    await callback.answer('Отлично!👏 Теперь я буду за тобой наблюдать😈')
    log.info('Start tracker')
    user_activity = UserActivity(callback.from_user.id)
    monitor_window = asyncio.create_task(user_activity.monitor_window())
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        monitor_window.cancel()
        print('interrupted')
    except Exception as e:
        print(f'EXCEPTION {e}')


@router.callback_query(F.data=='info')
async def second_stp(callback: CallbackQuery):
    await callback.answer(' ')
    await callback.message.answer('Выберите тип выводимых результатов:',
                                  reply_markup=kb.types)


@router.callback_query(F.data=='weeknd')
async def week(callback: CallbackQuery):
    await callback.answer(' ')
    await callback.message.answer('Выберите какой вид результатов хотите изучить:',
                                  reply_markup=kb.weekend)