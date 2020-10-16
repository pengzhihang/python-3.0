#coding:utf-8

with open('d:\\test\\test.txt','r',encoding='utf-8') as fs:
    print(fs.read()) 


# from concurrent.futures import thread,process
# 
# import time
# 
# import threading
# 
# t1=thread.ThreadPoolExecutor(100)
#  
# t2=process.ProcessPoolExecutor(2)
# 
# def sayhello(ages):
#     print(ages)
#     time.sleep(5)
#     print(ages)
# 
# tests=[]
# 
# for i in range(5):
# #     tt=threading.Thread(target=sayhello, args='i')
# #     tests.append(tt)
#     t2.submit(sayhello,'aa')
#     
# # print(len(tests))  
# # 
# # for i in tests:
# #     i.setDaemon(True)
# #     i.start()
# # i.join()
# #  
# 
# #      
# #     t2.submit(sayhello('aa'))
