#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

print('''
元组是不可改
变的，这意味着一但元组被定义，将无法再进行增加、删除或修改元素等
''')

#创建空列表
a=tuple()
print (a)
print(type(a))

#一次将元组赋值给多个变量：
marx_tuple = 'Groucho','Chico','Harpo'
print(marx_tuple)
print(type(marx_tuple))

a,b,c=marx_tuple
for i in (a,b,c):
    print(i)

# Groucho
# Chico
# Harpo