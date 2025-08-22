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

