#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/9/14:05
# Python 3.5

#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import redis
#
#
# class RedisHelper:
#
#     def __init__(self):
#         self.__conn = redis.Redis(host="192.168.77.129",password="123456")
#
#     def public(self, msg,chan):#发布
#         self.__conn.publish(msg,chan)
#         return True
#
#     def subscribe(self,chan): #订阅频道
#         pub = self.__conn.pubsub()
#         pub.subscribe(chan)
#         pub.parse_response()
#         return pub
import redis
import threading

class Listener(threading.Thread):
    def __init__(self, r, channels):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)

    def work(self, item):
        print (item['channel'], ":", item['data'])

    def run(self):
        for item in self.pubsub.listen():
            if item['data'] == "KILL":
                self.pubsub.unsubscribe()
                print (self, "unsubscribed and finished")
                break
            else:
                self.work(item)

if __name__ == "__main__":
    r = redis.Redis(host="192.168.77.129",password="123456")
    client = Listener(r, ['test'])
    client.start()

    r.publish('test', 'this will reach the listener')
    r.publish('fail', 'this will not')

    r.publish('test', 'KILL')