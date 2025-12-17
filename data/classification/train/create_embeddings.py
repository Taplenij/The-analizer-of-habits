import pandas as pd
import pyprind
from sentence_transformers import SentenceTransformer
from data.classification.train.data_clf import dict_apps

models = ['paraphrase-MiniLM-L12-v2', 'distiluse-base-multilingual-cased',
          'multi-qa-mpnet-base-cos-v1', 'multi-qa-distilbert-cos-v1',
          'multi-qa-MiniLM-L6-cos-v1', 'msmarco-distilbert-cos-v5',
          'msmarco-MiniLM-L12-cos-v5', 'msmarco-MiniLM-L12-cos-v5']
embd = []
for model in models:
    print(f'Start create table {model}')
    pg = pyprind.ProgBar(iterations=304)
    df = pd.DataFrame()
    transformer = SentenceTransformer(model)
    for l in dict_apps:
        for n in dict_apps[l]:
            embeddings = transformer.encode(n)
            df = df._append([[l, *embeddings]], ignore_index=True)
            pg.update()
    df.columns = ['category', *[f'values{i}' for i in range(1, embeddings.shape[0] + 1)]]
    df.to_csv(f'model_app_data_{model}.csv', index=False, encoding='utf-8')
    print(f'{model} table was ended')
