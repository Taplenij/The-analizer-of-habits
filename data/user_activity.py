import pyautogui as pg
import asyncio
from stwat import StopWatch


sw = StopWatch()


# Catch the open window
async def get_win_title():
    active_window = pg.getActiveWindow()
    return active_window.title.split(' - ')[-1] if active_window else False


async def manage_stopwatch(stop_watch: StopWatch, cur_st, next_st):
    stop_watch.FLAG = True  # Default FLAG value
    time_el = stop_watch.ELAPSED_TIME.format(0, 0, 0)  # Initialize from what date stopwatch will begin
    mouse_state = True

    async def mouse_pos():
        nonlocal mouse_state
        while True:
            pos1 = pg.position()
            await asyncio.sleep(5)
            pos2 = pg.position()
            mouse_state = pos1 != pos2

    mouse_task = asyncio.create_task(mouse_pos())  # Start mouse_pos function
    try:                                            # on background
        while stop_watch.FLAG and stop_watch.RUNNING:
            if cur_st and cur_st == next_st and mouse_state:  # If window is open
                # and is use...
                print(f'\r{time_el}', end=' ')  # ...start stopwatch
                time_el = await stop_watch.increment()
                next_st = await get_win_title()  # Check if new window is open.
            else:                                  # If it is...
                stop_watch.FLAG = False  # ...stop stopwatch
                await sw.stop()
            await asyncio.sleep(1)
    finally:
        mouse_task.cancel()


# Catch cursor position
async def mouse_pos():
    pos1 = pg.position()
    await asyncio.sleep(5)
    pos2 = pg.position()
    return pos1 != pos2


# Start stopwatch function
async def monitor_win():
    while True:
        current_state = await get_win_title()  # Catch active window
        print(current_state)
        await manage_stopwatch(sw, current_state, current_state)  # Start stopwatch


async def main():
    win_mon = asyncio.create_task(monitor_win())
    try:
        while True:
            await win_mon
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print('interrupted')
    except Exception as e:
        print(f'EXCEPTION {e}')
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('leave')
