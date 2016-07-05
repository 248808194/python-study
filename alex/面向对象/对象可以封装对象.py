#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

class C1():
    def __init__(self,name,age):
        self.name=name
        self.age=age

class C2():
    def __init__(self,name,obj):
        self.name=name
        self.obj=obj
    def show(self):
        print(self.name)

class C3():
    def __init__(self,money,aa):
        self.money = 123
        self.aaa = aa


OBJ_C1=C1("C1_NAME","18")
OBJ_C2=C2("C2_NAME",OBJ_C1)
OBJ_C3=C3(OBJ_C2)

print(OBJ_C2.name,OBJ_C1.name) #C2_NAME 18

print(C3.aaa.OBJ_C1.name)






