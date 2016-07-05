#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

class C1:
    def f1(self):
        pass
class C2:
    def f2(self):
        pass
class C3(C2,C1): #前后关系，前面的优先级高，后面的优先级低，
    #如果C1中也是def f2，那么obj.f2()的时候执行的是C2中的f2
    def f3(self):
        pass



obj = C3()
