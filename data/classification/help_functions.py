import numpy as np
import os
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

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