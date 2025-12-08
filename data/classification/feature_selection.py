import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('tables/model_app_data_multi-qa-mpnet-base-cos-v1.csv')
X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values
le = LabelEncoder()
y = le.fit_transform(y)
scl = StandardScaler()
X_std = scl.fit_transform(X)

rfc = RandomForestClassifier(criterion='gini', max_depth=10,
                             max_leaf_nodes=10, min_impurity_decrease=0.0001,
                             min_samples_split=5, min_samples_leaf=5,
                             n_estimators=50)
# rfc.fit(X, y)
# importance_feat = np.array([])
# feat_labels = df.columns[1:]
# importances = rfc.feature_importances_
# indices = np.argsort(importances)[::-1]
# for f in range(X.shape[1]):
#     if importances[f] != 0.0:
#         importance_feat = np.append(importance_feat, feat_labels[f])
# print(importance_feat)
# print(importance_feat.shape)
# np.save('new_selection', importance_feat)
