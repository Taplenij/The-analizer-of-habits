import asyncio
import win32gui
import win32process
import psutil
import pyautogui as pg
import os
from data.stwat import StopWatch
from datetime import time
from queue import Queue
import logging
import data.computer_vision as cv
from data.tg_bot.requests import DBC

log = logging.getLogger('user_activity')
log.setLevel(logging.DEBUG )
sh = logging.StreamHandler()

formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

sh.setFormatter(formatter)
log.addHandler(sh)

COMV = cv.ComputerVision()
req = DBC()

class UserActivity:
    def __init__(self, tg_id):
        self.tg_id = tg_id
        self._STOPWATCH = StopWatch()
        self._STOPWATCH.FLAG = True
        self._STOPWATCH.RUNNING = True
        self._NEXT_STATE = None # New opened window in browser
        self._CURRENT_STATE = None # Current opened window
        self._ELAPSED_TIME = None
        self._MOUSE_STATE = True
        self._FIFOQ: Queue[time] = Queue()
        self._BROWSERS = ['opera', 'chrome', 'safari', 'msedge', 'firefox']

    @staticmethod
    async def _get_title(): # This function gets window title
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        actname = process.name()
        return os.path.splitext(actname)[0] if actname else False

    async def _check_soc(self):
        name_title = await self._get_title()
        if name_title in self._BROWSERS: # If it's browser...
            await COMV.active_win_info() # ...we check what link was opened
            return COMV.TEXT
        else:
            return name_title # If it's not a browser, return founded title

    async def _mouse_pos(self): # Checking if user is active
        while True:
            pos1 = pg.position()
            await asyncio.sleep(5)
            pos2 = pg.position()
            self._MOUSE_STATE = pos1 != pos2

    async def _state_stopwatch(self): # Checking if stopwatch works
        if (self._STOPWATCH.FLAG
                and self._STOPWATCH.RUNNING):
            return True
        return False

    async def _state_machine(self): # Checking the reason to drop
                                    # the self._ELAPSED_TIME
        if (self._CURRENT_STATE
                and self._CURRENT_STATE == self._NEXT_STATE
                and self._MOUSE_STATE):
            return True
        return False

    async def _manage_stopwatch(self):
        mouse_task = asyncio.create_task(self._mouse_pos()) # Create task to
                                                            # work asynchronously
        self._ELAPSED_TIME = self._STOPWATCH.ELAPSED_TIME.format(0, 0, 0)
        self._STOPWATCH.FLAG = True
        self._MOUSE_STATE = True
        try:
            while await self._state_stopwatch(): # While stopwatch working...
                if await self._state_machine(): # ...and if app hasn't been changed
                    print(f'\r{self._ELAPSED_TIME}', end=' ')
                    self._ELAPSED_TIME = await self._STOPWATCH.increment()
                    self._NEXT_STATE = await self._check_soc()
                else:
                    # When app has been changed drops the elapsed time and gets one
                    cur_t = time(**await self._STOPWATCH.grab_current_time())
                    self._FIFOQ.put(cur_t, block=False) # Saves it in FIFO queue...
                    self._STOPWATCH.FLAG = False # ...and drops the stopwatch
                    await self._STOPWATCH.stop()
                await asyncio.sleep(1)
        finally:
            mouse_task.cancel()
            while not self._FIFOQ.empty():
                await req.create_pool()
                await req.increment_time(tg_id=self.tg_id,
                                         time=self._FIFOQ.get(block=False),
                                         table='user_info')
                await req.increment_time(tg_id=self.tg_id,
                                         time=self._FIFOQ.get(block=False),
                                         table='total_info')
                log.info(self._FIFOQ.get(block=False))

    # This function starts the program
    async def monitor_window(self):
        while True:
            try:
                start_title = await self._check_soc()
                self._CURRENT_STATE = start_title
                self._NEXT_STATE = start_title
                await req.create_pool()
                await req.record_activity(tg_id=self.tg_id,
                                          app=self._CURRENT_STATE,
                                          time=time(hour=0, minute=0, second=0),
                                          table='user_info')
                await req.record_activity(tg_id=self.tg_id,
                                          app=self._CURRENT_STATE,
                                          time=time(hour=0, minute=0, second=0),
                                          table='total_info')
                log.info(self._CURRENT_STATE)
                await self._manage_stopwatch()
            except Exception as e:
                log.error(e)
