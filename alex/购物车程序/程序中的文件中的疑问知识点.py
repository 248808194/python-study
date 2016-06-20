#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#with 用法
with open('users','rU') as file:
    aa=file.readlines() #['zhoutao:123456:10000\n', 'sara:654321:20000']
    print(type(aa))
    dic = dict() #生成一个空字典，字典下的第一个
    for i in aa:
        print(i)
        i = i.strip().split(':') #strip删除空白符，split()返回分隔后的字符串列表，返回的是一个列表,['zhoutao', '123456', '10000']
        print(i)
        dic[i[0]]=i[1] #字典赋值，生成键值对，key=i的第0个元素，value的i的第二个元素

print(dic)
# strip()用法
# a= ' asdfsdaf '
# a=a.strip()
# print(a)  asdfsdaf

#format函数
send="我的名字叫{username},我很爱我的{zuguo}" #通过关键字参数
formatstr=send.format(username='周涛',zuguo='cn')
print(formatstr)

send="我的名字叫{},我很爱我的{}"
formatstr1=send.format('zhoutao','cn')
print(formatstr1)
send="我的名字叫{1},我很爱我的{0}" #通过位置
formatstr2=send.format('zhoutao','cn')
print(formatstr2)