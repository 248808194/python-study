#
#
# LOG_USER = {"is_login":False}
#
# def outer(func):
#     def inner(*args,**kwargs):
#         if LOG_USER["is_login"]:
#             r = func()
#             print(r)
#             return r
#         else:
#             print("pls login !!")
#     return inner
#
# @outer
# def manager():
#     print("U are in MANAGER NOW!!")
# @outer
# def order():
#     print("U are in ORDER now:")
#
# def login(u_name,u_pwd):
#     if u_name == "zhoutao" and u_pwd == "123":
#         LOG_USER["is_login"] = True
#         LOG_USER["current_user"] = u_name
#         manager()
#
#
# def main():
#     while True:
#         inp = input("enter A(manager)/B(order):")
#         if inp == "A":
#             manager()
#         elif inp == "B":
#             u_name = input("enter your name:")
#             u_pwd = input("enter you pwd:")
#             login(u_name,u_pwd)
#
#
#
#
# main()


#利用装饰器装欢当前事件到unix事件

import datetime
import  time

# import datetime
# def outer(func):
#     def inner():
#         print("当前格林威治时间为:")
#         r=func()
#         print(r)
#         print("当前事件减少10天")
#         print(datetime.datetime.now() + datetime.timedelta(days=-10))
#     return inner
#
# @outer
# def time():
#     print(datetime.datetime.now())
#     return "FFF"
# time()
# print(datetime.datetime.now()) #输出当前格式，精确到微秒
#print(datetime.datetime.now().timetuple()) #转换成struct时间格式
# print(datetime.datetime.now() + datetime.timedelta(days=10)) #增加10天
# print(datetime.datetime.now() + datetime.timedelta(days=-10))#减少10天
# print(datetime.datetime.now() + datetime.timedelta(hours=-10))#减少10天
# print(datetime.datetime.now() + datetime.timedelta(seconds=-10))#减少10天

def outer(func):
    def inner():
        print("before")
        r=func()
        print("after")
        return r
    return inner

@outer
def foo():
    print("f1")
    return "FOO"

#foo()
a=foo()
print("a is ", a ,type(a))




