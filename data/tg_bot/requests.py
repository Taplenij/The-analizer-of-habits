import asyncpg as pg
from aiogram import Bot
from config import TOKEN
import numpy as np


class DBC:
    def __init__(self):
        self.pool = None
        self.bot = Bot(token=TOKEN)

    async def create_pool(self):
        self.pool = await pg.create_pool(
            user='postgres',
            password='password',
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
        try:
            if not self.pool:
                raise pg.exceptions.InterfaceError('Pool is not initialized')
            try:
                async with self.pool.acquire() as con:
                    await con.execute(f'INSERT INTO tg_id_list(tg_id) VALUES($1)', tg_id)
            except pg.exceptions.UniqueViolationError:
                print('This ID is already in database')
        except KeyboardInterrupt:
            print('Stop query')

    async def record_activity(self, tg_id, app, time, table, category, day=None):
        try:
            if not self.pool:
                raise RuntimeError('Pool is not initialized')
            try:
                async with self.pool.acquire() as con:
                    if table == 'user_info':
                        await con.execute('INSERT INTO user_info(tg_id, category,'
                                          'app, use_time) '
                                          'VALUES($1, $2, $3, $4)', tg_id, category, app, time)
                    elif table == 'total_info':
                        await con.execute('INSERT INTO total_info(tg_id, day,'
                                          'category, app, use_time) '
                                          'VALUES($1, $2, $3, $4, $5)',
                                          tg_id, day, category, app, time)
            except pg.exceptions.UniqueViolationError:
                print('This record is already exists')
        except KeyboardInterrupt:
            print('Stop query')

    async def get_info(self, tg_id, table):
        try:
            if not self.pool:
                raise RuntimeError('Pool is not initialized')
            async with self.pool.acquire() as con:
                info = np.array([[rec['app'], rec['use_time'].seconds] for rec in
                        (await con.fetch(f'SELECT app, use_time FROM {table} '
                                         'WHERE tg_id = $1', tg_id))])
                return info
        except KeyboardInterrupt:
            print('Stop query')

    async def get_time(self, tg_id, table):
        try:
            if not self.pool:
                raise RuntimeError('Pool is not initialized')
            async with self.pool.acquire() as con:
                times = np.array([str(t['use_time']) for t in
                                  (await con.fetch(f'SELECT use_time FROM {table} '
                                                   'WHERE tg_id = $1', tg_id))])
                return times
        except KeyboardInterrupt:
            print('Stop query')

    async def categories(self, tg_id, table):
        try:
            if not self.pool:
                raise RuntimeError('Pool is not initialized')
            async with self.pool.acquire() as con:
                ctgrs = await con.fetch(f'SELECT category FROM {table} WHERE tg_id = $1', tg_id)
                return np.array([c['category'] for c in ctgrs])
        except KeyboardInterrupt:
            print('Stop query')

    async def get_days(self, tg_id):
        try:
            if not self.pool:
                raise RuntimeError('Pool is not initialized')
            async with self.pool.acquire() as con:
                days = await con.fetch(f'SELECT day FROM total_info WHERE tg_id = $1', tg_id)
                return np.array([day['day'].isoformat() for day in days])
        except KeyboardInterrupt:
            print('Stop query')

    async def increment_time(self, tg_id, time, table, app, category):
        try:
            if not self.pool:
                raise RuntimeError('Pool is not initialized')
            async with self.pool.acquire() as con:
                await con.execute(f'UPDATE {table} SET use_time = use_time + $1 '
                                  'WHERE tg_id = $2 AND app = $3 '
                                  'AND category = $4',
                                  time, tg_id, app, category)
        except KeyboardInterrupt:
            print('Stop query')

    async def drop_info(self):
        try:
            if not self.pool:
                raise RuntimeError('Pool is not initialized')
            async with self.pool.acquire() as con:
                await con.execute('DELETE FROM user_info')
        except KeyboardInterrupt:
            print('Stop query')

    async def on_shutdown(self):
        if hasattr(self.bot, 'pool') and self.bot.pool:
            await self.bot.pool.closed()
