import pyautogui as pg
import asyncio
from stwat import StopWatch


class UserActivity:
    def __init__(self):
        self._stopwatch = StopWatch()
        self._stopwatch.FLAG = True
        self._stopwatch.RUNNING = True
        self._INFO = dict()
        self._next_state = None
        self._current_state = None
        self._elapsed_time = None
        self._mouse_state = True

    @staticmethod
    async def _get_title():
        active_window = pg.getActiveWindow()
        return active_window.title.split(' - ')[-1] if active_window else False

    async def _mouse_pos(self):
        while True:
            pos1 = pg.position()
            await asyncio.sleep(5)
            pos2 = pg.position()
            self._mouse_state = pos1 != pos2

    async def _state_stopwatch(self):
        if (self._stopwatch.FLAG
                and self._stopwatch.RUNNING):
            return True
        return False

    async def _state_machine(self):
        if (self._current_state
                and self._current_state == self._next_state
                and self._mouse_state):
            return True
        return False

    async def _manage_stopwatch(self):
        mouse_task = asyncio.create_task(self._mouse_pos())
        self._elapsed_time = self._stopwatch.ELAPSED_TIME.format(0, 0, 1)
        self._stopwatch.FLAG = True
        self._mouse_state = True
        try:
            while await self._state_stopwatch():
                if await self._state_machine():
                    print(f'\r{self._elapsed_time}', end=' ')
                    self._elapsed_time = await self._stopwatch.increment()
                    self._next_state = await self._get_title()
                else:
                    self._stopwatch.FLAG = False
                    await self._stopwatch.stop()
                await asyncio.sleep(1)
        finally:
            mouse_task.cancel()

    async def monitor_window(self):
        while True:
            self._current_state = await self._get_title()
            self._next_state = await self._get_title()
            print(self._current_state)
            await self._manage_stopwatch()


async def main():
    user_activity = UserActivity()
    monitor_window = asyncio.create_task(user_activity.monitor_window())
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        monitor_window.cancel()
        print('interrupted')
    except Exception as e:
        print(f'EXCEPTION {e}')
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('leave')
