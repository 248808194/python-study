#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

#创建列表

list1=[1,2,3,4,5]
print(type(list1))
#list函数创建空列表
a=list()
print(type(a))

#访问列表，切片等
a=list1[0]
print(a)

#更新列表
list1.append(6)
print(list1)

#使用list()将其它数据类型转换成列表
a=list('abcdefg')
print(a)
#元祖转换列表

atuple=(1,2,3,4,5,5)
a=list(atuple)
print (a)
#用split()可以依据分隔符将字符串切割成由若干子串组成的列表

zhoutao='2016/05/13'
a=zhoutao.split('/') #默认是空格
print(a)
zhoutao = '2016//05/1//12///123'
a=zhoutao.split('//')

print(a)
#，通过偏移量可以从列表中提取对应位置的元素

list=['a','b','c','d']
a=print(list[0])

#负偏移量代表从尾部开始计数：
a=print(list[-1])
a=print(list[-2])
a=print(list[-3])

#修改列表元素
names = ['www.confesseur.com','linux','centos']
names[0]=1
print(names)
#指定范围并使用切片提取元素
a=[0,1,2,3,4,5,6,7,8,9]
print(a[0:5]) #[0, 1, 2, 3, 4] #切片开始位0，结束位 5
print(a[0:5:2]) #偏移量[0, 2, 4]
#append添加元素到列表尾部
a.append([10,11,12])
print(a)
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