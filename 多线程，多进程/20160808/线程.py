#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/8/10:13
# Python 3.5
#
# def f1(bar):
#     print(bar)
#
#
# import threading
# t=threading.Thread(target=f1,args=(123,)) #创建线程，需要先import threading这个模块，创建t这个对象，让target=需要使用线程的对象，如果target下需要传递参数，则args= 参数
# t.start() #不代表当前线程会被立即执行，

#主线程需要等待子线程执行完毕






#主线程执行完毕可以不等待，t.close()
#t.setDaemon(True)不等待子线程执行完毕
#t.join（）执行到join主线程停住，等待子线程执行完毕继续往下走 可以加上秒参数

import  threading
class Mythread(threading.Thread):
    """
    自定义一个类，继承thraading.Thread这个类，
    执行自己的构造方法前先super执行父类的构造方法，
    自己的构造方法，传递一个函数，传递一个参数
    程序往下执行自己的run方法

    """
    def __init__(self,func,args):
        self.func = func
        self.args = args
        super(Mythread,self).__init__()

    def run(self):
        self.func(self.args)


def f1(arg):
    print(arg)

t=Mythread(f1,123)
t.start()
