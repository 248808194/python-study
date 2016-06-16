#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

money = 30
shifu = 0
huowu = {
    "iphone6splus": 1,
    "huaweimate8": 2,
    "asus": 3,
    "alienware": 4,
    "strix-gtx970": 5,
}
for  i in huowu.keys():
#   print(huowu[i]) #打印出各商品的金额
    huoq = int(huowu[i])
    if money >= huoq:
        shifu = shifu+huoq
        money = money - huoq
        #del huowu[i]
    #print(money)
sss = "支付成功，实付金额{},余额:{}"
print(sss.format(shifu,money))
#将money更新到userdb 下去


with open('user','a+') as userfile:
    qw  = userfile.readlines()
    for we in qw:
        cd=we.strip().split(':')
        print(cd)
        cd[2] = str(money)
        print(cd)
        abc=':'.join(cd)
    userfile.writelines(abc)





