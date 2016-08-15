#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/11/16:03
# Python 3.5

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',type='topic')

# severity = "error"
severity = "info"
message = 'error Hello World!'
channel.basic_publish(exchange='direct_logs',routing_key=severity,body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()