import hashlib
import math

def _insert(parms):
    result = {'status': 'insert stub'}
    if (not('cell' in parms)):
        result['status'] = 'error: missing cell reference'
        return result
    if (len(parms['cell']) != 4):
        result['status'] = 'error: invalid cell reference'
        return result
    if (parms['cell'][0] != 'r'):
        if (parms['cell'][0] != 'R'):
            result['status'] = 'error: invalid cell reference'
            return result
    if (parms['cell'][2] != 'c'):
        if (parms['cell'][2] != 'C'):
            result['status'] = 'error: invalid cell reference'
            return result 
    if (parms['cell'][1].isalpha() or parms['cell'][1].isspace()):
        result['status'] = 'error: invalid cell reference'
        return result 
    if (parms['cell'][3].isalpha() or parms['cell'][3].isspace()):
        result['status'] = 'error: invalid cell reference'
        return result 
    if (parms['value'].isalpha() or parms['value'].isspace()):
        result['status'] = 'error: invalid value'
        return result
    if (parms['level'].find(".") > -1):
        result['status'] = 'error: invalid value'
        return result
    if (int(parms['cell'][1]) < 1):
        result['status'] = 'error: invalid cell reference'
        return result
    if (int(parms['cell'][3]) < 1):
        result['status'] = 'error: invalid cell reference'
        return result
    if (len(parms['value']) == 0):
        result['status'] = 'error: invalid value'
        return result
    if (int(parms['value']) < 1):
        result['status'] = 'error: invalid value'
        return result
    if (int(parms['value']) > 9):
        result['status'] = 'error: invalid value'
        return result
    return result

def isValidGrid(grid):
    isGrid = True
    if (len(grid) > 81):
        isGrid = False
        return isGrid
    if (len(grid) < 81):
        isGrid = False
        return isGrid
    for gridIndex in range(81):
        if (not(isinstance(grid[gridIndex], int))):
            isGrid = False
    return isGrid

def calculateHash(grid):
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    strToBeHashed = ""
    
    gridIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = grid[gridIndex]
            gridIndex+=1
   
    for columnIndex in range(9):
        for rowIndex in range(9):
            strToBeHashed += str(matrix[rowIndex][columnIndex])
    hashValue = hashlib.sha256()
    encodedStr = strToBeHashed.encode()
    hashValue.update(encodedStr)
    strToReturn = hashValue.hexdigest()
    return strToReturn

def insertValue(grid, value, row, col):
    indexInGrid = (9 * (row - 1)) + col
    grid[indexInGrid - 1] = value
    return grid

def _isValueInRow(grid, value, row):
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    isInRow = False
    gridIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = grid[gridIndex]
            gridIndex+=1
    for entry in matrix[row - 1]:
        if (math.fabs(entry) == math.fabs(value)):
            isInRow = True 
            return isInRow
    return isInRow

def _isValueInColumn(grid, value, column):
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    isInColumn = False
    columnArray = []
    gridIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = grid[gridIndex]
            gridIndex+=1
    rowIndex = 0
    for rowIndex in range(9):
        columnArray.append(matrix[rowIndex][column - 1])
    for entry in columnArray:
        if (math.fabs(entry) == math.fabs(value)):
            isInColumn = True 
            return isInColumn
    return isInColumn

def _isValueInSubgrid(grid, value, row, column):
    subGridArray = []
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    isInSubgrid = False 
    gridIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = grid[gridIndex]
            gridIndex+=1
    for rowIndex in range(row - 1, row + 2):
        for columnIndex in range(column - 1, column + 2):
            subGridArray.append(matrix[rowIndex][columnIndex])
    for entry in subGridArray:
        if(math.fabs(entry) == math.fabs(value)):
            isInSubgrid = True  
            return isInSubgrid
    return isInSubgrid