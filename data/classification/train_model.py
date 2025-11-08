import numpy as np
import pandas as pd
import pyprind
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline

def get_score_info(clf, X_train, y_train, X_test):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    scores = cross_val_score(clf, X_train, y_train, cv=10, n_jobs=1)
    print(f'k-fold cross_val: {np.mean(scores)} +- {np.std(scores)}')
    print(f'Model train score: {clf.score(X_train, y_train)}')
    print(f'Model probability: {np.mean(clf.predict_proba(X_test))}')
    print(f'Model test accuracy: {accuracy_score(y_true=y_test, y_pred=y_pred)}')


df = pd.read_csv('model_app_data.csv', encoding='utf-8')

X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

le = LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    stratify=y, shuffle=True,
                                                    random_state=1)
pipe = make_pipeline(StandardScaler(), PCA(n_components=0.5, random_state=1))
pipe.fit(X_train)
X_train_pca = pipe.transform(X_train)
X_test_pca = pipe.transform(X_test)

# RANDOM FOREST
rfc = RandomForestClassifier(criterion='entropy', max_depth=30, n_estimators=150, random_state=1)
get_score_info(rfc, X_train_pca, y_train, X_test_pca)

# ADABOOST
# tree = DecisionTreeClassifier(criterion='gini', max_depth=15, max_features=5, random_state=1)
# tree.fit(X_train_pca, y_train)
# ada = AdaBoostClassifier(learning_rate=0.1, n_estimators=2000, random_state=1)
#
# get_score_info(ada, X_train_pca, y_train, X_test_pca)
