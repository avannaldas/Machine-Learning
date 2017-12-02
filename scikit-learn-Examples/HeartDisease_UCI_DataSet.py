'''
Classification Example based on UCI Dataset:
    Lichman, M. (2013).
    UCI Machine Learning Repository [http://archive.ics.uci.edu/ml].
    Irvine, CA: University of California, School of Information and Computer Science.

Dataset Link: http://archive.ics.uci.edu/ml/datasets/Statlog+%28Heart%29

Changes made to dataset before use:
    The data set was originally space separated, converted it to comma 
    separated and added column headers based on the dataset description.
    Dataset can be downloaded from the link given above
'''

import pandas as pd
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np

print('Reading data...')
df = pd.read_csv('heart.csv')
print('Initial data: df.head()...')
print(df.head())

print('Pre-Processing data...')
y = np.array(df['disease'])
X = np.array(df.drop(['disease'], 1))
X = preprocessing.scale(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print('Training...')
forest = ExtraTreesClassifier(n_estimators=200)
forest.fit(X_train, y_train)
print(forest.score(X_test, y_test))
