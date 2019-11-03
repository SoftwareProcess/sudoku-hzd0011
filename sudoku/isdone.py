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
    pass

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

