'''
Created on 2020-10-16

@author: ZHQC-041
'''
import unittest
from ddt import ddt,data,file_data

@ddt
class Test_First(unittest.TestCase):

    @file_data('../datas/first.yml')
    def testName(self,*args, **kwargs):
        print(kwargs['userName'])
        print(kwargs['passWD'])
        print(kwargs['code'])
        self.assertEqual(kwargs['code'],1111)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()