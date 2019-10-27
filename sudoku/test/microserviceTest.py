from unittest import TestCase
import http.client
from urllib.parse import urlencode
import json
import sudoku.dispatch as sudoku 
from unittest.case import skip

class MicroserviceTest(TestCase):
    def setUp(self):
        self.PATH = '/sudoku?'
        self.PORT = 5000
        self.URL = 'localhost'
        
    def microservice(self, parm = ""):
        '''Issue HTTP Get and return result, which will be JSON string'''
        try:
            theParm = urlencode(parm)
            theConnection = http.client.HTTPConnection(self.URL, self.PORT)
            theConnection.request("GET", self.PATH + theParm)
            theStringResponse = str(theConnection.getresponse().read(), "utf-8")
        except Exception as e:
            theStringResponse = "{'diagnostic': '" + str(e) + "'}"
            
        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = theStringResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if(isinstance(unicodeDictionary[element], str)):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result
        
# Happy path
#    Test that each dispatched operation returns a status element
    @skip
    def test100_010ShouldVerifyInstallOfCreate(self):
        parms = {}
        parms['op'] = 'create'
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertIn('create', result['status'])
    @skip
    def test100_020ShouldVerifyInstallOfInsert(self):
        parms = {}
        parms['op'] = 'insert'
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertIn('insert', result['status'])
        
    def test100_030ShouldVerifyInstallOfIsdone(self):
        parms = {}
        parms['op'] = 'isdone'
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertIn('isdone', result['status'])
        
    def test100_040ShouldVerifyInstallOfSolve(self):
        parms = {}
        parms['op'] = 'solve'
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertIn('solve', result['status'])
        
