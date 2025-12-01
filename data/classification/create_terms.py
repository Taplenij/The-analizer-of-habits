import pandas as pd
import numpy as np
import pyprind
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('clear_data.csv')

X = df['app_name'].values
y = df['category'].values
le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                    shuffle=True, random_state=1)

tfidf = TfidfVectorizer(strip_accents=None,
                        lowercase=False,
                        preprocessor=None)

param_grid = [{
    'vect__ngram_range': [(1, 1)],
    'vect__use_idf': [True, False],
    'vect__norm': [None, 'l2'],
    'clf__criterion': ['log_loss', 'entropy', 'gini'],
    'clf__max_leaf_nodes': [5, 10, 15, 20],
    'clf__max_depth': [5, 10, 15, 20, 25],
    'clf__min_impurity_decrease': [0.0001, 0.001],
    'clf__min_samples_leaf': [5, 10, 15, 20],
    'clf__min_samples_split': [5, 10, 15, 20],
    'clf__n_estimators': [10, 50, 100, 200]
}]

tree = RandomForestClassifier()
pipe_tfidf = Pipeline([('vect', tfidf), ('clf', tree)])
gs = GridSearchCV(pipe_tfidf, param_grid=param_grid, refit=True,
                  scoring='accuracy', cv=10, n_jobs=-1)
gs.fit(X_train, y_train)
print(gs.best_params_)
print(gs.best_score_)