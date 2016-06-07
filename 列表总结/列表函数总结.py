#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#extend()可以将一个列表合并到另一个列表中：
print()
#写法3
a=[123]
b=[456]
a.extend(b)
print(a)
#写法2
a=[123]
b=[456]
a=a+b
print(a)
#写法1
a=[123]
b=[456]
a+=b
print(a)

#insert()使用insert()在指定位置插入元素
a=[0,1,2,3,5,6,7,8,9]
a.insert(4,'4') #在第4位插入4这个字符
print(a)
#del删除指定位置的元素
# del是Python语句，而不是列表的方法，无法通过Devp[3].del进行调用
Dev = ['Python','Java','PHP','Go','C']
del Dev[1]
print(Dev)

#更新列表
list1=[1,2,3,4,5]
list1.append(6)
print(list1)
#使用remove()删除具有指定值的元素
a=[0,1,2,3,5,6,7,8,9]
a.remove(0)
print(a) #[1, 2, 3, 5, 6, 7, 8, 9]
#count 统计元素在列表中出现的次数
a=[0,1,2,3,5,6,7,8,9,9,9,9,9,1,1,1]
c=a.count(9)
print (c) #9出现5次
#使用pop()获取并删除指定位置的元素
a=[0,1,2,3,5,6,7,8,9]
a.pop() #不加默认最后一位-1
print(a)
a=[0,1,2,3,5,6,7,8,9]
a.pop(-1)
print(a)
a.pop(0)
print(a)
#使用index()查询具有特定值得元素位置
a=[0,1,2,3,5,6,7,8,9]
b=a.index(0)
print(b) #0的位置在第0个

#判断列表是否存在
a=[0,1,2,3,5,6,7,8,9]
print(0 in a)
print('0' in a)
#使用join()转换为字符串

a=['Python','Java','PHP','Go','C']#注意不能有数字
b=','.join(a)
print(b)
print(type(b))
#、使用sort()重新排序元素
# 列表方法sort()会对元列表进行排序，改变元列表内容；
# 通用函数sorted()则会返回排好序的列表副本，元列表内容不变；
a=[912,465,45734,32456435,767,0,1,3,1,34,65] # 列表方法sort()会对元列表进行排序，改变元列表内容；
a.sort()
print(a)
a=[912,465,45734,32456435,767,0,1,3,1,34,65] #通用函数sorted()则会返回排好序的列表副本，元列表内容不变；
b=sorted(a)
print(b)
print(a)

#、使用len()获取长度
a=[912,465,45734,32456435,767,0,1,3,1,34,65]
print(len(a))

#使用=赋值，使用copy()赋值
# 通过下面任意一种方法，都可以将一个列表的值赋值给另一个新的列表中：
a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]
for i in (a,b,c,d):
    print(i)
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]
