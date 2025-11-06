import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pyprind
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, classification_report

def analyzer_err(X_test, y_test, clf):
    y_pred = clf.predict(X_test)
    c_mat = confusion_matrix(y_true=y_test, y_pred=y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(c_mat, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.show()

    print(f'Detail report: {classification_report(y_test, y_pred)}')

    errors = X_test[y_pred != y_test]
    errors_pairs = list(zip(y_test[y_pred != y_test], y_pred[y_pred != y_test]))
    errors_count = pd.Series(errors_pairs).value_counts()
    print(f'Most frequency errors: {errors_count.head(10)}')

df = pd.read_csv('model_app_data.csv', encoding='utf-8')

X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

le = LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    stratify=y, shuffle=True,
                                                    random_state=1)

pipe_rfc = Pipeline([
                     ('pca', PCA()),
                     ('clf', RandomForestClassifier())
                    ])

param_grid = [{'clf__criterion': ['gini', 'entropy', 'log_loss'],
                'clf__n_estimators': [25, 50, 75, 100, 125, 150],
                'clf__max_depth': [2, 5, 10, 15, 20, 30],
                'pca__n_components': [0.5, 1, 2, 5, 7, 10, 20]}]


gs = GridSearchCV(estimator=pipe_rfc, param_grid=param_grid, refit=True, n_jobs=2)
gs.fit(X_train, y_train)
print(f'The best parameters: {gs.best_params_}')
print(f'The best score with k-fold-cross-validation: {gs.best_score_}')
# analyzer_err(X_test, y_test, pipe_rfc)
