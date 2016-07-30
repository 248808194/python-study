#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from multiprocessing import Process
from multiprocessing import queues
from multiprocessing import Array
from multiprocessing import RLock, Lock, Event, Condition, Semaphore
import multiprocessing
import time

def foo(i,lis,LOCK):
    LOCK.acquire()
    lis[0] = lis[0] - 1
    time.sleep(1)
    print('say hi',lis[0])
    LOCK.release()


if __name__ == "__main__":
    LOCK =RLock()

    li = Array('i', 1) #特殊的数据结构，数组，让进程之间能够数据共享
    li[0] = 10 #定义数组第0个元素等于10
    for i in range(10):
        p = Process(target=foo,args=(i,li,LOCK))
        p.start()