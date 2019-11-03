from unittest import TestCase
import sudoku.isdone as sudoku 

class IsdoneTest(TestCase):
    # _isCompleted() unit tests
    #    Happy path analysis:
    #    test100_100 should return true on completely filled in grid
    #    test100_110 should return false on grid with at least one cell not filled
    def test100_100ShouldReturnTrueOnFullGrid(self):
        grid = "[4, -5, -8, -9, 3, -1, -6, 7, 2, -2, 3, 7, -5, -8, 6, 9, -4, -1, -9, 6, 1, 7, 4, 2, 3, -5, 8, -3, 9, -6, -1, -5, 7, 8, -2, 4, -1, -4, 5, 3, -2, 8, -7, 6, -9, 7, 8, 2, 4, -6, 9, -5, 1, 3, 6, -1, -3, -2, 9, 5, -4, -8, -7, 8, 2, -4, 6, 7, -3, 1, 9, 5, -5, 7, 9, -8, -1, 4, -2, 3, 6]"
        expectedResult = True 
        actualResult = sudoku._isCompleted(grid)
        self.assertEqual(expectedResult, actualResult)
    
    def test100_110ShouldReturnFalseOnGridWithAnEmptyCell(self):
        grid = "[4, -5, -8, -9, 3, -1, -6, 7, 2, -2, 3, 7, -5, -8, 6, 0, -4, -1, -9, 6, 1, 7, 4, 2, 3, -5, 8, -3, 9, -6, -1, -5, 7, 8, -2, 4, -1, -4, 5, 3, -2, 8, -7, 6, -9, 7, 8, 2, 4, -6, 9, -5, 1, 3, 6, -1, -3, -2, 9, 5, -4, -8, -7, 8, 2, -4, 6, 7, -3, 1, 9, 5, -5, 7, 9, -8, -1, 4, -2, 3, 6]"
        expectedResult = False 
        actualResult = sudoku._isCompleted(grid)
        self.assertEqual(expectedResult, actualResult)
        
    # _isValidGrid() unit tests
    #    Happy path analysis:
    #    test200_100 should return true on valid grid
    def test200_100ShouldReturnTrueOnValidGrid(self):
        grid = "[4, -5, -8, -9, 3, -1, -6, 7, 2, -2, 3, 7, -5, -8, 6, 9, -4, -1, -9, 6, 1, 7, 4, 2, 3, -5, 8, -3, 9, -6, -1, -5, 7, 8, -2, 4, -1, -4, 5, 3, -2, 8, -7, 6, -9, 7, 8, 2, 4, -6, 9, -5, 1, 3, 6, -1, -3, -2, 9, 5, -4, -8, -7, 8, 2, -4, 6, 7, -3, 1, 9, 5, -5, 7, 9, -8, -1, 4, -2, 3, 6]"
        expectedResult = True 
        actualResult = sudoku._isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)