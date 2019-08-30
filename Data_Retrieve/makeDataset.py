import pandas as pd
import datetime


def getAccidentSeverity(number):
    Accident_Severity = {
        "F" : "Fatal",
        "G" : "Grievios",
        "S" : "Simple",
        "M" : "Motor Collusion",
        "?" : "?"
    }
    return Accident_Severity[str(number)]


def getMonthName(month_num):
    if (str(month_num) == "?"):
        return  "?"
    month_name = datetime.date(2015, int(month_num), 1).strftime('%B')
    return  month_name


def getTime(number):
    if(number == "?"):
        return "?"
    else:
        hour = float(number)
        Time = 0
        if(hour>=0 and hour<6):
            Time = 1
        elif(hour>=6 and hour<12):
            Time = 2
        elif(hour>=12 and hour<18):
            Time = 3
        elif(hour>=18 and hour<24):
            Time = 4
    return Time


def getJunctionType(number):
    Junction_Type = {
        "1" : "No Junction",
        "2" : "Cross Road",
        "3" : "T Junction",
        "4" : "Staggered Junction",
        "5" : "Round About",
        "6" : "Railway",
        "7" : "Other",
        "?" : "?"
    }
    return  Junction_Type[number]


def getTrafficControl(number):
    Traffic_Control = {
        "1" : "No Control",
        "2" : "Centreline",
        "3" : "Pedestrain Crossing",
        "4" : "Police Control",
        "5" : "Traffic Lights",
        "6" : "Police + Traffic Lights",
        "7" : "Stop/Give Way Sign",
        "8" : "Other",
        "?" : "?"
    }
    return Traffic_Control[number]


def getCollisionType(number):
    Collision_Type = {
        "01" : "Head On",
        "02" : "Rear End",
        "03" : "Right Angle",
        "04" : "Slide Swip",
        "05" : "Overturned vehicle",
        "06" : "Hit Object in Road",
        "07" : "Hit Object off Road",
        "08" : "Hit Parked Vehicle",
        "09" : "Hit Pedestrian",
        "10" : "Hit Animal",
        "11" : "Other",
        " ?" : "?"
    }
    return Collision_Type[number]


def getMovement(number):
    Movement = {
        "1" : "1-way Street",
        "2" : "2-way Street",
        "?" : "?"
    }
    return Movement[number]


def getDivider(number):
    Divider = {
        "1" : "Yes",
        "2" : "No",
        "?" : "?"
    }
    return Divider[number]


def getWeather(number):
    Weather = {
        "1" : "Fair",
        "2" : "Rain",
        "3" : "Wind",
        "4" : "Fog",
        "?" : "?"
    }
    return Weather[number]


def getLight(number):
    Light = {
        "1" : "Daylight",
        "2" : "Dawn",
        "3" : "Night(lit)",
        "4" : "Night(unlit)",
        "?" : "?"
    }
    return Light[number]


def getRoadGeometry(number):
    RoadGeometry = {
        "1" : "Straight+Flat",
        "2" : "Curve Only",
        "3" : "Slop Only",
        "4" : "Curve + Slop",
        "5" : "Crest",
        "?" : "?"
    }
    return RoadGeometry[number]


def getSurfaceCondition(number):
    Surface_Condition = {
        "1" : "Dry",
        "2" : "wet",
        "3" : "Muddy",
        "4" : "Flooded",
        "5" : "Other",
        "?" : "?"
    }
    return Surface_Condition[number]


def getSurfaceType(number):
    Surface_Type = {
        "1" : "Sealed",
        "2" : "Brick",
        "3" : "Earth",
        "?" : "?"
    }
    return Surface_Type[number]


def getSurfaceQuality(number):
    Surface_Quality = {
        "1" : "Good",
        "2" : "Rough",
        "3" : "Under Repair",
        "?" : "?"
    }
    return Surface_Quality[number]


def getRoadClass(number):
    Road_Class = {
        "1" : "National",
        "2" : "Regional",
        "3" : "Feeder",
        "4" : "Rural Road",
        "5" : "City",
        "?" : "?"
    }
    return Road_Class[number]


def getRoadFeature(number):
    Road_Feature = {
        "1" : "None",
        "2" : "Bridge",
        "3" : "Culvert",
        "4" : "Narrowing",
        "5" : "Speed Breakers",
        "?" : "?"
    }
    return Road_Feature[number]


def getLocationType(number):
    Location_Type = {
        "1" : "Urban Area",
        "2" : "Rural Area",
        "?" : "?"
    }
    return Location_Type[number]


def getVehicleLoading(number):
    Vehicle_Loading = {
        "1" : "Legal",
        "2" : "Unsafe",
        "?" : "?"
    }
    return Vehicle_Loading[number]


