1#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/11/13:12
# Python 3.5
import pika
connection = pika.BlockingConnection( pika.ConnectionParameters(host="192.168.77.129") )
channle = connection.channel()

#创建exchange，exchange和队列绑定
channle.exchange_declare(exchange="zhoutao_logs",type="fanout") ,#创建logs exchange，# fanout和exchange相关队列均会接受到消息
messages="hello wor123ld"

channle.basic_publish(exchange="zhoutao_logs",routing_key="",body=messages)
connection.close()