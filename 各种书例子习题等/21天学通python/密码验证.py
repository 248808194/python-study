#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

a={"city":"shanghai","name":"zhoutao"}
def foo(**kwargs):
    if kwargs["city"] == "shanghai" and kwargs["name"] == "zhoutao":
        print("pass")
        return "pass"
    else:
        return 0
a={"city":"shanghai","name":"zhoutao"}


print(foo(**a))

def person(name,age,*args,city,job):
    print(name,age,city,job,args)


person("zt",18,city="shanghai",job="enginner")




