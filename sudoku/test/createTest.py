from unittest import TestCase
import sudoku.create as sudoku 

class CreateTest(TestCase):
    # Happy path
    #    Test that each level returns the correct grid
    def test100_010TestCreatingGridWithLevel1(self):
        parms = {}
        parms['level'] = 1
        expectedResult = {}
        expectedResult['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        expectedResult['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        expectedResult['status'] = 'ok'
        actualResult = sudoku._create(parms)
        self.assertEqual(expectedResult, actualResult)