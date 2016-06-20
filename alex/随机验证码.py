#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

#纯字母验证码
import random
a=[]
for i in range(6):
    temp=random.randrange(65,91)
    c=chr(temp)
    a.append(c)

resurt="".join(a)
print(resurt)

#2/4 位有数字验证码
import random
a=[]
for i in range(6):
    if i == 2 or i == 4:
        num = random.randrange(0,10)
        a.append(str(num))
    else:
        temp=random.randrange(65,91)
        c=chr(temp)
        a.append(c)

resurt="".join(a)
print(resurt)

#纯随机验证码
import random
a=[]
for i in range(6):
    r=random.randrange(0,5)
    if r == 2 or r == 4:
        num = random.randrange(0,10)
        a.append(str(num))
    else:
        temp=random.randrange(65,91)
        c=chr(temp)
        a.append(c)

resurt="".join(a)
print(resurt)