import pandas as pd
def replaceByMean(column):
    column = pd.to_numeric(column, errors='coerce')
    meanValue = int(round(column.mean()))
    column = column.astype(str)
    column = column.replace({'?' : meanValue})
    column = pd.to_numeric(column, errors='coerce')
    return column