def getVehicleDefect(number):
    Vehicle_Defect = {
        "1" : "None",
        "2" : "Lights",
        "3" : "Brakes",
        "4" : "Steering",
        "5" : "Tyres",
        "6" : "Multiple",
        "7" : "Other",
        "?" : "?"
    }
    return Vehicle_Defect[number]


def getAlcohol(number):
    Alcohol = {
        "1" : "Suspected",
        "2" : "Not Suspected",
        "?" : "?"
    }
    return Alcohol[number]


def getSeatBelt(number):
    Seat_Belt = {
        "1" : "Yes",
        "2" : "No",
        "?" : "?"
    }
    return Seat_Belt[number]


def getVehicleType(number):
    Vehicle_Type = {
        "01" : "Bicyle",
        "02" : "Rickshaw",
        "03" : "Push Cart",
        "04" : "Motor Cycle",
        "05" : "Baby Taxi",
        "06" : "Tempo",
        "07" : "Microbus",
        "08" : "Minibus",
        "09" : "Bus",
        "10" : "Car",
        "11" : "Jeep",
        "12" : "Pick Up",
        "13" : "Truck",
        "14" : "Heavy Truck",
        "15" : "Artic Truck",
        "16" : "Oil tanker",
        "17" : "Tractor",
        "18" : "Animal Drawn",
        "19" : "Other",
        " ?" : "?"
    }
    return Vehicle_Type[number]


def getVehicleManoeuvre(number):
    Vehicle_Manoeuvre = {
        "01" : "Left Turn",
        "02" : "Right Turn",
        "03" : "U Turn",
        "04" : "Crossing Road",
        "05" : "Overtaking",
        "06" : "Going Ahead",
        "07" : "Reversing",
        "08" : "Sudden Start",
        "09" : "Sudden Stop",
        "10" : "Parked",
        "11" : "Other",
        " ?" : "?"
    }
    return Vehicle_Manoeuvre[number]


def createDataset():
    with open('Data_Retrieve/data.txt') as f:
        lines = f.readlines()

    Columns = ['Thana','District','Accident_Severity','Month','Year','Time','Junction_Type','Traffic_Control',
               'Collision_Type','Movement','Divider','Weather','Light','Road_Geometry','Surface_Condition','Surface_Type',
               'Surface_Quality','Road_Class','Road_Feature','Location_Type','X','Y','Road_No','Vehicle_Type',
               'Vehicle_Manoeuvre','Vehicle_Loading','Vehicle_Defect','Driver_Age','Alcohol','Seat_Belt']

    df = pd.DataFrame(columns=Columns)

    for index in lines:
        Thana = index[9:12]
        District = index[12:14]
        Accident_Severity = getAccidentSeverity(index[22:23])
        Month = getMonthName(index[26:28])
        Year = 2000 + int(index[28:30])
        Time = getTime(index[30:32])
        Junction_Type = getJunctionType(index[34:35])
        Traffic_Control = getTrafficControl(index[35:36])
        Collision_Type = getCollisionType(index[36:38])
        Movement = getMovement(index[38:39])
        Divider = getMovement(index[39:40])
        Weather = getWeather(index[40:41])
        Light = getLight(index[41:42])
        Road_Geometry = getRoadGeometry(index[42:43])
        Surface_Condition = getSurfaceCondition(index[43:44])
        Surface_Type = getSurfaceType(index[44:45])
        Surface_Quality = getSurfaceQuality(index[45:46])
        Road_Class = getRoadClass(index[46:47])
        Road_Feature = getRoadFeature(index[47:48])
        Location_Type = getLocationType(index[48:49])
        X = index[51:57]
        Y = index[57:63]
        Road_No = index[63:67]
        Vehicle_Type = getVehicleType(index[97:99])
        Vehicle_Manoeuvre = getVehicleManoeuvre(index[99:101])
        Vehicle_Loading = getVehicleLoading(index[101:102])
        Vehicle_Defect = getVehicleDefect(index[102:103])
        Driver_Age = index[119:121]
        Alcohol = getAlcohol(index[122:123])
        Seat_Belt = getSeatBelt(index[123:124])

        df = df.append(pd.DataFrame([[Thana, District, Accident_Severity, Month, Year, Time, Junction_Type, Traffic_Control,
                                      Collision_Type, Movement, Divider, Weather, Light, Road_Geometry, Surface_Condition,
                                      Surface_Type, Surface_Quality, Road_Class, Road_Feature, Location_Type, X, Y, Road_No,
                                      Vehicle_Type, Vehicle_Manoeuvre, Vehicle_Loading, Vehicle_Defect, Driver_Age,
                                      Alcohol, Seat_Belt]], columns=Columns), ignore_index=True)

    df.to_csv("Accident-Data.csv")
