#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/8/11:17
# Python 3.5

import queue

# q=queue.Queue(3) #10表示队列总长度为10，最多接受10个数据
# print(q.empty())
# q.put(11)
# q.put(13,timeout=1,block=False)
# q.put(14,timeout=1,block=False)
# print(q.empty())#放的超时时间，最多等1秒，放不去就保存,#设置成block=False,不在阻塞，表示忽略等待时间，只要队列没有位置则报错
# print(q.full())
# q.get()
# q.get(block=True,timeout=1)
#put放数据
#get取数据
#qsize 当前队列长队

q=queue.Queue(5)
q.put(11)
q.put(13)
q.put(14)
q.get()
q.task_done() #任务取到，告诉队列，任务已经取到，完成
q.get()
q.task_done() #任务取到，告诉队列，任务已经取到，完成
q.get()
q.task_done() #任务取到，告诉队列，任务已经取到，完成
q.join() #如果队列中的任务没有被拿则阻塞等待，
#join,task_done#阻塞进程，当队列中任务执行完毕，不在阻塞

