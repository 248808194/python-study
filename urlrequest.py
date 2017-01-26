#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-08-17-17-09
# Python 3.5
a="""
lfe.51xidu.com
m.xiduoil.com
175.102.13.47
m.ytx222.com
kx.ytx222.com
lf.ytx222.com
jm.xiduoil.com
lj.xiduoil.com
lj.91xidu.com
c.ytx222.com
img.jm.xiduoil.com
xzz.xiduoil.com
img.lj.xiduoil.com
csd.51xidu.com
lfe.51xidu.com
zhibo.xiduweb.com
vip.91xidu.com
m.zhibo.xiduweb.com
zhibo.xiduoil.com
175.102.13.50
console.zhibo.xiduweb.com
yxy.xiduoil.com
175.102.13.51
175.102.13.51
www.51xidu.com
m.51xidu.com
www.xiduweb.com
m.xiduweb.com
www.xxidu.cn
m.xxidu.cn
console.51xidu.com
m.xiduoil.com
175.102.13.47
m.ytx222.com
kx.ytx222.com
lf.ytx222.com
jm.xiduoil.com
lj.xiduoil.com
lj.91xidu.com
c.ytx222.com
img.jm.xiduoil.com
xzz.xiduoil.com
img.lj.xiduoil.com
csd.51xidu.com
"""

a=a.strip().split("\n")
b=[]
for i in a:
    b.append("http://"+i)
print(b)

from urllib.request import urlopen

for i in b:
    try:
        resp = urlopen(i)
        code = resp.getcode()
        print("%s open code is %s"%(i,code))
    except Exception as ex:
        print("%s open code is failed" %(i),ex)

#
