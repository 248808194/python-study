#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao


def login(username,passwd):
    with open('userdb','r') as userfile:
        for line in userfile:
            line = line.strip().split(':')
            if line[0] == username and line[1] == passwd:
                print("登录成功")
                return True
        else:
            print("登录失败")
            return  False


def regiter(username,passwd):
    with open('userdb','a') as userfile:
        newuser = "\n"+username+":"+passwd
        userfile.write(newuser)


def main():
    aa=input("请输入1:登录:/2:注册:")
    if aa == '1':
        username = input("输入用户名:")
        passwd = input("输入密码:")
        login(username,passwd)
    elif aa == '2':
        username = input("输入用户名:")
        passwd = input("输入密码:")
        regiter(username,passwd)
    else:
        print("输入不正确从新输入")


main()