#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
'''
函数一旦有return 就不再往下执行了。

传递参数的时候
普通参数
默认参数 #！！！默认参数必须要放在参数列表的后面
指定参数 # 实际参数赋值的时候指定的刑事参数
动态参数
    * 默认将传入的参数，全部放置在元祖中，
    ** # 默认将传入的参数，全部放置在字典中，2个*传值的时候必须是指定参数 ，是一个字典
万能参数
def foo(*args,**kwargs):

'''

# 动态参数
# 4：*参数
# def foo(*args):
#     print(args,type(args))
a=[1, 2, 3, 4, 5, 6,1237]
# foo(a)
def foo(*kwargs):
    print(kwargs)
foo(a) #类型为元祖，把整个列表作为元祖的一个元素执行 ([1, 2, 3, 4, 5, 6, 1237],)
foo(*a) #类型为元素，但是把列表转换成元祖 (1, 2, 3, 4, 5, 6, 1237)

def foo(**kwargs):
    print(kwargs)

foo(a=1)
a={'a':1,'b':2}
foo(a=a) #{'a': {'b': 2, 'a': 1}}
foo(**a) #{'b': 2, 'a': 1} 相当于直接赋值


print("万能参数")
def foo(*args, **kwargs): #一定是一个*在前面
    print(args)
    print(kwargs)

foo(11,23,21,1,45,25,1,**a)

#format args ** args 用法
a= " {name} is my name i am {age} old "
dd = {'name':'zhoutao','age':18}
print(a.format(**dd))


name = 'zhoutao' #全局变量
def f1():
    age=18
    global name  #对全局变量重新赋值服药使用global
    name = '123'
    print(age,name)
def f2():
    age = 18
    print(age,name)

f1()
f2()

name = [11,22,33]
def f1():
    print(name)
    name.append(44)
    print(name)

f1()

#全局变量，所以作用域都可读
#对全局变量进行【ch重新赋值】，需要global
#特殊：列表，字典，可修改，不可重新赋值
