'''Titanic Survivors Prediction | Kaggle'''
import pandas as pd
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

###################################################
# OVERVIEW
# 1) Read data
# 2) Missing value imputation
# 3) Drop NA / Nulls
# 4) Convert Categorical data to numerics
# 5) Copy target variable to separate data frame
# 6) Remove target variable
# 7) Split - train, cross validation, test
# 8) Predict against any test set
#
##################################################

# Read Train Data - assuming file is in current directory
df = pd.read_csv("Titanic_Train_Kaggle.csv")

# Read Test Data for Prediction - assuming file is in current directory
testDf = pd.read_csv("Titanic_Test_Kaggle.csv")

# Print and check the Structure of data (Initially to understand data)
#print(df.head())
#print(testDf.head())

# Select appropriate attributes
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Embarked']]
testDf = testDf[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Embarked']]

# Missing value imputation
df['Embarked'].fillna('S')
testDf['Embarked'].fillna('S')
df['Age'].fillna((df['Age'].mean()), inplace=True)
testDf['Age'].fillna((testDf['Age'].mean()), inplace=True)

# Convert categorical data to numerics
df["Embarked"] = df["Embarked"].astype("category")
df["Sex"] = df["Sex"].astype("category")
testDf["Embarked"] = testDf["Embarked"].astype("category")
testDf["Sex"] = testDf["Sex"].astype("category")

embarked_col = ['Embarked']
gender_col = ['Sex']
df['Embarked'] = pd.get_dummies(df, columns = embarked_col)
df['Sex'] = pd.get_dummies(df, columns = gender_col)
testDf['Embarked'] = pd.get_dummies(testDf, columns = embarked_col)
testDf['Sex'] = pd.get_dummies(testDf, columns = gender_col)

# Drop NULLs -- though there are no more Nulls in this data set,
# dropping any left over Nulls which haven't been replaced appropriately
df.dropna(inplace=True)
testDf.dropna(inplace=True)

# Print and check the data -- see if the data transformation is as expected (initially during data preprocessing)
#print(df)
#print(testDf)

# Target variable into y
y = np.array(df.Survived)
# Drop target variable from X
X = np.array(df.drop(['Survived'], 1))
X = preprocessing.scale(X)
testDf = preprocessing.scale(testDf)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf1 = svm.SVC(kernel='linear')
clf1.fit(X_train, y_train)
print(clf1.score(X_test, y_test))

print(clf1.predict(np.array(testDf)))
