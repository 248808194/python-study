#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/8/18:23
# Python 3.5

# from multiprocessing import  Process
#
# def foo(i):
#     print(i,"hello world")
#
# if __name__ == "__main__":
#     for i in range(10):
#         p = Process(target=foo,args=(i,))
#         p.start()
#         p.join()


#进程之间的数据共享，默认不能

# from multiprocessing import  Process
# from  multiprocessing import queues #特殊的queue #实现进程间数据共享
# import  multiprocessing
#
#
# def foo(i,arg):
#     arg.put(i)
#     print(i,"hello world",arg.qsize()) #将iput到li这个队列中去，
#
# if __name__ == "__main__":
#     li=queues.Queue(ctx=multiprocessing)
#     for i in range(10):
#         p = Process(target=foo,args=(i,li))
#         p.start()
#         p.join()

#进程之间的数据共享，默认不能

# from multiprocessing import  Process
# from  multiprocessing import queues #特殊的queue #实现进程间数据共享
# from multiprocessing import  Array #类似java中的数组
#
#
# def foo(i,arg):
#     arg[i] = i+100
#     for item in arg:
#         print(item)
#     print("=========")
#
# if __name__ == "__main__":
#     li = Array("i",10) #指定类型，，且开辟内存空间
#     for i in range(10):
#         p = Process(target=foo,args=(i,li))
#         p.start()
#         p.join()

from multiprocessing import  Process
from  multiprocessing import queues #特殊的queue #实现进程间数据共享
from multiprocessing import  Manager
# import multiprocessing
from multiprocessing import  RLock
import time


def foo(i,lock):
    lock.acquire()
    print(i)
    time.sleep(1)
    lock.release()

if __name__ == "__main__":
    lock = RLock()
    for i in range(10):
        p = Process(target=foo,args=(i,lock,))
        p.start()
        p.join()