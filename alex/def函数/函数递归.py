#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

def func(n):
    n+=1
    if n > 3:
        return "END"
    return func(n)

a=func(2)
print(a)
