#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao


"""
练习一：在终端输出如下信息

小明，10岁，男，上山去砍柴
小明，10岁，男，开车去东北
小明，10岁，男，最爱大保健
老李，90岁，男，上山去砍柴
老李，90岁，男，开车去东北
老李，90岁，男，最爱大保健

"""
class Foo:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def kanchai(self):
        print("%s,%s岁, %s,上山去砍柴" %(self.name,self.age,self.gender))
    def qudongbei(self):
        print("%s,%s岁, %s,开车去东北" %(self.name,self.age,self.gender))
    def dabaojian(self):
        print("%s,%s岁, %s,最爱大保健" %(self.name,self.age,self.gender))



xiaoming=Foo("小明","18","男")
xiaoming.kanchai()
xiaoming.dabaojian()
xiaoming.qudongbei()

laoli=Foo("老李","90","男")
laoli.kanchai()
laoli.qudongbei()
laoli.dabaojian()

