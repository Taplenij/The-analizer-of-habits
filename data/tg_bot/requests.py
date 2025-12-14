import asyncpg as pg
from aiogram import Bot
from config import TOKEN


class DBC:
    def __init__(self):
        self.pool = None
        self.bot = Bot(token=TOKEN)

    async def create_pool(self):
        self.pool = await pg.create_pool(
            user='---',
            password='---',
            database='---',
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
                await con.execute(f'INSERT INTO tg_id_list(tg_id) VALUES($1)', tg_id)
        except pg.exceptions.UniqueViolationError:
            print('This ID is already in database')

    async def record_activity(self, tg_id, app, time):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        try:
            async with self.pool.acquire() as con:
                await con.execute(f'INSERT INTO user_info(tg_id, app, use_time) '
                                  f'VALUES($1, $2, $3)', tg_id, app, time)
        except pg.exceptions.UniqueViolationError:
            print('This record is already exists')

    async def get_info(self, tg_id, table):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        async with self.pool.acquire() as con:
            info = [(rec['app'], rec['use_time'].isoformat()) for rec in
                    (await con.fetch(f'SELECT app, use_time FROM $1 '
                                     f'WHERE tg_id = $2', table, tg_id))]
            return info

    async def increment_time(self, tg_id, time, table):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        async with self.pool.acquire() as con:
            await con.execute(f'UPDATE $1 SET use_time = use_time + $2 '
                              f'WHERE tg_id = $3', table, time, tg_id)

    async def categories(self, tg_id, table):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        async with self.pool.acquire() as con:
            ctgrs = await con.fetch(f'SELECT category FROM $1 WHERE tg_id = $2', tg_id, table)
            return [c['category'] for c in ctgrs]

    async def drop_info(self):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        async with self.pool.acquire() as con:
            await con.execute('DELETE FROM user_info')

    async def get_days(self, tg_id):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        async with self.pool.acquire() as con:
            days = await con.fetch(f'SELECT day FROM total_info WHERE tg_id = $1', tg_id)
            return [day['day'].isoformat() for day in days]

    async def on_shutdown(self):
        if hasattr(self.bot, 'pool') and self.bot.pool:
            await self.bot.pool.closed()
