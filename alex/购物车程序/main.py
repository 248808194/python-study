#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#主入口文件：main.py
import operate,enter

if __name__ == '__main__':
    print("\033[35m----------------------------请输入用户名密码----------------------------\033[0m")
    enter.user() #先判断用户输入的用户名密码是否正确
    while True:
        operate.welcome() #循环执行operate.welcome（）函数
