import pandas as pd
import pyprind
from sentence_transformers import SentenceTransformer
from data.classification.data_clf import dict_apps

models = ['paraphrase-MiniLM-L12-v2', 'distiluse-base-multilingual-cased']
embd = []
df = pd.DataFrame()
pg = pyprind.ProgBar(iterations=304)
for model in models:
    transformer = SentenceTransformer(model)
    for l in dict_apps:
        for n in dict_apps[l]:
            embeddings = transformer.encode(n)
            df = df._append([[l, *embeddings]], ignore_index=True)
            pg.update()

df.columns = ['category', *[f'values{i}' for i in range(1, 385)]]

df.to_csv('model_app_data.csv', index=False, encoding='utf-8')
