#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

user='zhoutao'
passwd='123'

username = input("username:")
password = input("password:")
if username == user and password == passwd:

    print("welcome to loging")
else:
    print("username %s is worng...." %(username) )