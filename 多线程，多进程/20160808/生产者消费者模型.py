#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/8/13:34
# Python 3.5

import queue,threading,time
q=queue.Queue(10)
def productor(arg): #创建包子
    while True:
        q.put(str(arg)+"包子")

def consumer(arg): #创建消费者
    while True:
       print("消费者%s"%arg,q.get())
       time.sleep(1)

for i in range(9):#创建厨师
    t=threading.Thread(target=productor,args=(i,))
    t.start()

for j in range(20):#
    t=threading.Thread(target=consumer,args=(j,))
    t.start()

