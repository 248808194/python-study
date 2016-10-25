#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-08-19-10-18
# Python 3.5

import socket
# url="""
# zhibo.xiduweb.com
# csd.51xidu.com
# lfe.51xidu.com
# vip.91xidu.com
# lj.91xidu.com
# kx.ytx222.com
# zhibo.xiduoil.com
# jm.xiduoil.com
# lj.xiduoil.com
# img.jm.xiduoil.com
# xzz.xiduoil.com
# img.lj.xiduoil.com
# m.zhibo.xiduweb.com
# """
# url = """
# www.xiduweb.com
# m.xiduweb.com
# www.51xidu.com
# m.51xidu.com
# console.51xidu.com
# yxy.xiduoil.com
# m.xiduoil.com
# """


url = """
console.zhibo.xiduweb.com
c.ytx222.com
"""
def getIp(domain):
    try:
        myaddr = socket.getaddrinfo(domain,'http')[0][4][0]
        return (myaddr)
    except Exception:
        return domain + "can not turn to ip "



if __name__ == "__main__":
    url=url.strip().split("\n")
    for i in url:
        print("%s, ip is ---> %s"%(i,getIp(i)))