import asyncpg as pg


class DBC:
    def __init__(self):
        self.pool = None

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
        return self.pool

    async def rec_activity(self, time, app, tg_id):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        async with self.pool.acquire as con:
            await con.execute('INSERT INTO user_info(using_time)'
                              ' VALUE($1, $2) WHERE tg_id = VALUE($3)', time, tg_id)
            await con.execute('UPDATE TABLE user_info SET app = $1'
                              ' WHERE (tg_id = $2, time = $3', app, tg_id, time)

    async def rec_tg_id(self, tg_id):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        async with self.pool.acquire as con:
            try:
                await con.execute('INSERT INTO user_info(tg_id) VALUE($1)', tg_id)
            except pg.exceptions.UniqueViolationError:
                print('This id already exists in database')

    async def rec_app(self, app):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        async with self.pool.acquire as con:
            try:
                await con.execute('INSERT INTO app_list(app_name) VALUE $1', app)
            except pg.exceptions.UniqueViolationError:
                print('This app is already in database')

    async def remove_all(self):
        if not self.pool:
            raise RuntimeError('Pool is not initialized')
        async with self.pool.acquire as con:
            await con.execute('DELETE FROM user_info')
