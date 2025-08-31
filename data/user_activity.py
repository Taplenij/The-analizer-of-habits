import pyautogui as pg
import asyncio
from stwat import StopWatch
from datetime import time
from queue import Queue


class UserActivity:
    _STOPWATCH = StopWatch()
    _STOPWATCH.FLAG = True
    _STOPWATCH.RUNNING = True
    _NEXT_STATE = None
    _CURRENT_STATE = None
    _ELAPSED_TIME = None
    _MOUSE_STATE = True
    _FIFOQ: Queue[time] = Queue()

    @staticmethod
    async def _get_title():
        active_window = pg.getActiveWindow()
        return active_window.title.split(' - ')[-1] if active_window else False

    async def _mouse_pos(self):
        while True:
            pos1 = pg.position()
            await asyncio.sleep(5)
            pos2 = pg.position()
            self._MOUSE_STATE = pos1 != pos2

    async def _state_stopwatch(self):
        if (self._STOPWATCH.FLAG
                and self._STOPWATCH.RUNNING):
            return True
        return False

    async def _state_machine(self):
        if (self._CURRENT_STATE
                and self._CURRENT_STATE == self._NEXT_STATE
                and self._MOUSE_STATE):
            return True
        return False

    async def _manage_stopwatch(self):
        mouse_task = asyncio.create_task(self._mouse_pos())
        self._ELAPSED_TIME = self._STOPWATCH.ELAPSED_TIME.format(0, 0, 0)
        self._STOPWATCH.FLAG = True
        self._MOUSE_STATE = True
        try:
            while await self._state_stopwatch():
                if await self._state_machine():
                    print(f'\r{self._ELAPSED_TIME}', end=' ')
                    self._ELAPSED_TIME = await self._STOPWATCH.increment()
                    self._NEXT_STATE = await self._get_title()
                else:
                    cur_t = time(**await self._STOPWATCH.grab_current_time())
                    self._FIFOQ.put(cur_t, block=False)
                    self._STOPWATCH.FLAG = False
                    await self._STOPWATCH.stop()
                await asyncio.sleep(1)
        finally:
            mouse_task.cancel()
            while not self._FIFOQ.empty():
                return self._FIFOQ.get(block=False)

    async def monitor_window(self):
        while True:
            self._CURRENT_STATE = await self._get_title()
            self._NEXT_STATE = await self._get_title()
            print(self._CURRENT_STATE)
            return await self._manage_stopwatch()


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
