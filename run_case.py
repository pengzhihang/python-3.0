#coding:utf-8

'''
Created on 2020-10-15

@author: ZHQC-041
'''

import unittest
from common import HTMLTestRunnerNew
import os
from concurrent.futures import thread,process,Executor

# 获取路径# 当前脚本所在目录
curpath = os.path.dirname(os.path.realpath(__file__))
#测试用例路径
casepath = os.path.join(curpath, "cases")
#测试报告路径
reportpath = os.path.join(curpath, "reports")


def add_case(case_path=casepath, rule="test*.py"):

    '''加载所有的测试用例'''

    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule,top_level_dir=None)
    return discover


def run_case(all_case, report_path=reportpath, nth=0):

    '''执行所有的用例, 并把结果写入测试报告'''

    report_abspath = os.path.join(report_path, "result%s.html"%nth)

    with open(report_abspath, "wb+") as file:

        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title=u'自动化测试报告,测试结果如下：',description=u'用例执行情况：')
        # 调用add_case函数返回值
        runner.run(all_case)


if __name__ == "__main__":
    
    ts=thread.ThreadPoolExecutor(1000)
    # 用例集合
    cases = add_case()
    # 之前是批量执行，这里改成for循环执行
    for i, j in zip(cases, range(len(list(cases)))):
        ts.map(run_case(i, nth=j))
#         run_case(i, nth=j)  # 执行用例，生成报告
        # print(i,j)