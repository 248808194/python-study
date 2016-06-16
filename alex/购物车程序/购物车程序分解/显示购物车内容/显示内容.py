#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

huowu = {
    "iphone6splus": 6000,
    "huaweimate8": 3700,
    "asus": 4299,
    "alienware": 21999,
    "strix-gtx970": 3649,
}

index=1
for i  in huowu.keys():
    aa="{}:       商品名称:{}    ,商品价格:{}"
    print(aa.format(index,i,huowu[i]))
    index +=1