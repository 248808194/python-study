#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

import time

print(time.time()) #unix时间戳
print(time.ctime()) #返回当前时间字符串格式
print(time.ctime(time.time()-86400))# 如果赋一个时间戳就返回时间戳的字符串格式
print(time.ctime(86400)) #Fri Jan  2 08:00:00 1970
#print(time.gmtime()) #把年月日都拆开了
#或者可以这样
a=time.gmtime() #gmtime是格林威治时间
print(a)
print(type(a))
print(a.tm_year,a.tm_mon,a.tm_mday) #利用time.gmtime
print(time.localtime()) #本地时间#其实和gmtime一样只是是本地时间
print(time.mktime(time.localtime())) #将struct_time转成unix时间戳格式
#time.sleep(4) #延时4秒钟，其实就是和shell sleep一样
print(time.strftime("%Y-%m-%d-%H",time.localtime())) #将struct转换成指定格式 #以后常用
print(time.strftime("%Y-%m-%d-%H",time.gmtime())) #以后常用
"""
 %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
"""

print(time.strptime("2015-05-11","%Y-%m-%d")) #以后常用
#把一个字符串格式的时间格式，转换成unix时间戳
a="2015-05-11 13:45:00"
print(time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S")))
