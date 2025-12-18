import os
import joblib
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from data.classification.help_functions import preprocessor, tokenizer_porter

BASE_DIR = Path(__file__).parent
cur_d = os.getcwd()
stp = BASE_DIR / 'stop.z'
stop = joblib.load(stp)

df = pd.read_csv('D:/PyCharm 2025.2.4/PycharmProjects/The-analizer-of-habits/data/classification/tables/text_data.csv')

X = df['DataText'].values

vect = TfidfVectorizer(strip_accents=None, lowercase=True, preprocessor=preprocessor,
                        ngram_range=(1, 1), stop_words=None, tokenizer=tokenizer_porter)
vect = vect.fit(X)