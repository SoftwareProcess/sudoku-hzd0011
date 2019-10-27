import hashlib
import math
import json

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
    if (int(parms['cell'][1]) < 1):
        result['status'] = 'error: invalid cell reference'
        return result
    if (int(parms['cell'][3]) < 1):
        result['status'] = 'error: invalid cell reference'
        return result
    if (not('grid' in parms)):
        result['status'] = 'error: missing grid'
        return result
    if (isValidGrid(parms['grid']) == False):
        result['status'] = 'error: invalid grid'
        return result
    if (not('integrity' in parms)):
        result['status'] = 'error: no integrity value given'
        return result
    calculatedIntegrity = calculateHash(parms['grid'])
    if (calculatedIntegrity != parms['integrity']):
        result['status'] = 'error: integrity mismatch'
        return result
    rowNumber = int(parms['cell'][1])
    columnNumber = int(parms['cell'][3])
    if (_isCellAHint(parms['grid'], rowNumber, columnNumber)):
        result['status'] = 'error: attempted to change fixed hint'
        return result
    if (not('value' in parms)):
        returnGrid = insertValue(parms['grid'], 0, rowNumber, columnNumber)
        result['grid'] = returnGrid
        result['status'] = 'ok'
        gridToHash = json.dumps(returnGrid)
        result['integrity'] = calculateHash(gridToHash)
        return result
    if (parms['value'].find(".") > -1):
        result['status'] = 'error: invalid value'
        return result
    if (parms['value'].isalpha() or parms['value'].isspace()):
        result['status'] = 'error: invalid value'
        return result
    if (parms['value'] == ""):
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
    for entry in grid:
        if (entry.isalpha()):
            isGrid = False
            return isGrid
    gridArray = json.loads(grid)
    if (len(gridArray) != 81):
        isGrid = False 
        return isGrid
    return isGrid

def calculateHash(grid):
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    strToBeHashed = ""
    gridArray = json.loads(grid)
    gridIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = gridArray[gridIndex]
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
    gridArray = json.loads(grid)
    indexInGrid = (9 * (row - 1)) + col
    gridArray[indexInGrid - 1] = value
    return gridArray

def _isValueInRow(grid, value, row):
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    isInRow = False
    gridArray = json.loads(grid)
    gridIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = gridArray[gridIndex]
            gridIndex+=1
    for entry in matrix[row - 1]:
        if (math.fabs(int(entry)) == math.fabs(value)):
            isInRow = True 
            return isInRow
    return isInRow

def _isValueInColumn(grid, value, column):
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    isInColumn = False
    gridArray = json.loads(grid)
    columnArray = []
    gridIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = gridArray[gridIndex]
            gridIndex+=1
    rowIndex = 0
    for rowIndex in range(9):
        columnArray.append(matrix[rowIndex][column - 1])
    for entry in columnArray:
        if (math.fabs(int(entry)) == math.fabs(value)):
            isInColumn = True 
            return isInColumn
    return isInColumn

def _isValueInSubgrid(grid, value, row, column):
    subGridArray = []
    gridArray = json.loads(grid)
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    isInSubgrid = False 
    gridIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = gridArray[gridIndex]
            gridIndex+=1
    for rowIndex in range(row - 1, row + 2):
        for columnIndex in range(column - 1, column + 2):
            subGridArray.append(matrix[rowIndex][columnIndex])
    for entry in subGridArray:
        if(math.fabs(int(entry)) == math.fabs(value)):
            isInSubgrid = True  
            return isInSubgrid
    return isInSubgrid

def _isCellAHint(grid, row, column):
    isHint = False
    gridArray = json.loads(grid)
    indexInGrid = (9 * (row - 1)) + (column - 1)
    if (int(gridArray[indexInGrid]) < 0):
        isHint = True 
        return isHint
    return isHint