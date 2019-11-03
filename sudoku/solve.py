import json
import hashlib
import math

def _solve(parms):
    result = {'status': 'solve stub'}
    return result

def _suggestSolution(grid):
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

def _isCompleted(grid):
    isCompleted = True 
    for entry in grid:
        if entry == '0':
            isCompleted = False 
            return isCompleted
    return isCompleted

def _isGridCompliant(grid):
    pass

def _isValueInRow(grid, value, row):
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    isInRow = False
    gridArray = json.loads(grid)
    gridIndex = 0
    numberOfTimesValueIsInRow = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = gridArray[gridIndex]
            gridIndex+=1
    for entry in matrix[row - 1]:
        if (math.fabs(int(entry)) == math.fabs(value)):
            numberOfTimesValueIsInRow += 1
            if (numberOfTimesValueIsInRow > 1):
                isInRow = True 
                return isInRow
    return isInRow

def _isValueInColumn(grid, value, column):
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    isInColumn = False
    gridArray = json.loads(grid)
    columnArray = []
    gridIndex = 0
    numberOfTimesValueIsInColumn = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = gridArray[gridIndex]
            gridIndex+=1
    rowIndex = 0
    for rowIndex in range(9):
        columnArray.append(matrix[rowIndex][column - 1])
    for entry in columnArray:
        if (math.fabs(int(entry)) == math.fabs(value)):
            numberOfTimesValueIsInColumn += 1
            if (numberOfTimesValueIsInColumn > 1):
                isInColumn = True 
                return isInColumn   
    return isInColumn

def _isValueInSubgrid(grid, value, row, column):
    pass

def _whichSubgrid(row, column):
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
    pass
