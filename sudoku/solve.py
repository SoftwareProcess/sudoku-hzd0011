import json
import hashlib
import math

def _solve(parms):
    result = {}
    if (not(_isValidGrid(parms['grid']))):
        result['status'] = 'error: invalid grid'
        return result
    return result

def _suggestSolution(grid):
    gridArray = json.loads(grid)
    legalValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    emptyArray = []
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    gridArrayIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = gridArray[gridArrayIndex]
            gridArrayIndex+=1
    if (_isCompleted(grid) and _isGridCompliant(grid)):
        return gridArray 
    elif (_isCompleted(grid) and not(_isGridCompliant(grid))):
        return emptyArray
    else:
        gridArrayIndex = 0
        breakLoopIfTrue = False 
        for rowIndex in range(9):
            for columnIndex in range(9):
                if (matrix[rowIndex][columnIndex] == 0):
                    breakLoopIfTrue = True 
                    break
                gridArrayIndex += 1
            if (breakLoopIfTrue):
                break
        for value in legalValues:
            gridArray[gridArrayIndex] = value
            suggestedGridString = json.dumps(gridArray)
            if (not(_isValueInRow(suggestedGridString, value, rowIndex + 1))):
                if (not(_isValueInColumn(suggestedGridString, value, columnIndex + 1))):
                    if (not(_isValueInSubgrid(suggestedGridString, value, rowIndex + 1, columnIndex + 1))):
                        suggestedArray = _suggestSolution(suggestedGridString)
                        if (len(suggestedArray) != 0):
                            return suggestedArray
        return emptyArray

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
    gridIsCompliant = True 
    matrix = [[0 for rowNum in range(9)] for columnNum in range(9)]
    gridArray = json.loads(grid)
    gridIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = gridArray[gridIndex]
            gridIndex+=1
    for rowIndex in range(1, 10):
        for columnIndex in range(1, 10):
            if (int(matrix[rowIndex - 1][columnIndex - 1]) != 0):
                if (_isValueInRow(grid, int(matrix[rowIndex - 1][columnIndex - 1]), rowIndex)):
                    gridIsCompliant = False 
                    return gridIsCompliant
                if (_isValueInColumn(grid, int(matrix[rowIndex - 1][columnIndex - 1]), columnIndex)):
                    gridIsCompliant = False 
                    return gridIsCompliant
                if (_isValueInSubgrid(grid, int(matrix[rowIndex - 1][columnIndex - 1]), rowIndex, columnIndex)):
                    gridIsCompliant = False 
                    return gridIsCompliant
    return gridIsCompliant

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
    gridArray = json.loads(grid)
    isInSubgrid = False 
    numberOfTimesValueIsInSubgrid = 0
    subgridNumber = _whichSubgrid(row, column)
    subGridArray = _returnSubgrid(gridArray, subgridNumber)
    for entry in subGridArray:
        if (math.fabs(entry) == math.fabs(value)):
            numberOfTimesValueIsInSubgrid += 1
            if (numberOfTimesValueIsInSubgrid > 1):
                isInSubgrid = True 
                return isInSubgrid
    return isInSubgrid

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
