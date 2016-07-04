#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#5-2
def tpl_sum(T):
    result = 0
    for i in T:
        result += i
    return result


print(tpl_sum((1,2,3,4)))
print(tpl_sum([1,2,3,4]))
print(tpl_sum([1,2,123]))

#5-3
def hello(name="nihao"):
    print("%s zhoutao" %name)

#默认值声明name等于你好

hello()
def hello(name="nihao"):
    print("%s zhoutao" %name)


hello("hello") #指定了name值为hello

#如果有默认值和无默认值两个参数必须先声明无默认值参数
def foo(a,e=3):
    print(a,e)

foo(123)


def foo(hi="nihao",name="python"):
    print("%s,%s" %(hi,name))


foo()
foo("hello")
foo("hello","zhoutao")


#5-6

def foo(*args,a,b=5):
    print(args,a,b)

foo((1,2,3),a=5)

def foo(*a,b):
    print(a,b)

foo(123,b=123)


#5-7

def foo(a,b=1,**kwargs):
    print(a,b,kwargs)

foo(123,k=1,c=2,g=3)

#5-8

def cube(name,**nature):
    all_nature = { 'x':1,'y':1,'z':1,'color':'white', 'weight':1 }
    all_nature.update(nature)
    print(name,"立方体的属性:")
    print('体积：',all_nature['x'] * all_nature['y']*all_nature['z'])
    print('颜色:',all_nature['color'])
    print('重量:',all_nature['weight'])


cube('zhoutao',x=3,y=3,z=3,color="blue",weight=123)


#5-9

def foo(a,b):
    return a*b

print(foo(*(3,4))) #拆解元祖提供位置参数
print(foo(**{'a':3,'b':4})) #拆解字典提供关键字参数


5-10

def foo(aint,alist):
    aint = 0
    alist[0]=0
    alist.append(4)
    print('in foo aint',aint)
    print('in foo alist',alist)

aint = 3
alist = [1,2,3]
print("before aint", aint)
print("before alist",alist)
foo(aint,alist)
print("after aint", aint)
print("after alist",alist)


#5-11
def foo(lst=[]):
    lst.append('abc')
    print(lst)

foo()
foo()
foo()

def foo(): #global 参数一旦写到函数内，当执行函数的时候，a的值就为3
    global a
    a=0
    a += 3
    print(a)

a="zhoutao"
print(a)
foo()
print(a)


#filter
alist = [0,1,2,3,4,5,6,7,8,9]
a=list(filter(lambda x:x >= 5,alist))
print(a)

#filter是过滤结果为真则挑出来
#map是计算出结果跳出来
alist = [0,1,2,3,4,5,6,7,8,9]
a=list(map(lambda x:x +1,alist))
print(a)

#自定义函数排序
# alist = [9,8,7,6,5,123,34,5,123,5,1]
# alist.sort()
# print(alist)
# a=sorted(alist)
# print(a)
# sorted(alist)

# a=str1.count(' ')
# print(a)
import  string
str1="12312 1232 31  12 3"
def foo(a):
    return a.count(' ')

foo(str1)

def foo(a):
    b=sorted(a)
    print(b)


foo([9,8,7,6,5,123,34,5,123,5,1])




