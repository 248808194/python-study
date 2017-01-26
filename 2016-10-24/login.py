#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-10-24-11-07
# Python 3.5

import re
import menu

def login(u_name,u_passwd): #用户登录
    with open("userdb","r") as db:
        for line in db:
            line = line.strip().split("|")
            if line[2] == "1": #判断用户是否被锁定,锁定即退出程序
                print("%s is locked pls context the administrator" % (u_name))
                exit()
            if line[0] == u_name and line[1] == u_passwd: #判断用户名密码均匹配，打印欢迎信息
                print("welcome %s"%(u_name))
                return True
            else:
                print("password is not match")
                return False

def lock_user (u_name): #用户锁定函数
    with open("userdb", "r") as db:
        lines = db.readlines()
        with open("userdb", "w") as db:
            for i in lines:
                if i.startswith(u_name):
                    db.write(re.sub("0", "1",i))
                else:
                    db.write(i)


def main(): #主函数
    a=0#锁定判断标志位
    while True:
        if a == 3:#用户输入超过3次执行lock函数并退出循环
            lock_user(u_name)
            print("尝试3次登录失败，用户%s 锁定 程序退出"%(u_name))
            break
        else:
            u_name = input("Enter your username:")
            u_passwd = input("Enter you password:")
            if login(u_name,u_passwd)  == False:#如果login函数返回的结果为False则让a自加1
                a+=1
                continue
            else:
                menu.menu()
if __name__ == "__main__":
    main()

