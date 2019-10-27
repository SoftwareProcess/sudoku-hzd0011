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
    valueToInsert = int(parms['value'])
    if(_isValueInSubgrid(parms['grid'], valueToInsert, rowNumber, columnNumber)):
        returnGrid = insertValue(parms['grid'], valueToInsert, rowNumber, columnNumber)
        gridToHash = json.dumps(returnGrid)
        result['grid'] = returnGrid
        result['integrity'] = calculateHash(gridToHash)
        result['status'] = 'warning'
        return result 
    if (_isValueInRow(parms['grid'], valueToInsert, rowNumber)):
        returnGrid = insertValue(parms['grid'], valueToInsert, rowNumber, columnNumber)
        gridToHash = json.dumps(returnGrid)
        result['grid'] = returnGrid
        result['integrity'] = calculateHash(gridToHash)
        result['status'] = 'warning'
        return result
    if (_isValueInColumn(parms['grid'], valueToInsert, columnNumber)):
        returnGrid = insertValue(parms['grid'], valueToInsert, rowNumber, columnNumber)
        gridToHash = json.dumps(returnGrid)
        result['grid'] = returnGrid
        result['integrity'] = calculateHash(gridToHash)
        result['status'] = 'warning'
        return result
    returnGrid = insertValue(parms['grid'], valueToInsert, rowNumber, columnNumber)
    gridToHash = json.dumps(returnGrid)
    result['grid'] = returnGrid
    result['integrity'] = calculateHash(gridToHash)
    result['status'] = 'ok'
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

def _whichSubgrid(grid, row, column):
    subgrid = 0
    if (row >= 1 and row < 4):
        if (column >= 1 and column < 4):
            subgrid = 1
            return subgrid
        if (column >= 4 and column < 7):
            subgrid = 2
            return subgrid
        if (column >= 7):
            subgrid = 3
            return subgrid
    if (row >= 4 and row < 7):
        if (column >= 1 and column < 4):
            subgrid = 4
            return subgrid
        if (column >= 4 and column < 7):
            subgrid = 5
            return subgrid
        if (column >= 7):
            subgrid = 6
            return subgrid 
    if (row >= 7):
        if (column >= 1 and column < 4):
            subgrid = 7
            return subgrid
        if (column >= 4 and column < 7):
            subgrid = 8
            return subgrid
        if (column >= 7):
            subgrid = 9
            return subgrid 
    return subgrid

def _returnSubgrid(grid, subgrid):
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    gridIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = grid[gridIndex]
            gridIndex+=1
    subgrid1 = [matrix[0][0], matrix[0][1], matrix[0][2], 
                matrix[1][0], matrix[1][1], matrix[1][2],
                matrix[2][0], matrix[2][1], matrix[2][2]]
    subgrid2 = [matrix[0][3], matrix[0][4], matrix[0][5], 
                matrix[1][3], matrix[1][4], matrix[1][5],
                matrix[2][3], matrix[2][4], matrix[2][5]]
    subgrid3 = [matrix[0][6], matrix[0][7], matrix[0][8], 
                matrix[1][6], matrix[1][7], matrix[1][8],
                matrix[2][6], matrix[2][7], matrix[2][8]]
    subgrid4 = [matrix[3][0], matrix[3][1], matrix[3][2], 
                matrix[4][0], matrix[4][1], matrix[4][2],
                matrix[5][0], matrix[5][1], matrix[5][2]]
    subgrid5 = [matrix[3][3], matrix[3][4], matrix[3][5], 
                matrix[4][3], matrix[4][4], matrix[4][5],
                matrix[5][3], matrix[5][4], matrix[5][5]]
    subgrid6 = [matrix[3][6], matrix[3][7], matrix[3][8], 
                matrix[4][6], matrix[4][7], matrix[4][8],
                matrix[5][6], matrix[5][7], matrix[5][8]]
    subgrid7 = [matrix[6][0], matrix[6][1], matrix[6][2], 
                matrix[7][0], matrix[7][1], matrix[7][2],
                matrix[8][0], matrix[8][1], matrix[8][2]]
    subgrid8 = [matrix[6][3], matrix[6][4], matrix[6][5], 
                matrix[7][3], matrix[7][4], matrix[7][5],
                matrix[8][3], matrix[8][4], matrix[8][5]]
    subgrid9 = [matrix[6][6], matrix[6][7], matrix[6][8], 
                matrix[7][6], matrix[7][7], matrix[7][8],
                matrix[8][6], matrix[8][7], matrix[8][8]]
    if (subgrid == 1):
        return subgrid1
    if (subgrid == 2):
        return subgrid2
    if (subgrid == 3):
        return subgrid3
    if (subgrid == 4):
        return subgrid4
    if (subgrid == 5):
        return subgrid5
    if (subgrid == 6):
        return subgrid6
    if (subgrid == 7):
        return subgrid7
    if (subgrid == 8):
        return subgrid8
    if (subgrid == 9):
        return subgrid9
    else:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0]