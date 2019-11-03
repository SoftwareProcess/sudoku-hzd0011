import json
import hashlib
import math

def _isdone(parms):
    result = {'status': 'isdone stub'}
    return result

def _isCompleted(grid):
    isCompleted = True 
    for entry in grid:
        if entry == '0':
            isCompleted = False 
            return isCompleted
    return isCompleted

def _isGridCompliant(grid):
    pass

def _isSolved(grid):
    pass

def _isValidGrid(grid):
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

def _calculateHash(grid):
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
    pass

def _isValueInSubgrid(grid, value, row, column):
    pass

def _whichSubgrid(row, column):
    pass

def _returnSubgrid(grid, subgrid):
    pass

