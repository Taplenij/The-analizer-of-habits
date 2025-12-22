import joblib
import logging
import aiohttp
import asyncio
from data.classification.help_functions import preproc_2
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

log = logging.getLogger('classificator')
log.setLevel(logging.DEBUG)
sh = logging.StreamHandler()

formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

sh.setFormatter(formatter)
log.addHandler(sh)

BASE_DIR = Path(__file__).parent

CLF_PATH = BASE_DIR / 'trained_model.z'
TRF_PATH = BASE_DIR / 'transformer.z'

def classify(clf, vect):
    labels = {0: 'Education', 1: 'Entertainments',
              2: 'Games', 3: 'Other',
              4: 'System', 5: 'Work'}
    return labels[clf.predict(vect)[0]]

class AppNameClassifier:
    _CLF = joblib.load(CLF_PATH)
    _TRF = joblib.load(TRF_PATH)
    _HEADERS = {
        'User-Agent': 'Analizer_of_habits/1.0 '
                      '(https://github.com/Taplenij/The-analizer-of-habits.git)'
    }
    _VECT = None
    _FLAG = True

    async def vectorize(self, app):
        async with aiohttp.ClientSession(headers=self._HEADERS) as session:
            async with session.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{preproc_2(app)}') as r:
                if r.status != 200:
                    log.error('Error occured with getting info about app')
                    self._FLAG = False
                else:
                    text = await r.json()
                    data = text.get('extract', '')

                    if len(data) < 40:
                        log.error('Info text is too small')
                        self._FLAG = False
                    else:
                        self._VECT = self._TRF.transform([data])

    async def get_category(self):
        loop = asyncio.get_running_loop()
        with ProcessPoolExecutor(max_workers=4) as pool:
            if not self._FLAG:
                return None
            if isinstance(self._VECT, list):
                tasks = [loop.run_in_executor(pool, classify, self._CLF, v) for v in self._VECT]
                result = await asyncio.gather(*tasks)
                return result
            result = await loop.run_in_executor(pool, classify, self._CLF, self._VECT)
            return result