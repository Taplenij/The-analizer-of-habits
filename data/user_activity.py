import pyautogui as pg
import asyncio
from stwat import StopWatch


sw = StopWatch()


# Catch the open window
async def get_win_title():
    while True:
        active_window = pg.getActiveWindow()
        return active_window.title.split(' - ')[-1] if active_window else False


async def manage_stopwatch(stop_watch: StopWatch, cur_st, next_st):
    stop_watch.FLAG = True  # Default FLAG value
    time_el = stop_watch.ELAPSED_TIME.format(0, 0, 0)  # Initialize from what date stopwatch will begin
    while stop_watch.FLAG and stop_watch.RUNNING:
        if cur_st and cur_st == next_st:  # If window is open and is use...
            print(f'\r{time_el}', end=' ')  # ...start stopwatch
            await asyncio.sleep(1)
            time_el = await stop_watch.increment()
            next_st = await get_win_title()  # Check if new window is open. If it is...
        else:
            stop_watch.FLAG = False  # ...stop stopwatch
    await stop_watch.stop()
    return


# Catch cursor position
async def time_pos():
    while True:
        pos1 = pg.position()
        await asyncio.sleep(120)
        pos2 = pg.position()
        if pos1 != pos2:
            return True


#  Start stopwatch function
async def monitor_win():
    while True:
        current_state = await get_win_title()  # Catch active window
        await asyncio.sleep(1)
        print(current_state)
        await manage_stopwatch(sw, current_state, await get_win_title())  # Start stopwatch


async def main():
    win_mon = asyncio.create_task(monitor_win())
    pos_mon = asyncio.create_task(time_pos())
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print('interrupted')
    except Exception as e:
        print(f'EXCEPTION {e}')
    finally:
        win_mon.cancel()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('leave')
