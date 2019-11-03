import json

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
    pass

def _isValueInRow(grid, value, row):
    pass

def _isValueInColumn(grid, value, column):
    pass

def _isValueInSubgrid(grid, value, row, column):
    pass

def _whichSubgrid(row, column):
    pass

def _returnSubgrid(grid, subgrid):
    pass

