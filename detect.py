# Self-Harm Detection

import logging

import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfTransformer

# Import data

DATA_FILE_PATH = r'.\Suicide_Detection.csv'

print("Reading data file.")

data = pd.read_csv(DATA_FILE_PATH, on_bad_lines='skip')
df = pd.DataFrame(data, columns=['text', 'class'])

df['class'][df['class'] == 'suicide'] = 1
df['class'][df['class'] == 'non-suicide'] = 0

df['class'] = df['class'].astype(float)

X = df['text'].str.encode('utf-8').str.decode('latin-1').astype(str)
Y = df['class'].to_numpy()

print('Vectorizing Text')

count_vect = CountVectorizer()
x_train_counts = count_vect.fit_transform(X)

tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)


x_train, x_test, y_train, y_test = train_test_split(x_train_tfidf, Y, test_size=0.25, random_state=16)

print('Starting Logistic Regression')

log_reg = LogisticRegression(verbose=1, solver='liblinear', random_state=0, C=5, penalty='l2', max_iter=1000)
model = log_reg.fit(x_train, y_train)

y_score = model.predict(x_test)

n_right = 0
for i in range(len(y_score)):
    if y_score[i] == y_test[i]:
        n_right += 1

print("Accuracy: %.2f%%" % ((n_right/float(len(y_test)) * 100)))

