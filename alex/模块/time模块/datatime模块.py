#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

import datetime
import time
print(datetime.date.today()) #打印当前日期
print(datetime.date.fromtimestamp(time.time())) #讲时间戳转成日期格式

"""
    def __new__(cls, days=0, seconds=0, microseconds=0,
                milliseconds=0, minutes=0, hours=0, weeks=0):
"""
print(datetime.datetime.now()) #输出当前格式，精确到微秒
print(datetime.datetime.now().timetuple()) #转换成struct时间格式
print(datetime.datetime.now() + datetime.timedelta(days=10)) #增加10天
print(datetime.datetime.now() + datetime.timedelta(days=-10))#减少10天
print(datetime.datetime.now() + datetime.timedelta(hours=-10))#减少10天
print(datetime.datetime.now() + datetime.timedelta(seconds=-10))#减少10天

