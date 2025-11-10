import asyncpg as pg
from aiogram import Bot
from config import TOKEN


class DBC:
    def __init__(self):
        self.pool = None
        self.bot = Bot(token=TOKEN)

    async def create_pool(self):
        self.pool = await pg.create_pool(
            user='--',
            password='--',
            database='analizer_of_habits',
            host='localhost',
            port='5432',
            min_size=5,
            max_size=10
        )
        self.bot.pool = self.pool
        print('pool initialized')
        return self.pool

    async def record_id(self, tg_id):
        if not self.pool:
            raise pg.exceptions.InterfaceError('Pool is not initialized')
        try:
            async with self.pool.acquire() as con:
                async with con.transaction():
                    await con.execute(f'INSERT INTO tg_id_list(tg_id) VALUES({tg_id})')
        except pg.exceptions.UniqueViolationError:
            print('This ID is already in database')

    async def record_activity(self, tg_id, app, time):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        try:
            async with self.pool.acquire() as con:
                async with con.transaction():
                    await con.execute(f'INSERT INTO user_info(tg_id, app, time) '
                                      f'VALUES({tg_id}, {app}, {time})')
        except pg.exceptions.UniqueViolationError:
            print('This record is already exists')

    async def get_info(self, tg_id):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        async with self.pool.acquire() as con:
            async with con.transaction():
                info = [rec for rec in con.fetch(f'SELECT FROM user_info(app, time) '
                                                 f'WHERE tg_id = {tg_id}')]
            return info

    async def increment_time(self, tg_id, time):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        async with self.pool.acquire() as con:
            async with con.transaction():
                await con.execute(f'UPDATE user_info SET time = time + {time} '
                                  f'WHERE tg_id = {tg_id}')

    async def on_shutdown(self):
        if hasattr(self.bot, 'pool') and self.bot.pool:
            await self.bot.pool.closed()
