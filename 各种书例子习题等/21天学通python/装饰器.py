#example 1
def abc(func):
    def wrapper(*args,**kwargs):
        print("starting running")
        func(*args,**kwargs)
        print("end running")
    return wrapper

def hello(name):
    print("hello",name)

hello("zhoutao")

#example 2
@abc
def demo_decoration(x):
    a=[]
    for i in range(x):
        a.append(i)
    print(a)

demo_decoration(10)





# def document_it(func):
#     def new_function(*args,**kwargs):
#         print("running function:" ,func.__name__)
#         print("args:",args)
#         print("kwargs:",kwargs)
#         result = func(*args,**kwargs)
#         print("result:",result)
#         #return  result
#     return new_function
#
# @document_it
# def add_ints(a,b):
#     print("ADD_INTTT")
#     return a + b
# add_ints(3,5)

#加上装饰器之后自动执行装饰起函数#注意是执行，并且将被装饰的函数作为装饰起函数的参数来传递
#将装饰器函数的返回值重新赋值给被装饰的函数

# def outer(func):
#     def inner():
#         print("before")
#         func() #func()代指的就是老的F1函数
#         print("after")
#     return inner
#
# @outer
# def f1():
#     print("F1")
#
#
# f1()





