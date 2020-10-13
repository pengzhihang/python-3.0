#coding:utf-8

'''
Created on 2020-10-13

@author: ZHQC-041
'''

import unittest

class MyClass(unittest.TestCase):
    '''
    classdocs
    '''
    def test_login(self):
        self.assertEqual(1, 2)
        
    def test_order(self):
        self.assertEqual( 2, 3)
        
if __name__ == "__main__":
    unittest.main()
