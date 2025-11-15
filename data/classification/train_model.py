import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('tables/model_app_data_multi-qa-mpnet-base-cos-v1.csv')
X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values
le = LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y,
                                                    shuffle=True, random_state=1)

def get_score_info(clf, X_train, y_train, X_test, y_test):
    cv_score = cross_val_score(clf, X_train, y_train, cv=10, n_jobs=1)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    if hasattr(clf, 'predict_proba'):
        pred_prob = clf.predict_proba(X_test)
        mean_proba = np.mean(pred_prob)
    else:
        mean_proba = None

    print('K-fold cross-val: %.3f +- %.3f' % (np.mean(cv_score), np.std(cv_score)))
    print('Train score: %.3f' % clf.score(X_train, y_train))
    if not mean_proba:
        print('Model do not support attribute predict_proba')
    else:
        print('Predict probability: %.3f' % mean_proba)
    print('Test accuracy: %.3f' % accuracy_score(y_test, y_pred))

def check_stats_for_several_models(clf, method):
    cur_path = os.getcwd()
    for table in os.listdir(os.path.join(cur_path, 'tables')):
        df = pd.read_csv(os.path.join('tables', table), encoding='utf-8')
        X = df.iloc[:, 1:].values
        y = df.iloc[:, 0].values
        le = LabelEncoder()
        y = le.fit_transform(y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                            stratify=y, shuffle=True,
                                                            random_state=1)
        if method == 'hands':
            pipe = make_pipeline(StandardScaler(), LDA(n_components=5))
            X_train_lda = pipe.fit_transform(X_train, y_train)
            X_test_lda = pipe.transform(X_test)
            print(f'Score info with {table}')
            get_score_info(clf, X_train_lda, y_train, X_test_lda, y_test)
            print('--' * 50)
        elif not isinstance(clf, Pipeline) and method == 'pipeline':
            pipe = make_pipeline(StandardScaler(), LDA(n_components=5), clf)
            print(f'Score info with {table}')
            get_score_info(pipe, X_train, y_train, X_test, y_test)
            print('--' * 50)
        else:
            raise ValueError('Method parameter must be hand or pipeline')
# RANDOM FOREST
# rfc = RandomForestClassifier(criterion='gini', max_depth=10,
#                              max_leaf_nodes=10, min_impurity_decrease=0.0001,
#                              min_samples_split=5, min_samples_leaf=5,
#                              n_estimators=50)
# check_stats_for_several_models(rfc, 'hands')
# print('**' * 50)
# check_stats_for_several_models(rfc, 'pipeline')

#BAGGING
tree = DecisionTreeClassifier(criterion='entropy', max_depth=10, random_state=1)
bag = BaggingClassifier(estimator=tree, max_features=1.0, max_samples=1.0,
                        bootstrap=True, bootstrap_features=False, n_jobs=1)
check_stats_for_several_models(bag, 'hands')
print('**' * 50)
check_stats_for_several_models(bag, 'pipeline')

