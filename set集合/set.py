#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

#使用set()来创建一个集合

empty_set = set()
print(empty_set)
#与字典一样，集合是无序的


###!!!###!!!你可以利用已有列表、字符串、元组或字典的内容来创建集合

print("字符串创建集合")
a=set('zhoutao')
print(a)
print(type(a))

print("列表创建集合")
a=set([1,2,3,4,5])
print(a)
print(type(a))

print("元祖创建集合")
a=set(('a','b','c',1,2,3))
print(a)
print(type(a))

print("当字典作为参数传入的时候只有键会被使用")

a=set({'a':1,'b':2,'c':3})
print(a)
print(type(a))