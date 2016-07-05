#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

class F1: #父类，基类
    def show(self):
        print("show")
    def foo(self):
        print(self.name)

class F2(F1): #子类，派生类，#F1继承了F1类，相当于把F1里面的方法写到F2中去
    #F2子类，F1父类
    # def show(self):
    #     print("show")
    def __init__(self,name):
        self.name = name
    def bar(self):
        print("bar")


class F3(F2):
    pass


obj=F3("zhoutao")
obj.foo()



#继承中优先级是自己最高

#单继承中如果遇到self都要回到起点开始找，之类=》父类=》父父类
