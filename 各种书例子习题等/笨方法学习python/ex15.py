#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#读取文件

from sys import  argv

script, filename = argv #执行的时候python ex15.py filename


txt= open(filename) #open打开一个文件
print("here is your file name %s:" % (filename) ) 打印出filename变量

print(txt.read()) #读取文件 其实就是类似  print open('ex15_sample').read()
print("type the filename again:") #打印出一行文件，提示你再次输入文件名
file_again = input(">") #输入文件名
txt_again = open(file_again) #读取文件
print(txt_again.read())
