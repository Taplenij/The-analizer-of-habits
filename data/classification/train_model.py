import joblib
import pandas as pd
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import make_pipeline, Pipeline
from data.classification.help_functions import (get_score_info, check_stats_for_several_models,
                                                preprocessor, tokenizer, tokenizer_porter)

df = pd.read_csv('tables/text_data.csv')

X = df['DataText'].values
y = df['Category'].values
le = LabelEncoder()
le = le.fit(y)
y = le.transform(y)
joblib.dump(le, 'lblencdr' + '.z')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    shuffle=True, stratify=y,
                                                    random_state=1)

clf = SVC(random_state=1, kernel='linear', C=1.0, gamma=0.1)
tfidf = TfidfVectorizer(strip_accents=None, lowercase=True, preprocessor=preprocessor,
                        ngram_range=(1, 1), stop_words=None, tokenizer=tokenizer_porter)

X_train_v = tfidf.fit_transform(X_train)
X_test_v = tfidf.transform(X_test)
clf_v = clf.fit(X_train_v, y_train)

joblib.dump(clf_v, 'trained_model' + '.z')
joblib.dump(tfidf, 'transformer' + '.z')
