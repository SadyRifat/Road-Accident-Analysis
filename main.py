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
df = df.drop(['X', 'Y', 'Road_No', 'Accident_Severity'], axis=1)
X = df


df = df.drop('Driver_Age', axis=1)
for feature in df.columns:
    X[feature] = word2num.mappingNum(X[feature])
    X[feature] = md.replaceByMean(X[feature])


X['Driver_Age'] = md.replaceByMean(X['Driver_Age'])

fs.featureExtraction(X, Y)
fs.recursiveFeatureElimination(X, Y)
fs.univarientFeatureExtraction(X, Y)

print('success')
