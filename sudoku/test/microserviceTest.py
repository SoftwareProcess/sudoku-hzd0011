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
        