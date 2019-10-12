import numpy as np


def mappingNum(column):
    arr = column.unique()
    index = np.argwhere(arr == '?')
    arr = np.delete(arr, index)
    number = 1
    for name in arr:
        column = column.replace({name : number})
        number += 1
    return column

