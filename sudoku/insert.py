import hashlib

def _insert(parms):
    result = {'status': 'insert stub'}
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
    grid[indexInGrid] = value
    return grid
