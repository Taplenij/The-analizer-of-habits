import joblib
import logging
import aiohttp
import asyncio
from data.classification.help_functions import preproc
from concurrent.futures import ProcessPoolExecutor

log = logging.getLogger('classificator')
log.setLevel(logging.DEBUG)
sh = logging.StreamHandler()

formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

sh.setFormatter(formatter)
log.addHandler(sh)

def classify(clf, vect):
    le = joblib.load('lblencdr.z')
    return le.inverse_transform(clf.predict(vect)[0])

class AppNameClassifier:
    _CLF = joblib.load('trained_model.z')
    _TRF = joblib.load('transformer.z')
    _HEADERS = {
        'User-Agent': 'Analizer_of_habits/1.0 '
                      '(https://github.com/Taplenij/The-analizer-of-habits.git)'
    }
    _VECT_LIST = []

    async def vectorize(self, app):
        async with aiohttp.ClientSession(headers=self._HEADERS) as session:
            async with session.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{preproc(app)}') as r:
                if r.status != 200:
                    log.info('Error occured with getting info about app')
                else:
                    text = await r.json()
                    data = text.get('extract', '')

                    if len(data) < 50:
                        pass
                    else:
                        vect = self._TRF.transform(data)
                        self._VECT_LIST.append(vect)

    async def get_category(self):
        loop = asyncio.get_running_loop()
        async with ProcessPoolExecutor(max_workers=4) as pool:
            task = [loop.run_in_executor(pool, classify, self._CLF, vect)
                    for vect in self._VECT_LIST]
            return asyncio.gather(*task)