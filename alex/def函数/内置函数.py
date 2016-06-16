#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

"""
abs 绝对值
print(abs(-1))
false 0,None [] {} ()
all() 接受一个可迭代对象，所有为真才为真
"""
"""
a=all([0])
print(a)
#any() 接受一个可迭代对象 只要有真就为真
a=any([1,0,None])
print(a)
"""

"""
#字符串转换成字节类型
#bytes（只要转换的字符串，按照什么编码）
print(bytes("周涛",encoding="utf-8"))
print(bytes("周涛",encoding="gbk"))
"""
"""
#字节转换字符串
print(str(bytes("周涛",encoding="utf-8"),encoding="utf-8"))
"""

"""
#callable 是否可以被执行或者调用
a=1
b=callable(a) #值为false
print(b)

"""

# chr()
# ord()
# ascii转换
"""
a=chr(65)
print(a)
n= ord('B')
print(n)
import string
a=string.ascii_uppercase
"""
"""
b=list(a)
print(b)
for i in b:
    i=ord(i)
    print(i)
"""
"""
for i in range(0,99):
    i=chr(i)
    print(i)
"""

# compile() #把一个字符串编译成python 代码
# eval() #接受字符串，讲字符串当成一个表达式
# exec()
"""
s="123"
#编译，single，eval，exec
r=compile(s,"<string>","exec") #将字符串变异成代码
print(r)
exec(r) #执行代码
s="10*10"
ret=eval(s)
print(ret)

"""
"""
#反射：delattr() getattr() setattr() hasattr()

# dir() 快速查看，对象提供哪些功能
# print(dir(dict))
"""

"""
#分页显示，example 总共97页，每页显示10条，需要多少页
a=divmod(97,10)
print(a) #(9, 7)22，能得到商，能得到余
a=divmod(100,10)
print(a)
# 返回的是一个元祖，
# a[0] 为商
# a[1]为余
# 可以给2个参数接受
a=divmod(100,10)
n1,n2=divmod(100,10)
print(n1,n2)
print(type(n1)) #<class 'int'>
"""

"""
#判断对象是否是某一个的实例
a=isinstance("",str)
print(a)
a=isinstance((),tuple)
print(a)
a=isinstance([],list)
print(a)
a=isinstance({},dict)
print(a)
"""


# filter()
# map()

"""
def f1(args):
    result = []
    for item in args:
        if item > 22:
            result.append(item)
    return  result

li = [11,22,33,44,55]
a=f1(li)
print(a)

def f2(a):
    if a>22:
        return True
li = [11,22,33,44,55]
ret=filter(f2,li)
#在filter内部 ，循环第二个参数
# 就是for item in li:
# 在每次循环的时候去执行第一个参数，如果为真就把元素添加到result下去
# #其实就是li是可以循环的，把li每一个元素去执行f2，如果为真就添加到ret中去
# #就是做筛选符合条件就要，不符合条件就不要
#lambda内部会做返回值
li = [11,22,33,44,55]
ret=filter(lambda a: a>22 ,li) ##lambda内部会做返回值
print(list(ret))
"""

"""
#map函数 将函数返回值添加到结果中去
print(list(map(lambda a:a+100 ,[11,22,33,44,55] )))
ret=map(lambda a:a+100 ,[11,22,33,44,55] ) #[111, 122, 133, 144, 155]
print(list(ret))
"""

"""
#globals() #所以的全局变量
#locals()  #所以的局部变量
NAME='zhoutao'
def f1():
    a=123
    b=321
    print(locals())
    print(globals())
f1()
"""

"""
print(hash("str"))

a=max([1,2,3,4,5])
print(a)
a=min([1,2,3,4,5])
print(a)
a=sum([1,2,3,4,5])

print(a)
"""

"""
a=reversed([1,2,3,4,5,6]) #返回的是一个迭代器
for i in a:
    print(i)
"""


"""
#round()四舍五入
print(round(1.8))
print(round(1.5))
print(round(1.4))

"""

#sorted()#排序
"""
a=[1,2,3,5234,3461,1,23]
a.sort()
print(a)

#和上面的方法其实一样的
a=[1,2,3,5234,3461,1,23]
sorted(a)
"""


"""
#例子
# zip把所有的第一个元素当成一个大元素，以此类推
a=["zhoutao",1,2,3]
b=["is",1,2,3]
c=["goodman",1,2,3]

d=zip(a,b,c)
e=(list(d))
print(e) #[('zhoutao', 'is', 'goodman'), (1, 1, 1), (2, 2, 2), (3, 3, 3)]
f=e[0]

# f=" ".join(list(d)[0])
print(f)
g=" ".join(f)
print(g)


#pow() 方法返回 xy（x的y次方） 的值。
print(pow(2,2))
"""