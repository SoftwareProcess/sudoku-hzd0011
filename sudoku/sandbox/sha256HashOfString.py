'''
Created on Oct 26, 2019

@author: hunterdonald
sandbox used to figure out how to make hash codes for a grid
'''
import hashlib

def getHashOfGrid(gridToBeHashed):
    matrix = [[0 for rowNum in range(9)] for colNum in range(9)]
    strToBeHashed = ""
    
    gridIndex = 0
    for rowIndex in range(9):
        for columnIndex in range(9):
            matrix[rowIndex][columnIndex] = gridToBeHashed[gridIndex]
            gridIndex+=1
   
    for columnIndex in range(9):
        for rowIndex in range(9):
            strToBeHashed += str(matrix[rowIndex][columnIndex])
    hashValue = hashlib.sha256()
    encodedStr = strToBeHashed.encode()
    hashValue.update(encodedStr)
    strToPrint = hashValue.hexdigest()
    print(strToPrint)
getHashOfGrid([4,-5,-8,-9,0,-1,-6,7,2,-2,3,7,-5,-8,0,0,
                         -4,-1,-9,6,1,7,4,2,3,-5,8,-3,9,-6,-1,-5,
                         7,8,-2,4,-1,-4,'c',0,-2,8,-7,6,-9,7,8,2,4,
                         -6,9,-5,1,3,6,-1,-3,-2,9,5,-4,-8,-7,8,2,
                         -4,6,7,-3,1,9,5,-5,7,9,-8,-1,4,-2,3,6])   
#getHashOfGrid([-8,-1,-5,-7,-6,-9,-3,-2,8,-4,-9,0,0,0,-5,-8,-7,0,0,0,-6,0,-4,-8,0,-9,-5,0,-8,-1,0,0,-3,0,0,-2,0,-5,0,-1,-8,0,-9,0,-7,-7,-3,-9,-5,-2,-4,-6,-8,-1,-9,-4,0,0,0,-7,0,-1,-8,-5,-2,0,-8,-9,0,-4,-6,-3,-1,-6,0,-4,-3,-2,-7,0,0])
getHashOfGrid([-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0])