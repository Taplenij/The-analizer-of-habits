import numpy as np
import pandas as pd
import xgboost as xg
import pyprind
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('model_app_data.csv', encoding='utf-8')

X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

le = LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    stratify=y, shuffle=True,
                                                    random_state=1)

scl = StandardScaler()
X_train_std = scl.fit_transform(X_train)
X_test_std = scl.transform(X_test)

pca = PCA(n_components=0.5, random_state=1)
X_train_pca = pca.fit_transform(X_train_std)
X_test_pca = pca.transform(X_test_std)

# dtrain = xg.DMatrix(X_train_pca, label=y_train)
# dtest = xg.DMatrix(X_test_pca, label=y_test)
#
# params = {
#     'max_depth': 3,
#     'eta': 0.1,
#     'objective': 'multi:softprob',
#     'num_class': 3
# }
#
# bst = xg.train(params, dtrain, num_boost_round=500)
# preds = bst.predict(dtest)
# predictions = np.asarray([np.argmax(line) for line in preds])
# RANDOM FOREST
# pipe_rfc = Pipeline([('scl', StandardScaler()),
#                      ('pca', PCA()),
#                      ('clf', RandomForestClassifier())
#                     ])
#
# param_grid = [{'clf__criterion': ['gini', 'entropy', 'log_loss'],
#                 'clf__n_estimators': [25, 50, 75, 100, 125, 150],
#                 'clf__max_depth': [2, 5, 10, 15, 20, 30],
#                 'pca__n_components': [0.5, 1, 2, 5, 7, 10, 20]}]
#
#
#
# gs = GridSearchCV(estimator=pipe_rfc, param_grid=param_grid, refit=True, n_jobs=2)

# ADABOOST
pipe_tree = Pipeline([('scl', StandardScaler()),
                      ('pca', PCA()),
                      ('clf', DecisionTreeClassifier())])
param_grid = [{'pca__n_components': [0.5, 1, 2, 5, 10],
               'clf__criterion': ['gini', 'entropy', 'log_loss'],
               'clf__max_depth': [2, 5, 10, 15, 20, 30],
               'clf__max_features': [1, 5, 10, 20, 30, 40, 50]}]
gs = GridSearchCV(estimator=pipe_tree, param_grid=param_grid, refit=True, n_jobs=-1)
gs.fit(X_train_pca, y_train)
best_tree = gs.best_estimator_.named_steps['clf']
ada = AdaBoostClassifier(estimator=best_tree, n_estimators=500,
                         learning_rate=0.1, random_state=1)
ada.fit(X_train_pca, y_train)
y_pred = ada.predict(X_test_pca)
scores = cross_val_score(ada, X_test_pca, y_test, cv=10, n_jobs=1)
print(f'The best parameters: {gs.best_params_}')
# print(f'The best score with k-fold-cross-validation: {gs.best_score}')
print(f'Score with train data: {ada.score(X_train_pca, y_train)}')
print(f'Score with test data: {ada.score(X_test_pca, y_test)}')
print(f'Accuracy: {accuracy_score(y_true=y_test, y_pred=y_pred)}')
print(f'K-fold cross-validation {np.mean(scores)} +- {np.std(scores)}')