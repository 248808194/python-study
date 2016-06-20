#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

# def fetch(backend):
#     result = []
#     with open("ha.conf","r") as f:
#         flag = False
#         for line in f:
#             if line.strip().startswith("backend") and line.strip() == "backend " + backend:
#                 flag = True
#                 continue
#             if flag and line.strip().startswith("backend"):
#                 break
#             if flag and line.strip():
#                 result.append(line.strip())
#     return  result
#
# #思路一，先检查记录存不存在
# ret=fetch("www.oldboy.org")
# print(ret)


def add(backend,record):
    with open("ha.conf","r") as old , open("new.ha.conf","w") as new:
        in_backend = False
        has_backend = False
        has_record = False
        for line in old:
            if line.strip().startswith("backend") and line.strip() == "backend " + backend: #如果存在backend开头，且这一行是backend + backend变量
                has_backend = True
                in_backend = True
                new.write(line)
                continue
            if in_backend and line.strip().startswith("backend"): #如果in_backend为真，并且这一行是backend开头 (其实就是已经到了下一个backend)
                if not has_record: #如果不是record值
                    new.write(" "*8 + record +"\n") #写入新参数
                    new.write(line) #写入老的backend
                    in_backend = False #把in_backend 设为False
                    continue
            if in_backend and line.strip() == record: #如果在backend里面，并且这一行的值为record值
                has_record = True
                new.write(line)
                continue
            if line.strip():
                new.write(line)
        if not has_backend:
            new.write("backend "+ backend + "\n")
            new.write(" "*8 + record + "\n")


add("www.oldboy.org","server 100.2.7.10 100.1.7.10 weight 20 maxconn 3000")
