import asyncpg as pg
from aiogram import Bot
from tg_bot.token import TOKEN



class DBC:
    def __init__(self):
        self.pool = None
        self.bot = Bot(token=TOKEN)

    async def create_pool(self):
        self.pool = pg.create_pool(
            user='postgres',
            password='password',
            database='analizer_of_habits',
            host='localhost',
            port='5432',
            min_size=5,
            max_size=10
        )
        self.bot.pool = self.pool
        return self.pool

    async def record_id(self, tg_id):
        if not self.pool:
            raise RuntimeError('Pool not initialized')
        try:
            async with self.pool.acquire as con:
                await con.execute('INSERT INTO tg_id_info(tg_id) VALUES $1', tg_id)
        except pg.exceptions.UniqueViolationError:
            print('This id already in database')

    async def record_activity(self, tg_id, app, time):
        if not self.pool:
            raise RuntimeError('Pool not initialized')
        try:
            async with self.pool.acquire as con:
                await con.execute('INSERT INTO user_info(tg_id, app, time)'
                                  ' VALUES $1, $2, $3', tg_id, app, time)
        except pg.exceptions.UniqueViolationError:
            print('This record already exists')

    async def get_info(self, tg_id):
        if not self.pool:
            raise RuntimeError('Pool not initialized')
        async with self.pool.acquire as con:
            info = [rec for rec in con.fetch('SELECT FROM user_info(app, time)'
                                             ' WHERE tg_id = $1', tg_id)]
            return info

    async def increment_time(self, tg_id, time):
        if not self.pool:
            raise RuntimeError('Pool not initialized')
        async with self.pool.acquire as con:
            await con.execute('UPDATE user_info SET time = time + $1 '
                              'WHERE tg_id = $2', time, tg_id)

    async def on_shutdown(self):
        if hasattr(self.bot, 'pool') and self.bot.pool:
            await self.bot.pool.closed()
