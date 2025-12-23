from data.classification.train.data_clf import dict_apps, addit_data
from data.help_functions import preproc
import requests
import pandas as pd
import pyprind

df = pd.DataFrame()
user_agent = 'Analizer_of_habits/1.0 (https://github.com/Taplenij/The-analizer-of-habits.git)'
headers = {
    'User-Agent' : user_agent
}
pgb = pyprind.ProgBar(iterations=603)
for l in dict_apps:
    for name in dict_apps[l]:
        r = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{preproc(name)}',
                         headers=headers)
        if r.status_code != 200:
            new_row_df = pd.DataFrame([{'Category': l,
                                    'AppName': name,
                                    'DataText': addit_data[name]}])
        else:
            text = r.json()
            if len(text.get('extract', '')) < 50:
                new_row_df = pd.DataFrame([{'Category': l,
                                        'AppName': name,
                                        'DataText': addit_data[name]}])
            else:
                new_row_df = pd.DataFrame([{'Category': l,
                                            'AppName': name,
                                            'DataText': text.get('extract', '')}])
        df = pd.concat([df, new_row_df], ignore_index=True)
        pgb.update()
df.columns = ['Category', 'AppName', 'DataText']
df.to_csv('text_data.csv', index=False, encoding='utf-8')
print('\nEND')