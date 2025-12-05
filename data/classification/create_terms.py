from data.classification.data_clf import dict_apps
from data.classification.help_functions import preproc
import requests
import pandas as pd
import pyprind

df = pd.DataFrame()

user_agent = 'Analizer_of_habits/1.0 (https://github.com/Taplenij/The-analizer-of-habits.git)'

headers = {
    'User-Agent' : user_agent
}
pgb = pyprind.ProgBar(iterations=304)
for l in dict_apps:
    for name in dict_apps[l]:
        r = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{preproc(name)}',
                         headers=headers)
        print('define text')
        text = r.json()
        print(text['extract'])
        df = df._append([[l, text['extract']]], ignore_index=True)
        pgb.update()
df.columns = ['AppName', 'DataText']
df.to_csv('text_data.csv', index=False, encoding='utf-8')
print('END')
