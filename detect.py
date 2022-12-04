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
def read_data(DATA_FILE_PATH):
    print("Reading data file.")

    data = pd.read_csv(DATA_FILE_PATH, on_bad_lines='skip')
    df = pd.DataFrame(data, columns=['text', 'class'])

    df['class'][df['class'] == 'suicide'] = 1
    df['class'][df['class'] == 'non-suicide'] = 0

    df['class'] = df['class'].astype(float)

    X = df['text'].str.encode('utf-8').str.decode('latin-1').astype(str)
    Y = df['class'].to_numpy()

    nan_output = np.isnan(Y)

    Y[nan_output] = 0

    return X, Y

def vectorize_text(X, Y):
    print('Vectorizing Text')

    count_vect = CountVectorizer()
    x_train_counts = count_vect.fit_transform(X)

    tfidf_transformer = TfidfTransformer()
    x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)


    x_train, x_test, y_train, y_test = train_test_split(x_train_tfidf, Y, test_size=0.25, random_state=16)

    return x_train, x_test, y_train, y_test

def logistic_regression(x_train, y_train):

    print('Starting Logistic Regression')

    log_reg = LogisticRegression(verbose=1, solver='liblinear', random_state=0, C=5, penalty='l2', max_iter=1000)
    model = log_reg.fit(x_train, y_train)

    return model

def test_model(model, x_test, y_test):
    y_score = model.predict(x_test)

    n_right = 0
    for i in range(len(y_score)):
        if y_score[i] == y_test[i]:
            n_right += 1

    print("Accuracy: %.2f%%" % ((n_right/float(len(y_test)) * 100)))

def train_model():

    X, Y = read_data(DATA_FILE_PATH)
    x_train, x_test, y_train, y_test = vectorize_text(X, Y)
    model = logistic_regression(x_train, y_train)
    test_model(model, x_test, y_test)

    return model


if __name__ == '__main__':
    train_model()