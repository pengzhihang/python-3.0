#coding:utf-8

'''
Created on 2020-10-12

@author: ZHQC-041
'''

import yaml

fs=open('data.yaml')

datas=yaml.load(fs, Loader=yaml.FullLoader)

print(type(datas))

print(datas)

