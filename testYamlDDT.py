#coding:utf-8

import unittest
from ddt import ddt,file_data,unpack,data
import os
import time
import HTMLTestRunner

@ddt
class mytest(unittest.TestCase):
    
    @file_data('data.yaml')
    @unpack
    def test_case_01(self,*args, **kwargs):
        print(kwargs['userName'])
        print(kwargs['userPwd'])
        print(kwargs['code'])
        self.assertEqual(kwargs['aget'], 1)
        
if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    localpath = os.getcwd()
    print('本文件目录位置：'+localpath)
    filepath = os.path.join(localpath,'Report',now +'.html')
    print('报告存放路径  ：'+filepath)
    
    ts = unittest.TestSuite()#实例化
    #按类加载全部testxxx测试用例
    ts.addTest(unittest.TestLoader().loadTestsFromTestCase(mytest))
    #按函数加载testxxx测试用例
    #ts.addTest(HtmlReport('test_1'))
    #打开文件位置，如果没有则新建一个文件
    filename = open(filepath,'wb')
    htmlroport = HTMLTestRunner.HTMLTestRunner(stream=filename,title='标题XXX报告',description='XXX报告XX描述')
    htmlroport.run(ts)