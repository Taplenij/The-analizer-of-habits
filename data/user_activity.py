import pyautogui as pg
import asyncio
from datetime import datetime


# Catch the open window
async def get_win_title():
    while True:
        active_window = pg.getActiveWindow().title
        if active_window:
            print(active_window)
        else:
            print('None')
        await asyncio.sleep(1)


async def time_pos():
    while True:
        pos1 = pg.position()
        await asyncio.sleep(120)
        pos2 = pg.position()
        return True if pos1 == pos2 else False


# async def timer():


async def main():
    task = asyncio.create_task(get_win_title())
    task2 = asyncio.create_task(time_pos())
    while True:
        await asyncio.sleep(1)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('leave')
