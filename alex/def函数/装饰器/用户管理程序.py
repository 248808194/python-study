#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#定义一个全局变量
LOGIN_USER = { "is_login":False }

def outer(func):
    def inner(*args,**kwargs):
        if LOGIN_USER["is_login"]:
           r =  func()
           print(r)
           return r
        else:
            print("请登录:")
    return inner

@outer
def order():
    print("欢迎%s登录" % LOGIN_USER["current_user"])
@outer
def changepwd():
     print("欢迎%s登录" % LOGIN_USER["current_user"])
@outer
def manager():
    print("欢迎%s登录" % LOGIN_USER["current_user"])


def login(user,pwd):
    if user == 'zhoutao' and pwd ==  '123456':
        LOGIN_USER["is_login"] = True
        LOGIN_USER["current_user"] = user
        manager()

def main():
    while True:
        inp = input("1:后台管理 ,2:登录:   ")
        if inp == "1":
            manager()
        elif inp == "2":
            u_name = input("enter username:")
            u_pwd = input("enter password:")
            login(u_name,u_pwd)


main()