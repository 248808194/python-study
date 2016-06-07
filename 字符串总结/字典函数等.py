#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

#使用dict()转换为字典

lol = [['a','b'],['c','d'],['e','f']] #大列表中框一个小列表
a=dict(lol)
print(a)

#包含双值元组的列表：
lot = [('a','b'),('c','d'),('e','f')]
b=dict(lot)
print(b)

#双字符的字符串组成的列表：
los = ['ab','cd','ef']
c=dict(los)
print(c)

#列表元祖，字符串，都可以通过dict变成字典

#使用[key]添加或修改元素

a={'a': 'b', 'c': 'd', 'e': 'f'}
#添加进字典
a['z']='w'
print(a) #{'c': 'd', 'e': 'f', 'a': 'b', 'z': 'w'}
#修改字典

a['z']='W+'
print(a) #{'a': 'b', 'z': 'W+', 'c': 'd', 'e': 'f'}


#合并字典
AA={'a': 'b', 'c': 'd', 'e': 'f'}
BB={'1': '2', '3': '4', '5': '6', '7': '10'}
AA.update(BB)
print(AA) #{'c': 'd', '7': '10', 'e': 'f', 'a': 'b', '3': '4', '5': '6', '1': '2'}

#del删除具有制定键的元素
del AA['c']
print(AA) #{'1': '2', '3': '4', 'e': 'f', '5': '6', 'a': 'b', '7': '10'}
AA.clear()
print(AA)

#使用keys()获取所有键
number = { 'a':'1','b':'2','c':'3' }
print(number.keys()) #dict_keys(['a', 'c', 'b'])
a=list(number.keys()) #在python3中，你只能自己调用list()将dict_keys()转换为列表类型。
print(a)
#使用values()获取所有值
print(number.values())
a=list(number.values()) #dict_values(['1', '3', '2'])
print(a) #['1', '3', '2']

#使用items()获取所有键值对

print(number.items())
a=list(number.items()) #dict_items([('c', '3'), ('a', '1'), ('b', '2')])
print(a) #[('c', '3'), ('a', '1'), ('b', '2')]


#使用=赋值另外一个字典，修改其中一个字典，原来会更改，。使用copy()赋值不会出现这个情况
a={'1': '2', '3': '4', 'e': 'f', '5': '6', 'a': 'b', '7': '10'}
b=a
a['zhoutao']=123
print(a)
print(b)

#copy
a={'1': '2', '3': '4', 'e': 'f', '5': '6', 'a': 'b', '7': '10'}
b=a.copy()
a['zhoutao']=123
print(a) #{'3': '4', '1': '2', '5': '6', '7': '10', 'zhoutao': 123, 'e': 'f', 'a': 'b'}
print(b) #{'3': '4', '1': '2', '5': '6', '7': '10', 'e': 'f', 'a': 'b'}

#pop 函数
#如果字典中key 键存在，删除并返回dict[key]，
#如果key 键不存在，且没有给出default 的值，引发KeyError 异常。
a={'1': '2', '3': '4', 'e': 'f', '5': '6', 'a': 'b', '7': '10'}
print(a)
a.pop('123')
print(a)

#方法set()相似，如果字典中不存在key 键，由dict[key]=default 为它赋值。


{'1': 3.1415920000000002, 1: 'abc', 3.2000000000000002: 'xyz'}
dict2.setdefault('a','a123')
{'1': 3.1415920000000002, 1: 'abc', 'a': 'a123', 3.2000000000000002: 'xyz'}

