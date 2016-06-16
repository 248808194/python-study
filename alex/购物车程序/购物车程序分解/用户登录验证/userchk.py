#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#1：先定义一个用户数据文件
#2： 定义一个字典去读取用户数据库，暂存下用户名密码
#3： 验证数据用户的用户名和密码
with open('userdb','rU') as dbfile:
    data=dbfile.readlines() #j将文件内容每行读入到变量data中去
    userdict=dict()
    for i in data:
        i=i.strip().split(':')
        userdict[i[0]]=i[1] #i第0个元素就是用户名，i第二个元素就是密码
        print(userdict)

def ccc():
    while True:
        username = input("Enter username:")
        passwd = input("Enter password:")
        if username in userdict.keys(): #检查字典中是否存在 username 用户名
            password  = userdict[username]
            if passwd == password:
                break
            else:
                print("您输入的密码错误")
        else:
            print("您输入的账号错误")

ccc()



