#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = '2016/8/4'
# Python 3.5


import socketserver
import subprocess
IP_PORT = ("0.0.0.0",9999)
class MYsocketserver(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.request.sendall(bytes("welcome to my socker server",encoding="utf8"))
            recv_date = self.request.recv(1024)
            print(recv_date)
            cmd=subprocess.Popen(recv_date.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            cmd_result = cmd.stdout.read()
            #发送ready消息
            ready_tag = "R|%s" %(len(cmd_result))
            self.request.sendall(bytes(ready_tag,encoding="utf8"))

            #接收到start 消息头
            recv_date_start=self.request.recv(1024)
            if str(recv_date_start,encoding="utf8").startswith("S"):
                self.request.sendall(cmd_result)








if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(IP_PORT,MYsocketserver)
    server.serve_forever()




