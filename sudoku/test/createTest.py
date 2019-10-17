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
        
    def test100_020TestCreatingGridWithLevel2(self):
        parms = {}
        parms['level'] = 2
        expectedResult = {}
        expectedResult['grid'] = [0, -3, 0, 0, 0, -2, 0, -6, -5, -5, -8, 0, -1, -3, -4, 0, -2, -9, 0, -2, -7, 0, -5, 0, 0, 0, -1, 0, 0, -2, 0, 0, -9, 0, -1, -3, -8, -5, -9, 0, -7, -1, 0, -4, -2, -1, 0, 0, -6, -2, 0, 0, 0, -7, 0, 0, 0, 0, -4, -7, -2, -5, 0, -6, -7, -5, 0, 0, -8, 0, -9, 0, 0, -9, -4, -5, -6, 0, 0, -7, -8]
        expectedResult['integrity'] = '39a4fbe2283d82b8dff98f36e6fcb09e6071653a77795e9527b26f90b4ad0d26'
        expectedResult['status'] = 'ok'
        actualResult = sudoku._create(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_030TestCreatingGridWithLevel3(self):
        parms = {}
        parms['level'] = 3
        expectedResult = {}
        expectedResult['grid'] = [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, -1, -7, 0, -5, 0, 0]
        expectedResult['integrity'] = 'b594924588d873f60df054a64a7bfaa1d4196ab1d2000f1788a453c1765b05b8'
        expectedResult['status'] = 'ok'
        actualResult = sudoku._create(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_040TestCreatingGridWithLevel4(self):
        parms = {}
        parms['level'] = 4
        expectedResult = {}
        expectedResult['grid'] = [0, -6, -7, 0, -2, 0, 0, 0, -3, 0, -8, 0, -7, 0, -3, 0, 0, -6, -1, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -3, 0, 0, 0, -8, -8, 0, 0, 0, -4, 0, 0, 0, -1, -4, 0, 0, 0, -6, 0, 0, -5, 0, -3, 0, 0, 0, 0, 0, 0, 0, -2, -6, 0, 0, -2, 0, -4, 0, -3, 0, -5, 0, 0, 0, -9, 0, -8, -4, 0]
        expectedResult['integrity'] = '0ea83ad27c27241477102e2377f1bb14cc2f8c6125fbc85fab972c9ab0661319'
        expectedResult['status'] = 'ok'
        actualResult = sudoku._create(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_050TestCreatingGridWithLevel5(self):
        parms = {}
        parms['level'] = 5
        expectedResult = {}
        expectedResult['grid'] = [-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0]
        expectedResult['integrity'] = '110a79143bc7c2b66faff5e8fe895320d402e4f91dbbe6b969931228abb84242'
        expectedResult['status'] = 'ok'
        actualResult = sudoku._create(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_060TestCreatingGridWithDefaultLevel(self):
        parms = {}
        expectedResult = {}
        expectedResult['grid'] = [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, -1, -7, 0, -5, 0, 0]
        expectedResult['integrity'] = 'b594924588d873f60df054a64a7bfaa1d4196ab1d2000f1788a453c1765b05b8'
        expectedResult['status'] = 'ok'
        actualResult = sudoku._create(parms)
        self.assertEqual(expectedResult, actualResult)
        
    # Sad path
    #    1) level less than 1
    #    2) level greater than 5
    #    3) level is a string
    #    4) level is a float
    #    5) level is None
    #    6) level value is missing
    
    def test100_910TestWithLevel0(self):
        parms = {}
        parms['level'] = 0
        expectedResult = {}
        expectedResult['status'] = 'error: invalid level'
        actualResult = sudoku._create(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_920TestWithLevel6(self):
        parms = {}
        parms['level'] = 6
        expectedResult = {}
        expectedResult['status'] = 'error: invalid level'
        actualResult = sudoku._create(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_930TestWithStringLevel(self):
        parms = {}
        parms['level'] = "two"
        expectedResult = {}
        expectedResult['status'] = 'error: invalid level'
        actualResult = sudoku._create(parms)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_940TestWithFloatLevel(self):
        parms = {}
        parms['level'] = 2.0
        expectedResult = {}
        expectedResult['status'] = 'error: invalid level'
        actualResult = sudoku._create(parms)
        self.assertEqual(expectedResult, actualResult)