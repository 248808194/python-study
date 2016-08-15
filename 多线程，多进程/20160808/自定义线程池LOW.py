#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/8/16:52
# Python 3.5

import queue
import threading
import time
from  multiprocessing
class Mythreadpool:
    """
    init构造方法定义最大长度为maxsize的队列，默认值为5，让队列放上threading.Thread 这个类
    """
    def __init__(self,maxsize=5):
        self.maxsize = maxsize
        self.q = queue.Queue(maxsize)
        for i in range(maxsize):
            self.q.put(threading.Thread)

    def getthread(self): #定义getthread方法，获取一个threading.Thread类
        return self.q.get(threading.Thread) #return的是一个threading.Thread类

    def addthread(self):
        self.q.put(threading.Thread) #定义addthread方法，往队列中放一个threading.Thread类


def task_get(i,tpool):
    print(i)
    time.sleep(1)
    tpool.addthread() #秉承线程执行完毕交还线程原则，程序执行完毕需要往队列中增加threading.Thread类

tpool = Mythreadpool(5)

for i in range(100):
    t=tpool.getthread() #定义t对象获取threading.Thread类，一次获取5个队列
    obj = t(target= task_get,args=(i,tpool))
    obj.start() #通过线程执行task_get函数


