import pyautogui as pg
import asyncio


# Catch the open window
async def get_win_title():
    while True:
        active_window = pg.getActiveWindow().title
        if active_window:
            print(active_window)
        else:
            print('None')
        await asyncio.sleep(1)


async def main():
    task = asyncio.create_task(get_win_title())
    while True:
        await asyncio.sleep(1)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('leave')
