import pandas as pd
import seaborn as sns
import calendar
from matplotlib import pyplot as plt

df = pd.read_csv('../Accident-Data.csv')


# df['Month'] = df['Month'].map({'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May' : 5, 'June' : 6, 'July' : 7,
#                                'August' : 8, 'September' : 9, 'October' : 10, 'November' : 11, 'December' : 12,})
# df['Junction_Type'] = df['Junction_Type'].map({'No Junction': 1, 'Cross Road': 2, 'T Junction': 3,
#                                                'Staggered Junction': 4, 'Round About' : 5, 'Railway' : 6, 'Other' : 7})
# df['Traffic_Control'] = df['Traffic_Control'].map({'No Control': 1, 'Centreline': 2, 'Pedestrain Crossing': 3, 'Police Control': 4,
#                                                    'Traffic Lights' : 5, 'Police + Traffic Lights' : 6, 'Stop/Give Way Sign' : 7, 'Other' : 8})
# df['Collision_Type'] = df['Collision_Type'].map({'Head On': 1, 'Rear End': 2, 'Right Angle': 3, 'Slide Swip': 4,
#                                                  'Overturned vehicle' : 5,'Hit Object in Road' : 6, 'Hit Object off Road' : 7,
#                                                  'Hit Parked Vehicle' : 8, 'Hit Pedestrian' : 9, 'Hit Animal' : 10, 'Other' : 11})
# df['Movement'] = df['Movement'].map({'1-way Street': 1, '2-way Street': 2})
# df['Divider'] = df['Divider'].map({'Yes': 1, 'No': 2})
# df['Weather'] = df['Weather'].map({'Fair': 1, 'Rain': 2, 'Wind': 3, 'Fog': 4})
# df['Light'] = df['Light'].map({'Daylight': 1, 'Dawn': 2, 'Night(lit)': 3, 'Night(unlit)': 4})
# df['Road_Geometry'] = df['Road_Geometry'].map({'Straight+Flat' : 1, 'Curve Only': 2, 'Slop Only': 3, 'Curve + Slop': 4, 'Crest' : 5})
# df['Surface_Condition'] = df['Surface_Condition'].map({'Dry': 1, 'Wet': 2, 'Muddy': 3, 'Flooded': 4, 'Other' : 5})
# df['Surface_Type'] = df['Surface_Type'].map({'Sealed': 1, 'Brick': 2, 'Earth': 3})
# df['Surface_Quality'] = df['Surface_Quality'].map({'Good': 1, 'Rough': 2, 'Under Repair': 3})
# df['Road_Class'] = df['Road_Class'].map({'National': 1, 'Regional': 2, 'Feeder': 3, 'Rural Road': 4, 'City' : 5})
# df['Road_Feature'] = df['Road_Feature'].map({'None': 1, 'Bridge': 2, 'Culvert': 3, 'Narrowing': 4, 'Speed Breakers' : 5})
# df['Location_Type'] = df['Location_Type'].map({'Urban Area': 1, 'Rural Area': 2})
# df['Vehicle_Type'] = df['Vehicle_Type'].map({'Bicyle': 1, 'Rickshaw': 2, 'Push Cart': 3, 'Motor Cycle': 4, 'Baby Taxi' : 5,
#                                              'Tempo' : 6, 'Microbus' : 7, 'Minibus' : 8, 'Bus' : 9, 'Car' : 10, 'Jeep' : 11,
#                                              'Pick Up' : 12, 'Truck' : 13, 'Heavy Truck' : 14, 'Artic Truck' : 15, 'Oil tanker' : 16,
#                                              'Tractor' : 17, 'Animal Drawn' : 18, 'Other' : 19})
# df['Vehicle_Manoeuvre'] = df['Vehicle_Manoeuvre'].map({'Left Turn': 1, 'Right Turn': 2, 'U Turn': 3, 'Crossing Road': 4, 'Overtaking' : 5,
#                                              'Going Ahead' : 6, 'Reversing' : 7, 'Sudden Start' : 8, 'Sudden Stop' : 9, 'Parked' : 10, 'Other' : 11})
# df['Vehicle_Loading'] = df['Vehicle_Loading'].map({'Legal': 1, 'Unsafe': 2})
# df['Vehicle_Defect'] = df['Vehicle_Defect'].map({'None': 1, 'Lights': 2, 'Brakes': 3, 'Steering': 4, 'Tyres' : 5, 'Multiple' : 6, 'Other' : 7})
# df['Alcohol'] = df['Alcohol'].map({'Suspected': 1, 'Not Suspected': 2})
# df['Seat_Belt'] = df['Seat_Belt'].map({'Yes': 1, 'No': 2, 'Muddy': 3, 'Flooded': 4, 'Other' : 5})

# sns.countplot(x="Accident_Severity", data=df)
# plt.show()


# for col in df.columns:
#     print(col)

# print(df['Junction_Type'].unique())
# sns.countplot(x="Collision_Type", data=df)
# plt.show()
def mapping_num(featureName):
    arr = df[featureName].unique()
    number = 1
    for name in arr:
        df[featureName] = df[featureName].replace({name : number})
        number += 1

mapping_num('Junction_Type')

sns.countplot(x="Junction_Type", data=df)
plt.show()
# print(df['Collision_Type'])


