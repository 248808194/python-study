#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/12/14:32
# Python 3.5

import pymysql

#建立连接和游标
conn = pymysql.connect(host="192.168.77.129",user="zhoutao",password="123",db="T1")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) #默认获取的数据是元祖类型，如果想要或者字典类型的数据 加上cursor=pymysql.cursors.DictCursor


cursor.execute("select * from test")
#get one
getone=cursor.fetchone()
#get n
getn= cursor.fetchmany(5)
#get all
getall = cursor.fetchall()

print("getone=>\t%s\ngetn->\t\t%s\ngetall=>\t%s"%(getone,getn,getall))


conn.commit()#提交修改
cursor.close()#关闭游标
conn.close() #关闭连接