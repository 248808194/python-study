#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

def fetch(backend): #查找函数
    result = []
    with open("ha.conf","r") as f:
        flag = False
        for line in f:
            if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                flag = True
                continue
            if flag and line.strip().startswith("backend"):
                break
            if flag and line.strip():
                result.append(line.strip())
    return  result

#思路一，先检查记录存不存在
ret=fetch("www.oldboy.org")
print(ret)



# def add():
#     pass
