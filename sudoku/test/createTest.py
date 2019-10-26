'''
    Created on Oct 16, 2019
    
    @author: Hunter Donald hzd0011
    
    Acceptance test file for create.py 
'''

from unittest import TestCase
import sudoku.create as sudoku 


class CreateTest(TestCase):
    # setGrid unit tests
    def test100_010ShouldReturnLevel1Grid(self):
        parms = {}
        parms['level'] = 1
        expectedResult = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        actualResult = sudoku.setGrid(parms)
        self.assertEqual(expectedResult, actualResult)
   
    def test100_020ShouldReturnLevel2Grid(self):
        parms = {}
        parms['level'] = 2
        expectedResult = [0, -3, 0, 0, 0, -2, 0, -6, -5, -5, -8, 0, -1, -3, -4, 0, -2, 
                  -9, 0, -2, -7, 0, -5, 0, 0, 0, -1, 0, 0, -2, 0, 0, -9, 0, -1, 
                  -3, -8, -5, -9, 0, -7, -1, 0, -4, -2, -1, 0, 0, -6, -2, 0, 0, 
                  0, -7, 0, 0, 0, 0, -4, -7, -2, -5, 0, -6, -7, -5, 0, 0, -8, 0, 
                  -9, 0, 0, -9, -4, -5, -6, 0, 0, -7, -8]
        actualResult = sudoku.setGrid(parms)
        self.assertEqual(expectedResult, actualResult)
     
    def test100_030ShouldReturnLevel3Grid(self):
        parms = {}
        parms['level'] = 3
        expectedResult = [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 
                  0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, 
                  -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, 
                  -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, 
                  -1, -7, 0, -5, 0, 0]
        actualResult = sudoku.setGrid(parms)
        self.assertEqual(expectedResult, actualResult)
    
    def test100_040ShouldReturnLevel4Grid(self):
        parms = {}
        parms['level'] = 4
        expectedResult = [0, -6, -7, 0, -2, 0, 0, 0, -3, 0, -8, 0, -7, 0, -3, 0, 0, -6, -1, 
                  0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -3, 0, 0, 0, -8, -8, 0, 0, 0, 
                  -4, 0, 0, 0, -1, -4, 0, 0, 0, -6, 0, 0, -5, 0, -3, 0, 0, 0, 0, 0, 0, 
                  0, -2, -6, 0, 0, -2, 0, -4, 0, -3, 0, -5, 0, 0, 0, -9, 0, -8, -4, 0]
        actualResult = sudoku.setGrid(parms)
        self.assertEqual(expectedResult, actualResult)
    
    def test100_050ShouldReturnLevel5Grid(self):
        parms = {}
        parms['level'] = 5
        expectedResult = [-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0,
                   0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, 
                   -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0]
        actualResult = sudoku.setGrid(parms)
        self.assertEqual(expectedResult, actualResult)
    
    def test100_060ShouldReturnLevel3Grid(self):
        parms = {}
        expectedResult = [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 
                  0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, 
                  -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, 
                  -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, 
                  -1, -7, 0, -5, 0, 0]
        actualResult = sudoku.setGrid(parms)
        self.assertEqual(expectedResult, actualResult)
        
    # setHashValue unit tests
    def test110_010ShouldReturnLevel1Hash(self):
        grid = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        expectedResult = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = sudoku.setHashValue(grid)
        self.assertEqual(expectedResult, actualResult)
   
    def test110_020ShouldReturnLevel2Hash(self):
        grid = [0, -3, 0, 0, 0, -2, 0, -6, -5, -5, -8, 0, -1, -3, -4, 0, -2, 
                  -9, 0, -2, -7, 0, -5, 0, 0, 0, -1, 0, 0, -2, 0, 0, -9, 0, -1, 
                  -3, -8, -5, -9, 0, -7, -1, 0, -4, -2, -1, 0, 0, -6, -2, 0, 0, 
                  0, -7, 0, 0, 0, 0, -4, -7, -2, -5, 0, -6, -7, -5, 0, 0, -8, 0, 
                  -9, 0, 0, -9, -4, -5, -6, 0, 0, -7, -8]
        expectedResult = '39a4fbe2283d82b8dff98f36e6fcb09e6071653a77795e9527b26f90b4ad0d26'
        actualResult = sudoku.setHashValue(grid)
        self.assertEqual(expectedResult, actualResult)
    
    def test110_030ShouldReturnLevel3Hash(self):
        grid = [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 
                  0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, 
                  -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, 
                  -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, 
                  -1, -7, 0, -5, 0, 0]
        expectedResult = 'b594924588d873f60df054a64a7bfaa1d4196ab1d2000f1788a453c1765b05b8'
        actualResult = sudoku.setHashValue(grid)
        self.assertEqual(expectedResult, actualResult)
        
    def test110_040ShouldReturnLevel4Hash(self):
        grid = [0, -6, -7, 0, -2, 0, 0, 0, -3, 0, -8, 0, -7, 0, -3, 0, 0, -6, -1, 
                  0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -3, 0, 0, 0, -8, -8, 0, 0, 0, 
                  -4, 0, 0, 0, -1, -4, 0, 0, 0, -6, 0, 0, -5, 0, -3, 0, 0, 0, 0, 0, 0, 
                  0, -2, -6, 0, 0, -2, 0, -4, 0, -3, 0, -5, 0, 0, 0, -9, 0, -8, -4, 0]
        expectedResult = '0ea83ad27c27241477102e2377f1bb14cc2f8c6125fbc85fab972c9ab0661319'
        actualResult = sudoku.setHashValue(grid)
        self.assertEqual(expectedResult, actualResult)
    
    def test110_050ShouldReturnLevel5Hash(self):
        grid = [-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0,
                   0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, 
                   -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0]
        expectedResult = '110a79143bc7c2b66faff5e8fe895320d402e4f91dbbe6b969931228abb84242'
        actualResult = sudoku.setHashValue(grid)
        self.assertEqual(expectedResult, actualResult)