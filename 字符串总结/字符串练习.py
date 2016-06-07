#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
import string
a=string.ascii_lowercase
print(a) #abcdefghijklmnopqrstuvwxyz
print(a.find('a',0,10))
print(a.find('a',1,10)) #可指范围查找子串，返回索引值，否则返回-1
print(a.rfind('a',0,10)) #反向查找
print(a.index('a')) #同find，只是找不到产生ValueError异常
print(a.rindex('a'))#同上反向查找
print(a.count("a"),'123')

b=string.ascii_uppercase
print(b)
print(b.lower())#lower转小写
print(a.upper()) #uper转大写
a='ABCabcDEFdef'
print(a.swapcase()) #abcABCdefDEF

#S.split(str, ' ')   #将string转list，以空格切分
#S.join(list, ' ')   #将list转string，以空格连接
b=list(a)
print(b)
print(a.split())  #将string转list，以空格切分
a.join(' ') ##将list转string，以空格连接
print(a)
print(type(a))