#coding:utf-8

'''
Created on 2020-10-13

@author: ZHQC-041
'''
# import requests
# import json
# 
# with open('d:\\test\\test.txt','r',encoding='utf-8') as fs:
#     print(fs.read())
import requests
import threading
import json

rq=requests.get('http://c.m.163.com/nc/article/headline/T1348647853363/0-20.html')
   
getS=json.loads(rq.content)

print(getS)
   
for i in getS['T1348647853363'][1:]:
    if i.haskeys('votecount'):
        print ('标题:%s'.decode('utf-8')%i['title'])
        print ('地址:%s'.decode('utf-8')%i['url'])
        print ('</br>')