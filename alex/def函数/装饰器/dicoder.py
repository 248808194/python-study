#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

#def outer(func):.....
#@outer #自动执行outer函数，并且将其下面的函数名f1当作参数传递。
#def f1()


#
# outer()

# def outer(func):
#     print("123",func)
# @outer
# #功能1：自动执行outer函数，并且将其下面的函数名f1当作参数传递。
# def f1():
#     print("F1")
#
# def outer(func):
#     return "111"
# @outer
# #功能2：将outer函数的返回值，重新赋值给f1
#
# #记住，一旦一个函数被装饰器装饰，其实就是被装饰的函数被重新赋值为装饰器的内部(内层)函数
# def f1():
#     print("F1")
def outer(func):
    def inner(*args,**kwargs):
        print("before")
        r= func(*args,**kwargs)
        print("after")
        return r
    return inner
@outer
def f1(arg):
    print("f1",arg)
    return "cut you"
#记住，一旦一个函数被装饰器装饰，其实就是被装饰的函数被重新赋值为装饰器的内部(内层)函数z
a=f1("ffff")
print(a)
#第一步28，第二步34，第三步，29，第四步，33
#执行f1()的时候，第一步30，第二步，31，第三步，36，第四步32



# @装饰器函数名
# def func():
#     pass
#1:将func当作参数传递给装饰器函数，并执行
#2：将装饰器函数的返回值重新赋值给func

