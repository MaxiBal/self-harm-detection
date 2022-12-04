# Self-Harm Detection

import matplotlib
import math
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Import data

DATA_FILE_PATH = r'.\Suicide_Detection.csv'

data = pd.read_csv(DATA_FILE_PATH)
df = pd.DataFrame(data, columns=['text', 'class']).to_numpy()

df[:, 1][df[:, 1] == 'suicide'] = 1
df[:, 1][df[:, 1] == 'non-suicide'] = 0

vectorizor = CountVectorizor()
train_x = vectorizor.fit_transform(df).toarray()

