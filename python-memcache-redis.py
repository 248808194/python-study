#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/8/23:58
# Python 3.5

#

import redis
pool = redis.ConnectionPool(host="192.168.77.129",port=6379,password="123456")

r=redis.Redis(connection_pool=pool)
pipe=r.pipeline(transaction=True)
r.mset({"a1":123,"a2":456})
r.mset({"b1":123,"b2":456})
pipe.execute()
print(r.mget(["a1","a2","b1","b2"]))
