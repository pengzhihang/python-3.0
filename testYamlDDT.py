#coding:utf-8

import unittest
from ddt import ddt,file_data,unpack,data

@ddt
class mytest(unittest.TestCase):
    
#     @file_data('data.yaml')
    
    
    @data(1,2,3,4,5,6)
    @unpack
    def test_case_01(self,*args, **kwargs):
        print(kwargs)
#         print(kwargs['userName'])
#         print(kwargs['userPwd'])
#         print(kwargs['code'])
#         self.assertEqual(kwargs['aget'], 1)
        
if __name__ == "__main__":
    unittest.main()