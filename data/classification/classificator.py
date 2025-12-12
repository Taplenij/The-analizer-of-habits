import joblib
import aiohttp
import asyncio
from data.classification.help_functions import preproc
from concurrent.futures import ProcessPoolExecutor

def classify(clf, vect):
    return clf.predict(vect)[0]

class AppNameClassifier:
    _CLF = joblib.load('trained_model.z')
    _TRF = joblib.load('transformer.z')
    _HEADERS = {
        'User-Agent': 'Analizer_of_habits/1.0 '
                      '(https://github.com/Taplenij/The-analizer-of-habits.git)'
    }
    _VECT_LIST = []

    async def get_vector(self, app_list):
        async with aiohttp.ClientSession(headers=self._HEADERS) as session:
            for name in app_list:
                async with session.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{preproc(name)}') as r:
                    if r.status != 200:
                        continue

                    text = await r.json()
                    data = text.get('extract', '')

                    if len(data) < 50:
                        continue

                    vect = self._TRF.transform(data)
                    self._VECT_LIST.append(vect)

    async def get_category(self):
        loop = asyncio.get_running_loop()
        async with ProcessPoolExecutor(max_workers=4) as pool:
            task = [loop.run_in_executor(pool, classify, self._CLF, vect)
                    for vect in self._VECT_LIST]
            return asyncio.gather(*task)