#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/11/13:16
# Python 3.5
import pika

connection = pika.BlockingConnection( pika.ConnectionParameters(host="192.168.77.129") )
channel = connection.channel()


#创建exchange，exchange和队列绑定
channel.exchange_declare(exchange="zhoutao_logs",type="fanout")#创建logs exchange，# fanout和exchange相关队列均会接受到消息
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue  #随机创建队列名
channel.queue_bind(exchange="zhoutao_logs",queue=queue_name) #让exchange和队列做绑定


def callback(ch,method,properties,body):
    print(body)

channel.basic_consume(callback,queue=queue_name,no_ack=True)
channel.start_consuming()
