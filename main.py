from typing import List, Any

from Data_Retrieve import makeDataset
from Pre_Process import word2num
from Pre_Process import handlingMissingData as md
import pandas as pd
import feature_selection as fs
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

print("success")
