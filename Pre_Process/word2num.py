def mappingNum(column):
    arr = column.unique()
    number = 1
    for name in arr:
        column = column.replace({name : number})
        number += 1
    return column


