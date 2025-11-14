import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline, Pipeline

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
    target_path = cur_path + 'tables'
    for table in os.listdir(target_path):
        df = pd.read_csv(table, encoding='utf-8')
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
            get_score_info(clf, X_train_lda, y_train, X_test_lda, y_test)
        elif method == 'pipeline':
            pipe = make_pipeline(StandardScaler(), LDA(n_components=5), clf)
            get_score_info(pipe, X_train, y_train, X_test, y_test)

#
# rfc = RandomForestClassifier(criterion='gini', max_depth=10,
#                              max_leaf_nodes=10, min_impurity_decrease=0.0001,
#                              min_samples_split=5, min_samples_leaf=5,
#                              n_estimators=50)
#
# pipe_lda = make_pipeline(StandardScaler(), LDA(n_components=5))
# X_train_lda = pipe_lda.fit_transform(X_train, y_train)
# X_test_lda = pipe_lda.transform(X_test)
# print('without pipeline:')
# get_score_info(rfc, X_train_lda, y_train, X_test_lda, y_test)
#
# pipe_rfc_lda = make_pipeline(StandardScaler(), LDA(n_components=5),
#                              RandomForestClassifier(criterion='gini', max_depth=10,
#                              max_leaf_nodes=10, min_impurity_decrease=0.0001,
#                              min_samples_split=5, min_samples_leaf=5,
#                              n_estimators=50))
# print('With pipeline:')
# get_score_info(pipe_rfc_lda, X_train, y_train, X_test, y_test)
# predict_category('Chivalry 2', rfc, trans)
#BAGGING
