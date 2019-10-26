from unittest import TestCase
import sudoku.insert as sudoku 

class InsertTest(TestCase):
    # isValidGrid() unit tests
    # Happy path analysis:
    #    test100_110 valid grid
    def test100_110ShouldReturnTrueOnValidGrid(self):
        grid = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        expectedResult = True 
        actualResult = sudoku.isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)
    # Sad path analysis:
    #    test100_910 grid with GT 81 elements
    #    test100_920 grid with LT 81 elements
    #    test100_930 grid with an invalid cell
    def test100_910ShouldReturnFalseOnGridWithGT81Elements(self):
        grid = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0, 0]
        expectedResult = False
        actualResult = sudoku.isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_920ShouldReturnFalseOnGridWithLT81Elements(self):
        grid = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7]
        expectedResult = False
        actualResult = sudoku.isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_930ShouldReturnFalseOnGridInvalidCell(self):
        grid = ['c', -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        expectedResult = False
        actualResult = sudoku.isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)
        
    # calculateHash() unit tests
    # Happy path analysis:
    #    test200_100 calculate hash for valid grid
    def test200_100ShouldReturnHashValueForValidGrid(self):
        grid = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, 
                -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, 
                -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, 
                -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 
                0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, 
                -4, -3, -2, -7, 0, 0]
        expectedResult = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = sudoku.calculateHash(grid)
        self.assertEqual(expectedResult, actualResult)
        
    # insertValue() unit tests
    # Happy path analysis:
    #    test300_100 insert value into grid at location
    def test300_100ShouldReturnGridWithInsertedValue(self):
        grid = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, 
                -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, 
                -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, 
                -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 
                0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, 
                -4, -3, -2, -7, 0, 0]
        value = 7
        row = 1
        col = 9
        expectedResult = [-8, -1, -5, -7, -6, -9, -3, -2, 7, -4, -9, 0, 0, 0, 
                -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, 
                -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, 
                -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 
                0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, 
                -4, -3, -2, -7, 0, 0]
        actualResult = sudoku.insertValue(grid, value, row, col)
        self.assertEqual(expectedResult, actualResult)
        