import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from data.classification.help_functions import (preprocessor, tokenizer_porter,
                                                tokenizer, stop)

df = pd.read_csv('tables/text_data.csv')

X = df['DataText'].values
y = df['Category'].values
le = LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    shuffle=True, stratify=y,
                                                    random_state=1)
tf_idf = TfidfVectorizer(strip_accents=None, lowercase=True,
                         preprocessor=preprocessor)
tree = DecisionTreeClassifier(max_depth=1, random_state=1)
rfc = RandomForestClassifier(random_state=1)
boost = AdaBoostClassifier(estimator=tree, random_state=1)
svc = SVC()
param_grid_rfc = [{'vect__ngram_range': [(1, 1)],
                   'vect__stop_words': [stop, None],
                   'vect__tokenizer': [tokenizer, tokenizer_porter],
                   'clf__n_estimators': [10, 50, 100, 500],
                   'clf__criterion': ['gini', 'entropy', 'log_loss'],
                   'clf__max_depth': [5, 10, 50],
                   },
                  {'vect__ngram_range': [(1, 1)],
                   'vect__stop_words': [stop, None],
                   'vect__tokenizer': [tokenizer, tokenizer_porter],
                   'vect__use_idf':[False],
                   'vect__norm':[None],
                   'clf__n_estimators': [10, 50, 100, 500],
                   'clf__criterion': ['gini', 'entropy', 'log_loss'],
                   'clf__max_depth': [5, 10, 50],
                   }]
param_grid_boost = [{'vect__ngram_range': [(1, 1)],
                     'vect__stop_words': [stop, None],
                     'vect__tokenizer': [tokenizer, tokenizer_porter],
                     'clf__n_estimators': [10, 50, 100, 500],
                     'clf__learning_rate': [0.1, 0.001]
                    },
                    {'vect__ngram_range': [(1, 1)],
                     'vect__stop_words': [stop, None],
                     'vect__tokenizer': [tokenizer, tokenizer_porter],
                     'vect__use_idf':[False],
                     'vect__norm':[None],
                     'clf__n_estimators': [10, 50, 100, 500],
                     'clf__learning_rate': [0.1, 0.001]
                     }]
param_grid_svc = [{'vect__ngram_range': [(1, 1)],
                   'vect__stop_words': [stop, None],
                   'vect__tokenizer': [tokenizer, tokenizer_porter],
                   'clf__kernel': ['linear', 'rbf'],
                   'clf__C': [1, 10, 100],
                   'clf__gamma': [0.1, 0.001]
                    },
                  {'vect__ngram_range': [(1, 1)],
                   'vect__stop_words': [stop, None],
                   'vect__tokenizer': [tokenizer, tokenizer_porter],
                   'vect__use_idf':[False],
                   'vect__norm':[None],
                   'clf__kernel': ['linear', 'rbf'],
                   'clf__C': [1, 10, 100],
                   'clf__gamma': [0.1, 0.001]
                   }]
pipe_rfc = Pipeline([('vect', tf_idf), ('clf', rfc)])
pipe_boost = Pipeline([('vect', tf_idf), ('clf', boost)])
pipe_svc = Pipeline([('vect', tf_idf), ('clf', svc)])
gs_rfc = GridSearchCV(pipe_rfc, param_grid_rfc, scoring='accuracy',
                      refit=True, cv=10, n_jobs=-1)
gs_boost = GridSearchCV(pipe_boost, param_grid_boost, scoring='accuracy',
                      refit=True, cv=10, n_jobs=-1)
gs_svc = GridSearchCV(pipe_svc, param_grid_svc, scoring='accuracy',
                      refit=True, cv=10, n_jobs=-1)
gs_rfc = gs_rfc.fit(X_train, y_train)
gs_boost = gs_boost.fit(X_train, y_train)
gs_svc = gs_svc.fit(X_train, y_train)
print('Random Forest: ', gs_rfc.best_score_)
print('AdaBoosting: ', gs_boost.best_score_)
print('SVC: ', gs_svc.best_score_)