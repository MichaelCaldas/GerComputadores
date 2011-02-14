'''
Created on 13/02/2011

@author: Michael
'''
import unittest
from Micro import Micro
from should_dsl.dsl import should
from should_dsl.matchers import be

class Test_Micro(unittest.TestCase):

    def setUp(self):
        self.micro = Micro("001", "Micro ultra veloz", 500, 4)
        self.micro.codPatrimonio |should| be("001")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()