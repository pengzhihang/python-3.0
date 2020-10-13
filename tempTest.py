#coding:utf-8

'''
Created on 2020-10-12

@author: ZHQC-041

'''
import requests
import os,sys
import json



rg=requests.get('http://www.baidu.com')

print(rg.content)

a={'aaa':123,'bbb':'bbb','ccc':['a','b','c',1,2,3]}

b=json.dumps(a)

print(b)

print(os.name)
