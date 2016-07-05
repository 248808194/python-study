#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

import commons
def run():
    inp = input("enter something:")
    if hasattr(commons,inp):
        func=getattr(commons,inp)
        func()
    else:
        print("404")

#利用字符串的形式去模块中(寻找hasattr、删除delattr# ，检查getattr，设置setattr)成员，这就是反射



if __name__ == '__main__':
    run()
