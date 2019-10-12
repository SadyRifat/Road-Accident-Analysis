from Data_Retrieve import makeDataset
from Pre_Process import word2num
from Pre_Process import handlingMissingData as md
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import pandas as pd
import feature_selection as fs
import learningAlgorithms as algo
import warnings

warnings.filterwarnings("ignore")


# makeDataset.createDataset()

df = pd.read_csv('Accident-Data.csv')
Y = df['Accident_Severity']
df = df.drop(['Unnamed: 0', 'X', 'Y', 'Road_No', 'Accident_Severity'], axis=1)
X = df


df = df.drop('Driver_Age', axis=1)
for feature in df.columns:
    X[feature] = word2num.mappingNum(X[feature])
    X[feature] = md.replaceByMean(X[feature])


X['Driver_Age'] = md.replaceByMean(X['Driver_Age'])
Xfeature = []
for feature in X.columns:
    Xfeature.append(feature)

featureExtraction = fs.featureExtraction(X, Y, 15)
recursiveFeature = fs.recursiveFeatureElimination(X, Y, 15)
univariateFeature = fs.univariateFeatureExtraction(X, Y, 15)

featureLIST = []
featureLIST.append(featureExtraction)
featureLIST.append(recursiveFeature)
featureLIST.append(univariateFeature)

commonFeatures = fs.findCommonFeature(featureLIST)
intersectionFeature = fs.findIntersectionFeature(Xfeature, commonFeatures)
for feature in intersectionFeature:
    X = X.drop(feature, axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)

model = algo.decesionTree(X_train, Y_train)
pred = model.predict(X_test)
print((classification_report(Y_test, pred)))


model = algo.naiveBayes(X_train, Y_train)
pred = model.predict(X_test)
print((classification_report(Y_test, pred)))


model = algo.adaBoost(X_train, Y_train)
pred = model.predict(X_test)
print((classification_report(Y_test, pred)))

