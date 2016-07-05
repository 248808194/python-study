#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
class sqlhelper:
    def __init__(self,a1,a2,a3):
        self.hhost=a1
        self.uusername=a2
        self.pwd=a3
        print("hhost = %s,uusername = %s,pwd=%s" %(self.hhost,self.uusername,self.pwd) )
        print("hhost = %s,uusername = %s,pwd=%s" %(a1,a2,a3) )
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


obj =  sqlhelper("a1.salt.com","zhou","tao")
obj.hhost = "c1.salt.com"
obj.uusername = "zhoutao"
obj.password = "123"

#obj.fetch("select * from A")
