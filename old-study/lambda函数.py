#coding: utf-8
#匿名函数与lambda函数，python允许lambda关键字创建匿名函数，不需要以标准方式声明函数，一条完整的
#lambda语句是一个完整的表达式，表达式的返回值是一个可以调用的函数对象

#examp1

def add(x,y):
    return x+y

a=  add(1,1)

#examp2

add=lambda x,y:x+y

a=add(1,1)
#例1和例2是相等的

#example3
def foo(x):
    return lambda y:x+y
#example4
def foo1(x):
    def bar1(y):
        return x+y
    return bar1

#3,4相等


#lambda 和列表解析

a=[lambda x,i=i :x+i for i in range(10)]
#以为i为全局变量，所以i=i

#map函数



]: a=reduce(lambda x,y:x+y,[1,2,3],1)

In [132]: a
Out[132]: 7

In [133]: a=reduce(lambda x,y:x+y,[1,2,3],12)

In [134]: a
Out[134]: 18

a=filter(lambda x:  x>0,(0,1,2,3,4,5))


#map
zt1=[1,2,3]
zt2=[4,5,6]
zt3=[7,8,9]

def foo(*x):
    return sum(list(x))/3.0

print map(foo,zt1,zt2,zt3)