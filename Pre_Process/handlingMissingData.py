import pandas as pd

def replaceByMean(column):
    column = pd.to_numeric(column, errors='coerce')
    meanValue = int(round(column.mean()))
    column = column.fillna(meanValue).astype(int)
    return column
