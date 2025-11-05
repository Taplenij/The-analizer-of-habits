import numpy as np
import pandas as pd
import pyprind
from torch.nn.functional import embedding

from data_clf import dict_apps
from sentence_transformers import SentenceTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA

df = pd.DataFrame()
pg = pyprind.ProgBar(iterations=304)
transformer = SentenceTransformer('paraphrase-MiniLM-L12-v2')

for l in dict_apps:
    for n in dict_apps[l]:
        embeddings = transformer.encode(n)
        for e in embeddings:
            df = df._append([[l, e]], ignore_index=True)
            pg.update()

# df = pd.read_csv('apps_data.csv', encoding='utf-8')
#
# X = df['name'].values
# y = df['category'].values
#
# le = LabelEncoder()
#
#
# y = le.fit_transform(y)
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
#                                                     stratify=y, shuffle=True,
#                                                     random_state=1)
#
# param_grid = [{'randomforestclassifier__criterion': ['gini', 'entropy', 'log_loss'],
#                 'randomforestclassifier__n_estimators': [25, 50, 75, 100],
#                 'randomforestclassifier__max_depth': [2, 5, 10]}]
#
# pl_rf = make_pipeline(StandardScaler(), PCA(), RandomForestClassifier(criterion='gini',
#                                                                n_estimators=100,
#                                                                max_depth=5,
#                                                                random_state=1))
#
# print(pl_rf.get_params())
#
# # gs = GridSearchCV(estimator=pl_rf, param_grid=param_grid, refit=False, n_jobs=2)
# # gs.fit(X_train, y_train)
# # print(gs.best_params_)