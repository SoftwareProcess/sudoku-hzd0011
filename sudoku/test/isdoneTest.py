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
        
    # Sad path analysis:
    #    test200_900 should return false on grid with GT 81 elements
    #    test200_910 should return false on grid with LT 81 elements
    #    test200_920 should return false on grid with an invalid cell
    def test100_900ShouldReturnFalseOnGridWithGT81Elements(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0, 0]"
        expectedResult = False
        actualResult = sudoku._isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_910ShouldReturnFalseOnGridWithLT81Elements(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7]"
        expectedResult = False
        actualResult = sudoku._isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_920ShouldReturnFalseOnGridInvalidCell(self):
        grid = "['c', -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        expectedResult = False
        actualResult = sudoku._isValidGrid(grid)
        self.assertEqual(expectedResult, actualResult)
        
    # _calculateHash() unit tests
    #    Happy path analysis:
    #    test300_100 should return correct hash for a grid
    def test300_100ShouldReturnIntegrityValueForGrid(self):
        grid = "[4, -5, -8, -9, 3, -1, -6, 7, 2, -2, 3, 7, -5, -8, 6, 9, -4, -1, -9, 6, 1, 7, 4, 2, 3, -5, 8, -3, 9, -6, -1, -5, 7, 8, -2, 4, -1, -4, 5, 3, -2, 8, -7, 6, -9, 7, 8, 2, 4, -6, 9, -5, 1, 3, 6, -1, -3, -2, 9, 5, -4, -8, -7, 8, 2, -4, 6, 7, -3, 1, 9, 5, -5, 7, 9, -8, -1, 4, -2, 3, 6]"
        expectedResult = 'e33e2de2fdbb25aacf25b299e101cccfdd2e1be4284acc257bcdc76737272af6'
        actualResult = sudoku._calculateHash(grid)
        self.assertEqual(expectedResult, actualResult)
        
    # _isValueInRow() unit tests
    #    Happy path analysis:
    #    test400_100 should return true if value is in row more than once
    #    test400_110 should return false if value is not in row more than once
    def test400_100ShouldReturnTrueIfValueIsInRow(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 3, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
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
        
    # _isValueInColumn() unit tests
    #    Happy path analysis:
    #    test500_100 Should return true if value is in column more than once
    #    test500_110 Should return false if value is not in column more than once
    def test500_100ShouldReturnTrueIfValueIsInColumn(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 9, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
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
        
    # _whichSubgrid() unit tests
    #    Happy path analysis:
    #    test600_100 test corner of a subgrid
    #    test600_110 test middle of a subgrid
    #    test600_120 test middle cell in top row of subgrid
    def test600_100ShouldReturnCorrectSubgridNumberForCellInCornerOfSubgrid(self):
        row = 3
        column = 3
        expectedResult = 1
        actualResult = sudoku._whichSubgrid(row, column)
        self.assertEqual(expectedResult, actualResult)
        
    def test600_110ShouldReturnCorrectSubgridNumberForCellInMiddleOfSubgrid(self):
        row = 5
        column = 8
        expectedResult = 6
        actualResult = sudoku._whichSubgrid(row, column)
        self.assertEqual(expectedResult, actualResult)
        
    def test600_120ShouldReturnCorrectSubgridNumberForCellInMiddleTopPositionOfSubgrid(self):
        row = 7
        column = 5
        expectedResult = 8
        actualResult = sudoku._whichSubgrid(row, column)
        self.assertEqual(expectedResult, actualResult)
        
    # _returnSubgrid() unit tests
    #    Happy path analysis:
    #    test700_100 should return correct subgrid given a subgrid number and matrix
    def test700_100ShouldReturnCorrectSubgridForValidMatrixAndValidSubgridNum(self):
        grid = [-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0]
        subgrid = 7
        expectedResult = [0, 0, 0, 0, -1, 0, -4, 0, 0]
        actualResult = sudoku._returnSubgrid(grid, subgrid)
        self.assertEqual(expectedResult, actualResult)
        
    # _isValueInSubgrid() unit tests
    #    Happy path analysis:
    #    test800_100 should return true if value is in subgrid more than once
    #    test800_110 should return false if value is not in subgrid more than once
    def test800_100ShouldReturnTrueIfValueIsInSubgrid(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, -1, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        value = 1
        row = 2
        column = 3
        expectedResult = True 
        actualResult = sudoku._isValueInSubgrid(grid, value, row, column)
        self.assertEqual(expectedResult, actualResult)
    
    def test800_110ShouldReturnFalseIfValueIsNotInSubgrid(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        value = 7
        row = 2
        column = 3
        expectedResult = False
        actualResult = sudoku._isValueInSubgrid(grid, value, row, column)
        self.assertEqual(expectedResult, actualResult)
        
    # _isGridCompliant() unit tests
    #    test900_100 should return true if a grid does not violate sudoku rules
    #    test900_110 should return false if a grid violates sudoku rules (row)
    #    test900_120 should return false if a grid violates sudoku rules (column)
    #    test900_130 should return false if grid violates sudoku rules (subgrid)
    def test900_100ShouldReturnTrueForGridThatDoesNotViolateSudoku(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        expectedResult = True 
        actualResult = sudoku._isGridCompliant(grid)
        self.assertEqual(expectedResult, actualResult)
      
    def test900_110ShouldReturnFalseForGridThatDoesViolateSudokuRowRule(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 8, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        expectedResult = False 
        actualResult = sudoku._isGridCompliant(grid)
        self.assertEqual(expectedResult, actualResult)  
        
    def test900_120ShouldReturnFalseForGridThatDoesViolateSudokuColumnRule(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 8, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        expectedResult = False 
        actualResult = sudoku._isGridCompliant(grid)
        self.assertEqual(expectedResult, actualResult)
        
    def test900_130ShouldReturnFalseForGridThatDoesViolateSudokuSubGridRule(self):
        grid = "[-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 8, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]"
        expectedResult = False 
        actualResult = sudoku._isGridCompliant(grid)
        self.assertEqual(expectedResult, actualResult)
         
    