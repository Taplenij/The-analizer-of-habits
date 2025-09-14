import asyncio
from data.tg_bot.requests import DBC
from config import TOKEN
from aiogram import Bot, Dispatcher
from handlers import router

bot = Bot(token=TOKEN)
db = DBC()
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await db.create_pool()
    await dp.start_polling(bot)
    await db.on_shutdown()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot was stopped')
