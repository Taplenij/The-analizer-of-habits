import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

df = pd.read_csv('model_app_data.csv', encoding='utf-8')

X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    stratify=y, shuffle=True,
                                                    random_state=1)

pipe_lda = make_pipeline(StandardScaler(), LDA(n_components=2))
X_train_lda = pipe_lda.fit_transform(X_train, y_train)
X_test_lda = pipe_lda.transform(X_test)

X_lda = pipe_lda.transform(X)


colors = ['red', 'blue', 'green', 'gray', 'black', 'cyan']
markers = ['o', '^', 's', 'x', 'v', '*']
def draw(X, y, colors, markers):
    for idx, cls in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cls, 0], y=X[y == cls, 1],
                    alpha=0.8, c=colors[idx],
                    marker=markers[idx], label=cls)

    plt.tight_layout()
    plt.show()
draw(X_train_lda, y_train, colors, markers)
draw(X, y, colors, markers)