#coding: utf-8

#x=10 为全局变量
#x=5为局部变量

print "Example 1"
print '------------------------'
x=10
def foo():
    x=5
    print "in foo x= %d" %(x)
foo()
print "out foo x=%d" %(x)
print "#######################################################################3333"

print "Example 2"
print '------------------------'
a=10
def foo(a):
    print "in foo a=%d" %(a)

foo(20)
print "out foo a=%d" %(a)
print "#######################################################################3333"

#局部变量作用域只在函数内部看Example 3
print "Example 3"
print '------------------------'
a=10
def foo(a):
    y=99
    print "in foo a=%d y=%d" %(a,y)

foo(20)
#print "out foo a=%d y=%d" %(a,y)
print "#######################################################################"

#变量查找顺序
x=10;z=10
def foo():
    x=5
    y=1
    def bar():
        print "x=%d,y=%d,z=%d" %(x,y,z)
        return bar

foo()
x,y,z


def foo1(x):
    def bar1(y):
        return x+y
    return bar1


#a=foo1(10)其实是return 的bar1 以为foo1(x) 逻辑就是returnbar1函数
#a(10)#其实是bar1(y)：return x+y
#如果这样就可以这样
a=foo1(10)(20)
print a



