'''
    Created on Oct 26, 2019
    
    @author: Hunter Donald hzd0011
    
    Unit tests for methods in _insert 
'''

from unittest import TestCase
import sudoku.insert as sudoku 

class InsertTest(TestCase):
    # isValidGrid() unit tests
    # Happy path analysis:
    #    test100_110 valid grid
    def test100_110ShouldReturnTrueOnValidGrid(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        expectedResult = True 
        actualResult = sudoku._isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)
    # Sad path analysis:
    #    test100_910 grid with GT 81 elements
    #    test100_920 grid with LT 81 elements
    #    test100_930 grid with an invalid cell
    def test100_910ShouldReturnFalseOnGridWithGT81Elements(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0, 0]"
        expectedResult = False
        actualResult = sudoku._isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_920ShouldReturnFalseOnGridWithLT81Elements(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7]"
        expectedResult = False
        actualResult = sudoku._isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_930ShouldReturnFalseOnGridInvalidCell(self):
        grid = "['c', -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        expectedResult = False
        actualResult = sudoku._isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)
        
    # calculateHash() unit tests
    # Happy path analysis:
    #    test200_100 calculate hash for valid grid
    def test200_100ShouldReturnHashValueForValidGrid(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        expectedResult = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = sudoku._calculateHash(grid)
        self.assertEqual(expectedResult, actualResult)
        
    # insertValue() unit tests
    # Happy path analysis:
    #    test300_100 insert value into grid at location
    #    test300_110 insert value into grid at location
    def test300_100ShouldReturnGridWithValidInsertedValue(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        value = 7
        row = 1
        col = 9
        expectedResult = [-8, -1, -5, -7, -6, -9, -3, -2, 7, -4, -9, 0, 0, 0, 
                -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, 
                -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, 
                -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 
                0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, 
                -4, -3, -2, -7, 0, 0]
        actualResult = sudoku._insertValue(grid, value, row, col)
        self.assertEqual(expectedResult, actualResult)
        
    def test300_110ShouldReturnGridWithValidInsertedValue(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        value = 3
        row = 5
        col = 8
        expectedResult = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, 
                -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, 
                -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 3, -7, 
                -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 
                0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, 
                -4, -3, -2, -7, 0, 0]
        actualResult = sudoku._insertValue(grid, value, row, col)
        self.assertEqual(expectedResult, actualResult)
        
    def test300_120ShouldReturnGridWithValidInsertedValue(self):
        grid = "[8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        value = 0
        row = 1
        col = 1
        expectedResult = [0, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, 
                -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, 
                -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, 
                -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 
                0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, 
                -4, -3, -2, -7, 0, 0]
        actualResult = sudoku._insertValue(grid, value, row, col)
        self.assertEqual(expectedResult, actualResult)
        
    # Unit Tests for isValueInRow
    # happy path analysis:
    #    test400_100 value is in row
    #    test400_110 value is not in row
    
    def test400_100ShouldReturnTrueIfValueIsInRow(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        value = 3
        row = 1
        expectedResult = True 
        actualResult = sudoku._isValueInRow(grid, value, row)
        self.assertEqual(expectedResult, actualResult)
        
    def test400_110ShouldReturnFalseIfValueIsNotInRow(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        value = 4
        row = 1
        expectedResult = False 
        actualResult = sudoku._isValueInRow(grid, value, row)
        self.assertEqual(expectedResult, actualResult)
        
    # Unit tests for isValueInColumn
    # Happy path analysis:
    #    test500_100 value is in column
    #    test500_110 value is not in column
    
    def test500_100ShouldReturnTrueIfValueIsInColumn(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        value = 9
        column = 1
        expectedResult = True 
        actualResult = sudoku._isValueInColumn(grid, value, column)
        self.assertEqual(expectedResult, actualResult)
        
    def test500_110ShouldReturnFalseIfValueIsNotInColumn(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        value = 2
        column = 1
        expectedResult = False
        actualResult = sudoku._isValueInColumn(grid, value, column)
        self.assertEqual(expectedResult, actualResult)
        
    # Unit tests for isInSubGrid
    # Happy path analysis:
    #    test600_100 value is in subgrid
    #    test600_110 value is not in subgrid
    
    def test600_100ShouldReturnTrueIfValueIsInSubgrid(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        value = 1
        row = 2
        column = 3
        expectedResult = True 
        actualResult = sudoku._isValueInSubgrid(grid, value, row, column)
        self.assertEqual(expectedResult, actualResult)
        
    def test600_110ShouldReturnFalseIfValueIsNotInSubgrid(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        value = 7
        row = 2
        column = 3
        expectedResult = False
        actualResult = sudoku._isValueInSubgrid(grid, value, row, column)
        self.assertEqual(expectedResult, actualResult)
        
    # Unit tests for isCellAHint()
    # Happy path analysis:
    #    test700_100 value in cell before insert is a hint (last cell in row)
    #    test700_110 value in cell before insert is a hint (first cell in row and column)
    #    test700_120 value in cell before insert is a hint (last in column)
    #    test700_130 value in cell before insert is not a hint
    
    def test700_100ShouldReturnTrueIfValueInCellIsAHintLastInRow(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        row = 3
        col = 9
        expectedResult = True 
        actualResult = sudoku._isCellAHint(grid, row, col)
        self.assertEqual(expectedResult, actualResult)
        
    def test700_110ShouldReturnTrueIfValueInCellIsAHintTopLeftCorner(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        row = 1
        col = 1
        expectedResult = True 
        actualResult = sudoku._isCellAHint(grid, row, col)
        self.assertEqual(expectedResult, actualResult)
        
    def test700_120ShouldReturnTrueIfValueInCellIsAHintLastInColumn(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        row = 9
        col = 5
        expectedResult = True 
        actualResult = sudoku._isCellAHint(grid, row, col)
        self.assertEqual(expectedResult, actualResult)
        
    def test700_130ShouldReturnFalseIfValueInCellIsNotAHint(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        row = 2
        col = 9
        expectedResult = False
        actualResult = sudoku._isCellAHint(grid, row, col)
        self.assertEqual(expectedResult, actualResult)
        
    # Unit tests for _whichSubgrid()
    #    test800_100 test corner of a subgrid
    #    test800_110 test middle of subgrid
    #
    
    def test800_100ShouldReturnTheCorrectSubgridForCoordinates(self):
        row = 3
        column = 3
        expectedResult = 1
        actualResult = sudoku._whichSubgrid(row, column)
        self.assertEqual(expectedResult, actualResult)
        
    def test800_110ShouldReturnTheCorrectSubgridForCoordinates(self):
        row = 5
        column = 8
        expectedResult = 6
        actualResult = sudoku._whichSubgrid(row, column)
        self.assertEqual(expectedResult, actualResult)
        
    # Unit tests for _returnSubgrid()
    #    test900_100 test valid grid and subgrid
    
    def test900_100ShouldReturnCorrect3x3Subgrid(self):
        grid = [-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0]
        subgrid = 7
        expectedResult = [0, 0, 0, 0, -1, 0, -4, 0, 0]
        actualResult = sudoku._returnSubgrid(grid, subgrid)
        self.assertEqual(expectedResult, actualResult)
        