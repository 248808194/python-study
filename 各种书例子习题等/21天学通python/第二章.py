#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao


"""
用户输入一个整数，输出这个整数的平方值
NUM=int(input("enter a number:"))
print(NUM)
print(NUM*NUM)
"""

"""
用户输入三个整数放入列表并输出最小值

lista=[]
NUM=input("enter 3 number:")
a=NUM.split(",")
print(a,type(a))


for I in a:
    lista.append(int(I))

b=min(lista)
print(b)

"""

"""
编程实现用户输入5个整数，并得到列表【01,2,3,4】然后选用两种切片方法去除列表中[1,3]并输出

NUM=input("enter 5 number:")
a=NUM.split(",")
print(a[1:4])
print(a[-3])
"""

"""
初始化字典，{"a":1,"b":2},并设置其key为c的对应值为3

dict1={'a':1,'b':2}
print(dict1)
dict2 = dict((["a",1],["b",2])) #元祖字典
print(dict2)
dict3=dict([("a",1),("b",2)])
print(dict3)

dict3.update({"c":3})
print(dict3)

"""

"""
输入某科目排名前10的分数，求其总分和平均分

"""
lista=[]
countten=0

while True:
    inp=input("enter stu number")
    if inp.isdigit():
        inp=int(inp)
        countten += 1
        if countten == 3:
            continue
        lista.append(inp)
    if countten == 10:
        break

print(lista)
print(sum(lista))
print(len(lista))