# Sad path
#    Verify status of 
#        1) missing parm
#        2) non-dict parm
#        3) missing "op" keyword
#        4) empty "op" keyword
#        5) invalid op name

    def test100_910ShouldErrOnMissingParm(self):
        result = self.microservice()
        self.assertIn('status', result)
        self.assertEquals(result['status'], sudoku.ERROR01)
        
    def test100_920ShouldErrOnNoOp(self):
        parms = {}
        parms['level'] = 3
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertEquals(result['status'], sudoku.ERROR01)
                
    def test100_930ShouldErrOnEmptyOp(self):
        parms = {}
        parms['op'] = ''
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertEquals(result['status'], sudoku.ERROR03)
        
    def test100_940ShouldErrOnUnknownOp(self):
        parms = {}
        parms['op'] = 'nop'
        result = self.microservice(parms)
        self.assertIn('status', result)
        self.assertEquals(result['status'], sudoku.ERROR03)
        
    # Acceptance tests for _create
    #
    # Sad path analysis:
    #    test200_910: level LT 1
    #    test200_920: level GT 5
    #    test200_930: level value is a string
    #    test200_940: level value is a float
    #    test200_950: empty level value
    def test200_910ShouldErrOnLevelLT1(self):
        parms = {'level':"0"}
        parms['op'] = 'create'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test200_920ShouldErrOnLevelGT5(self):
        parms = {'level':"6"}
        parms['op'] = 'create'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test200_920ShouldErrWhenLevelIsString(self):
        parms = {'level':"five"}
        parms['op'] = 'create'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test200_930ShouldErrWhenLevelIsFloat(self):
        parms = {'level':"3.0"}
        parms['op'] = 'create'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test200_940ShouldErrWhenLevelIsEmpty(self):
        parms = {'level':""}
        parms['op'] = 'create'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    # Happy path analysis:
    #    test200_100 valid level 1 grid
    #    test200_110 valid level 2 grid
    #    test200_120 valid level 3 grid
    #    test200_130 valid level 4 grid
    #    test200_140 valid level 5 grid
    #    test200_150 default grid
    def test200_100ShouldReturnLevel1Grid(self):
        level1Grid = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms = {'level' : "1"}
        parms['op'] = 'create'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 3)
        self.assertEqual(level1Grid, actualResult['grid'])
        
    def test200_110ShouldReturnLevel2Grid(self):
        level2Grid = [0, -3, 0, 0, 0, -2, 0, -6, -5, -5, -8, 0, -1, -3, -4, 0, -2, 
                  -9, 0, -2, -7, 0, -5, 0, 0, 0, -1, 0, 0, -2, 0, 0, -9, 0, -1, 
                  -3, -8, -5, -9, 0, -7, -1, 0, -4, -2, -1, 0, 0, -6, -2, 0, 0, 
                  0, -7, 0, 0, 0, 0, -4, -7, -2, -5, 0, -6, -7, -5, 0, 0, -8, 0, 
                  -9, 0, 0, -9, -4, -5, -6, 0, 0, -7, -8]
        parms = {'level' : "2"}
        parms['op'] = 'create'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 3)
        self.assertEqual(level2Grid, actualResult['grid'])
        
    def test200_120ShouldReturnLevel3Grid(self):
        level3Grid = [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 
                  0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, 
                  -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, 
                  -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, 
                  -1, -7, 0, -5, 0, 0]
        parms = {'level' : "3"}
        parms['op'] = 'create'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 3)
        self.assertEqual(level3Grid, actualResult['grid'])
        
    def test200_130ShouldReturnLevel4Grid(self):
        level4Grid = [0, -6, -7, 0, -2, 0, 0, 0, -3, 0, -8, 0, -7, 0, -3, 0, 0, -6, -1, 
                  0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -3, 0, 0, 0, -8, -8, 0, 0, 0, 
                  -4, 0, 0, 0, -1, -4, 0, 0, 0, -6, 0, 0, -5, 0, -3, 0, 0, 0, 0, 0, 0, 
                  0, -2, -6, 0, 0, -2, 0, -4, 0, -3, 0, -5, 0, 0, 0, -9, 0, -8, -4, 0]
        parms = {'level' : "4"}
        parms['op'] = 'create'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 3)
        self.assertEqual(level4Grid, actualResult['grid'])
        
    def test200_140ShouldReturnLevel5Grid(self):
        level5Grid = [-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 
                  0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0,
                   0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, 
                   -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0]
        parms = {'level' : "5"}
        parms['op'] = 'create'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 3)
        self.assertEqual(level5Grid, actualResult['grid'])
        
    def test200_150ShouldReturnDefaultLevel3Grid(self):
        level3Grid = [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 
                  0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, 
                  -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, 
                  -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, 
                  -1, -7, 0, -5, 0, 0]
        parms = {}
        parms['op'] = 'create'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 3)
        self.assertEqual(level3Grid, actualResult['grid'])
        
    # Acceptance tests for _insert
    #
    # Sad path analysis:
    #    test300_900 test with invalid length for cell
    #    test300_910 test with row value LT 1
    #    test300_920 test with column value LT 1
    #    test300_930 test with invalid cell string
    #    test300_940 test with invalid cell string
    #    test300_950 test with invalid cell string
    #    test300_960 test with invalid cell string
    #    test300_970 test with missing cell parm
    #    test300_980 test with empty cell string
    #    test300_990 test inserting value LT 1
    #    test300_901 test inserting value GT 9
    #    test300_911 test inserting empty value
    #    test300_921 test inserting string value
    #    test300_931 test inserting float value
    #    test300_941 test inserting with missing grid
    #
    
    def test300_900ShouldErrWhenCellStringLengthIsNotFour(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = "r3c22"
        parms['value'] = "3"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_910ShouldErrWhenRowValueLT1(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = "r0c2"
        parms['value'] = "3"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_920ShouldErrWhenColumnValueLT1(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = "r3c0"
        parms['value'] = "3"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_930ShouldErrWhenFirstCharInCellStringIsNotR(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = "e3c2"
        parms['value'] = "3"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_940ShouldErrWhenThirdCharInCellStringIsNotC(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = "r332"
        parms['value'] = "3"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_950ShouldErrWhenSecondCharInCellStringIsNotAnInt(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = "rrc2"
        parms['value'] = "3"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_960ShouldErrWhenFourthCharInCellStringIsNotAnInt(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = "r2c "
        parms['value'] = "3"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_970ShouldErrWhenCellParmIsMissing(self):
        parms = {}
        parms['op'] = 'insert'
        parms['value'] = "3"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_980ShouldErrWhenCellIsEmptyString(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = ""
        parms['value'] = "3"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_990ShouldErrWhenValueIsLT1(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = "r1c3"
        parms['value'] = "0"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_901ShouldErrWhenValueIsGT9(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = "r1c3"
        parms['value'] = "10"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_911ShouldErrWhenValueIsEmpty(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = "r1c3"
        parms['value'] = ""
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')
        
    def test300_921ShouldErrWhenValueIsString(self):
        parms = {}
        parms['op'] = 'insert'
        parms['cell'] = "r1c3"
        parms['value'] = "one"
        parms['grid'] = [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, 
                  -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 
                  0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, 
                  -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, 
                  -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0]
        parms['integrity'] = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
        actualResult = self.microservice(parms)
        self.assertEqual(len(actualResult), 1)
        self.assertIn(actualResult['status'][0:5], 'error:')