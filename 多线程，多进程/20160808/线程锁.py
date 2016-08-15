#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/8/14:35
# Python 3.5
#
# import threading,time
#
# NUM=10
# def foo():
#     global NUM
#     NUM -=1
#     time.sleep(1)
#     print(NUM)
#
#
# for i in range(10):
#     t=threading.Thread(target=foo)
#     t.start()

#无锁状态，下，多线程一次性执行10次foo，NUM值最后是0，因为线程都来让num 自减1，



# import threading,time
#
# NUM=10
# def foo(l):
#     global NUM
#
#     l.acquire()
#     NUM -=1
#     print(NUM)
#     #解锁
#     l.release()
#
# lock = threading.RLock()
# print(type(lock))
# for i in range(10):
#     t=threading.Thread(target=foo,args=(lock,))
#     t.start()
#定义一个lock对象等于threading.Lock()这个类，将这个对象传递到foo函数中，执行lock的acquire方法和release方法加锁，解锁，一个进程进来先锁定 原子性操作，操作完成后在解锁


# import threading,time
#
#
# def foo(i,e):
#     print(i)
#     e.wait() #当e.wait()的时候，想象成红灯，
#     print(i+100)
#
# event = threading.Event()
# for i in range(10):
#     t=threading.Thread(target=foo,args=(i,event))
#     t.start()
# event.clear() #event.clear()让程序停止等待绿灯
# inp = input("enter 1:")
# if inp == "1":
#     event.set()  #绿灯放行
# """
# 执行步骤
#     1: loading foo函数
#     2：执行多线程，每个线程执行print(i)函数，执行完毕遇到wait红灯等待
#     3：执行event.clear()程序停止等待
#     4：执行event.set() 绿灯放行执行print (i+100)操作
# """

#
# import  threading,time
#
# def foo(i,s):
#     s.acquire()
#     time.sleep(1)
#     print(i)
#     s.release()
#
# semaphore = threading.Semaphore(3)
# semaphore.acquire()
# for i in range(10):
#     t=threading.Thread(target=foo,args=(i,semaphore))
#     t.start()


#条件


# import  threading
# def condition():
#     ret = False
#     inp = input(">>>:")
#     if inp == "True":
#         ret = True
#     else:
#         ret == 'False'
#     return  ret
#
#
# def foo(i,c):
#     print(i)
#     c.acquire()
#     c.wait_for(condition) #waoiit_for的值为True 就继续执行#这里特别说明condition没有加()来执行函数，因为threading源码里面加了()去执行wait_for传入的函数
#     print(i+100)
#     c.release()
#
# c=threading.Condition()
# for i in range(10):
#     t=threading.Thread(target=foo,args=(i,c,))
#     t.start()
#
# """
# 执行步骤
#     1：定义foo函数，传入i,c;i为for循环的i值，c为吊桶threading.Condtion()这个对象
#     2：执行10次线程，
#     3：遇到acquire(),wait()阻塞线程，等待用户输入，当inp=n的时候，意味着就是放n个线程
# """


from threading import Timer

def foo():
    print("hello world")


t=Timer(1,foo) #等待1秒在执行线程
t.start()