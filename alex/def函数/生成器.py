#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

#
# li = [11,22,33,44]
# resurt = filter(lambda x: x> 22,li)
# print(resurt) #具有生成指定条件数据能力的对象
#
# for  i in resurt: #只有循环的时候去生成
#     print(i)

def f1():
    print("F1")

def func():
    yield 1
    yield 2
    yield f1

ret = func()

for i in ret:
    print(i)

print("___________")
# def myrange(arg):
#     start = 0
#     while True:
#         if start > 10:
#             return
#         yield start
#         start += 1
#
# ret = myrange(10)
# print(ret)
#
# for i in ret:
#     print(i)