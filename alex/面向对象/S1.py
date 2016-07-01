#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

class sqlhelper:
    def __init__(self):
        print("自动执行")
    def fetch(self,sql): #self指的是类实例对象本身
        print(self.hhost)
        print(self.uusername)
        print(self.password)
        print(sql)

    def create(self,sql):
        pass

    def remove(self,sql):
        pass

    def modify(self,sql):
        pass


obj =  sqlhelper()
obj.hhost = "c1.salt.com"
obj.uusername = "zhoutao"
obj.password = "123"

obj.fetch("select * from A")

#在python只要类() 就会自动执行__init__方法