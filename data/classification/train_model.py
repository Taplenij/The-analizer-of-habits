import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.pipeline import make_pipeline, Pipeline
from data.classification.help_functions import get_score_info, check_stats_for_several_models

features_columns = np.load('new_selection.npy')

df = pd.read_csv('tables/model_app_data_multi-qa-mpnet-base-cos-v1.csv')

X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values
le = LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True,
                                                    stratify=y, random_state=1)
pipe = make_pipeline(StandardScaler(), LDA(n_components=5))
X_train_lda = pipe.fit_transform(X_train, y_train)
X_test_lda = pipe.transform(X_test)

# RANDOM FOREST
rfc = RandomForestClassifier(criterion='gini', max_depth=10,
                             max_leaf_nodes=10, min_impurity_decrease=0.0001,
                             min_samples_split=5, min_samples_leaf=5,
                             n_estimators=50, random_state=1)

get_score_info(rfc, X_train_lda, y_train, X_test_lda, y_test)
# check_stats_for_several_models(rfc, 'hands')
# print('**' * 50)
# check_stats_for_several_models(rfc, 'pipeline')