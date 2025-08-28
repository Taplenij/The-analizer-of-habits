from datetime import timedelta


class StopWatch:
    RUNNING = True
    FLAG = False
    ONE_SEC = timedelta(seconds=1)
    ELAPSED_TIME = 'time_elapsed: {:.0f}h {:>2.0f}m {:>2.0f}s'
    START_TIME = dict(hours=0, minutes=0, seconds=1)
    START_STATE = _CURRENT_STATE = timedelta(**START_TIME)

    async def stop(self):
        self._CURRENT_STATE = self.START_STATE
        print('Stop')

    async def forced_stop(self):
        self.RUNNING = False

    async def increment(self):
        self._CURRENT_STATE += self.ONE_SEC
        hours = self._CURRENT_STATE.seconds // 3600
        minutes = self._CURRENT_STATE.seconds // 60
        seconds = self._CURRENT_STATE.seconds % 60
        return self.ELAPSED_TIME.format(hours, minutes, seconds)
