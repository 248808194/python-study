#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#一个函数可以被多个装饰器装饰
USER_INFO = {}
def check_login(func):
    def inner(*args,**kwargs):
        if USER_INFO.get("is_login",None):
            ret = func(*args,**kwargs)
            return ret
        else:
            print("PLS LOGIN")
    return inner

def check_admin(func):
    def inner(*args,**kwargs):
        if USER_INFO.get("is_login",None): #这样写的原因是None为false就不执行
            if USER_INFO.get("user_type",None) == 2:
                ret = func(*args,**kwargs)
                return ret
            else:
                print("无权查看")
        else:
            print("请登录")
    return inner

def check_admin(func):
    def inner(*args,**kwargs):
        if USER_INFO.get("user_type",None) == 2:
            ret = func(*args,**kwargs)
            return ret
        else:
            print("无权查看")
    return inner

@check_login
@check_admin
def index():
    print("index")

@check_login
def home():
    print("home")

@check_login
def login():
    print("login")


def main():
    while True:
        inp = input("1,login,2:查看信息，3.超级管理员管理")
        if inp == '1':
            login()
        elif inp == '2':
            index()
        elif inp == '3':
            home()



main()