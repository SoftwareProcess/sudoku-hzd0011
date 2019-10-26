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
    pass

def insertValue(grid, value):
    pass
