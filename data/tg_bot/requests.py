import asyncpg as pg
from aiogram import Bot
from config import TOKEN
import numpy as np
from data.classification.help_functions import week_days
from data.classification.train.data_clf import categories


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

    async def get_info(self, tg_id, table, day=None):
        try:
            if not self.pool:
                raise RuntimeError('Pool is not initialized')
            async with self.pool.acquire() as con:
                if table == 'user_info':
                    info = np.array([[rec['app'], rec['use_time'].seconds] for rec in
                            (await con.fetch(f'SELECT app, use_time FROM user_info '
                                             'WHERE tg_id = $1', tg_id))])
                    return info
                elif table == 'total_info':
                    times = []
                    days_s, days_d = week_days(day)
                    for d in days_d:
                        val = await con.fetchval('SELECT SUM(use_time) FROM total_info '
                                                  'WHERE day = $1 AND tg_id = $2',
                                                 d, tg_id)
                        times.append(int(val.seconds))
                    return times
        except KeyboardInterrupt:
            print('Stop query')

    async def get_time_catgrs(self, tg_id, table):
        try:
            if not self.pool:
                raise RuntimeError('Pool is not initialized')
            async with self.pool.acquire() as con:
                times = []
                for c in categories:
                    val = await con.fetchval(f'SELECT SUM(use_time) FROM {table} '
                                             'WHERE category = $1 AND tg_id = $2',
                                             c, tg_id)
                    times.append(int(val.seconds))
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
                days = np.array([d['day'] for d in
                                 (await con.fetch(f'SELECT day FROM total_info WHERE tg_id = $1',
                                                  tg_id))])
                return np.unique(days)
        except KeyboardInterrupt:
            print('Stop query')

    async def increment_time(self, tg_id, time, table, app, category, day=None):
        try:
            if not self.pool:
                raise RuntimeError('Pool is not initialized')
            async with self.pool.acquire() as con:
                if table == 'user_info':
                    await con.execute('UPDATE user_info SET use_time = use_time + $1 '
                                      'WHERE tg_id = $2 AND app = $3 '
                                      'AND category = $4',
                                      time, tg_id, app, category)
                elif table == 'total_info':
                    await con.execute('UPDATE total_info SET use_time = use_time + $1 '
                                      'WHERE tg_id = $2 AND app = $3 '
                                      'AND category = $4 AND day = $5',
                                      time, tg_id, app, category, day)

        except KeyboardInterrupt:
            print('Stop query')

    async def drop_info(self, table):
        try:
            if not self.pool:
                raise RuntimeError('Pool is not initialized')
            async with self.pool.acquire() as con:
                await con.execute(f'DELETE FROM {table}')
        except KeyboardInterrupt:
            print('Stop query')

    async def on_shutdown(self):
        if hasattr(self.bot, 'pool') and self.bot.pool:
            await self.bot.pool.closed()
