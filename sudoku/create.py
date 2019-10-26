'''
    Created on Oct 16, 2019
    
    @author: Hunter Donald hzd0011
    
    Production code for _create() 
'''

def _create(parms):
    pass

def setGrid(parms):
    level1Grid = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
    if (parms['level'] == 1):
        returnGrid = level1Grid
    return returnGrid
    
def setHashValue(parms):
    pass