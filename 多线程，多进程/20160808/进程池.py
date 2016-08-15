#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/8/22:57

import time
from multiprocessing import Pool
#默认5个进程

def f1(arg):
    time.sleep(0.1)
    print(arg)

if __name__ == "__main__":
    pool = Pool(5)
    for i in range(30):
        pool.apply(func=f1,args=(i,)) #apply串型操作，一个进程执行完了，在执行另外一个进程

import time
from multiprocessing import Pool
#默认5个进程

def f1(arg):
    time.sleep(0.1)
    print(arg)

if __name__ == "__main__":
    pool = Pool(5)
    for i in range(30):
        pool.apply_async(func=f1,args=(i,))#apply异步方式
    # pool.close() #所有任务执行完毕，如果不加close会主动抛出一个断言错误
    time.sleep(0.5)
    pool.terminate() #当前已经在执行的任务执行完毕
    pool.join()
    print("end")