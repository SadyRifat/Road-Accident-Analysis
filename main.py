from Data_Retrieve import makeDataset
from Pre_Process import word2num
from Pre_Process import handlingMissingData as md
import pandas as pd

def processingData(column):
    column = word2num.mappingNum(column)
    column = md.replaceByMean(column)
    return column

makeDataset.createDataset()

df = pd.read_csv('Accident-Data.csv')

df['Month'] = processingData(df['Month'])
df['Junction_Type'] = processingData(df['Junction_Type'])
df['Traffic_Control'] = processingData(df['Traffic_Control'])
df['Collision_Type'] = processingData(df['Collision_Type'])
df['Movement'] = processingData(df['Movement'])
df['Divider'] = processingData(df['Divider'])
df['Weather'] = processingData(df['Weather'])
df['Light'] = processingData(df['Light'])
df['Road_Geometry'] = processingData(df['Road_Geometry'])
df['Surface_Condition'] = processingData(df['Surface_Condition'])
df['Surface_Type'] = processingData(df['Surface_Type'])
df['Surface_Quality'] = processingData(df['Surface_Quality'])
df['Road_Class'] = processingData(df['Road_Class'])
df['Road_Feature'] = processingData(df['Road_Feature'])
df['Location_Type'] = processingData(df['Location_Type'])
df['Vehicle_Type'] = processingData(df['Vehicle_Type'])
df['Vehicle_Manoeuvre'] = processingData(df['Vehicle_Manoeuvre'])
df['Vehicle_Loading'] = processingData(df['Vehicle_Loading'])
df['Vehicle_Defect'] = processingData(df['Vehicle_Defect'])
df['Alcohol'] = processingData(df['Alcohol'])
df['Seat_Belt'] = processingData(df['Seat_Belt'])

print(df.describe())
