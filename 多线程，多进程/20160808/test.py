#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/8/14:50
# Python 3.5

def foo():
    f1 = 123
    print("foo f1%s"%f1)
    def bar():
        f1 +=1
        print(f1)
