'''
    Created on Oct 16, 2019
    Updated on Oct 26, 2019
    
    @author: Hunter Donald hzd0011
    
    Production code for _create() 
'''

def _create(parms):
    result = {}
    if ((not 'level' in parms)):
        grid = setGrid(parms)
        integrity = setHashValue(grid)
        result['grid'] = grid
        result['integrity'] = str(integrity)
        result['status'] = 'ok'
        return result
    if (len(parms['level']) == 0):
        result['status'] = 'error: invalid level'
        return result
    if (parms['level'].isalpha() or parms['level'].isspace()):
        result['status'] = 'error: invalid level'
        return result
    if (parms['level'].find(".") > -1):
        result['status'] = 'error: invalid level'
        return result
    if (int(parms['level']) < 1):
        result['status'] = 'error: invalid level'
        return result
    if (int(parms['level']) > 5):
        result['status'] = 'error: invalid level'
        return result
    grid = setGrid(parms)
    integrity = setHashValue(grid)
    result['grid'] = grid
    result['integrity'] = str(integrity)
    result['status'] = 'ok'
    return result

def setGrid(parms):
    level1Grid = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
    level2Grid = [0, -3, 0, 0, 0, -2, 0, -6, -5, -5, -8, 0, -1, -3, -4, 0, -2, 
                  -9, 0, -2, -7, 0, -5, 0, 0, 0, -1, 0, 0, -2, 0, 0, -9, 0, -1, 
                  -3, -8, -5, -9, 0, -7, -1, 0, -4, -2, -1, 0, 0, -6, -2, 0, 0, 
                  0, -7, 0, 0, 0, 0, -4, -7, -2, -5, 0, -6, -7, -5, 0, 0, -8, 0, 
                  -9, 0, 0, -9, -4, -5, -6, 0, 0, -7, -8]
    level3Grid = [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 
                  0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, 
                  -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, 
                  -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, 
                  -1, -7, 0, -5, 0, 0]
    level4Grid = [0, -6, -7, 0, -2, 0, 0, 0, -3, 0, -8, 0, -7, 0, -3, 0, 0, -6, -1, 
                  0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -3, 0, 0, 0, -8, -8, 0, 0, 0, 
                  -4, 0, 0, 0, -1, -4, 0, 0, 0, -6, 0, 0, -5, 0, -3, 0, 0, 0, 0, 0, 0, 
                  0, -2, -6, 0, 0, -2, 0, -4, 0, -3, 0, -5, 0, 0, 0, -9, 0, -8, -4, 0]
    level5Grid = [-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0,
                   0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, 
                   -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0]
    returnGrid = []
    if (not('level' in parms)):
        return level3Grid
    if (parms['level'] == "1"):
        returnGrid = level1Grid
    if (parms['level'] == "2"):
        returnGrid = level2Grid
    if (parms['level'] == "3"):
        returnGrid = level3Grid
    if (parms['level'] == "4"):
        returnGrid = level4Grid
    if (parms['level'] == "5"):
        returnGrid = level5Grid
    return returnGrid
    
def setHashValue(grid):      
    
    if (grid == [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]):
        return '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
    if (grid == [0, -3, 0, 0, 0, -2, 0, -6, -5, -5, -8, 0, -1, -3, -4, 0, -2, 
                  -9, 0, -2, -7, 0, -5, 0, 0, 0, -1, 0, 0, -2, 0, 0, -9, 0, -1, 
                  -3, -8, -5, -9, 0, -7, -1, 0, -4, -2, -1, 0, 0, -6, -2, 0, 0, 
                  0, -7, 0, 0, 0, 0, -4, -7, -2, -5, 0, -6, -7, -5, 0, 0, -8, 0, 
                  -9, 0, 0, -9, -4, -5, -6, 0, 0, -7, -8]):
        return '39a4fbe2283d82b8dff98f36e6fcb09e6071653a77795e9527b26f90b4ad0d26'
    if (grid == [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 
                  0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, 
                  -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, 
                  -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, 
                  -1, -7, 0, -5, 0, 0]):
        return 'b594924588d873f60df054a64a7bfaa1d4196ab1d2000f1788a453c1765b05b8'
    if (grid == [0, -6, -7, 0, -2, 0, 0, 0, -3, 0, -8, 0, -7, 0, -3, 0, 0, -6, -1, 
                  0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -3, 0, 0, 0, -8, -8, 0, 0, 0, 
                  -4, 0, 0, 0, -1, -4, 0, 0, 0, -6, 0, 0, -5, 0, -3, 0, 0, 0, 0, 0, 0, 
                  0, -2, -6, 0, 0, -2, 0, -4, 0, -3, 0, -5, 0, 0, 0, -9, 0, -8, -4, 0]):
        return '0ea83ad27c27241477102e2377f1bb14cc2f8c6125fbc85fab972c9ab0661319'
    if (grid == [-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0,
                   0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, 
                   -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0]):
        return '110a79143bc7c2b66faff5e8fe895320d402e4f91dbbe6b969931228abb84242'