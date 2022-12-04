# Self-Harm Detection

import matplotlib
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Import data

DATA_FILE_PATH = r'C:\Users\860281\Downloads\Suicide_Detection.csv'

data = pd.read_csv(DATA_FILE_PATH)
df = pd.DataFrame(data, columns=['text', 'class'])

vectorizor = CountVectorizor()
train_x = vectorizor.fit_transform(df).toarray()

for ep in range(n_epochs):
    avg_cost = 0

    for i in range(len(train_x)):
        data_points = train_x[i]
        label = train_y[i]
        pred_prob = sigmoid()