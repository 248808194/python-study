#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

def run():
    inp = input("enter something:")
    m,f=inp.split('/')
    obj= __import__("lib."+m,fromlist=True) #可以利用字符串拼接的方式，导入模块，如果是要以文件路径，要驾驶fromlist = true
    if hasattr(obj,f):
        func=getattr(obj,f)
        func()
    else:
        print("404")

#利用字符串的形式去模块中(寻找hasattr、删除delattr# ，检查getattr，设置setattr)成员，这就是反射



if __name__ == '__main__':
    run()