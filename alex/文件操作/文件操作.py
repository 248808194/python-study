#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#1：打开文件
# f=open('file','r')
# f=open('file','w')
#
# #文件存在就保存，不存在，创建并且写入内容
# f=open('file','x')
# f=open('file','a') #追加。。。

#truncate截断文件，当指针在哪边的时候，当执行truncate，就会把指针后面的内容给清空

# f=open("db","r+")
# f.seek(3)
# f.truncate()

# f.close()
#for 循环文件对象

f=open("db","r+")
for line in f:
    print(line.strip())
f.close()

#with打开多个文件 ,读一个文件写另外一个文件
# with open("db", "r") as f1,  open("db1", "w") as f2:
#     times = 0
#     for line in f1:
#         times += 1
#         if times <= 10:
#             f2.write(line)
#         else:
#             break

#读写文件时候文件进行替换
with open("db", "r") as f1,  open("db1", "w") as f2:
    for line in f1:
        new_line=line.replace("sdffg","12345")
        f2.write(new_line)