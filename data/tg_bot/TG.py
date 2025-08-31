import asyncio
from data.requests import DBC
from token import TOKEN
from aiogram import Bot, Dispatcher

bot = Bot(token=TOKEN)

db = DBC()

dp = Dispatcher()


async def main():
    await db.create_pool()
    await dp.start_polling(bot)
    await db.on_shutdown()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot was stopped')
