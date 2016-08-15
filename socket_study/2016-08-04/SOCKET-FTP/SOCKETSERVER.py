#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = '2016/8/4=%time'
# Python 3.5

import socketserver,json
IP_PORT = ("127.0.0.1",9999)
class MYsocketserver(socketserver.BaseRequestHandler):
    def handle(self):
        recv_msg = self.request.recv(1024)
        recv_msg = str(recv_msg,encoding="utf8")
        recv_msg_dict=json.loads(recv_msg) #str-dict
        action = recv_msg_dict.get("action")
        print(recv_msg_dict)
        print(action)

        if hasattr(self,"%s"%(action)):
            func=getattr(self,"%s"%action)
            func(recv_msg_dict)


    def put(self,*args,**kwargs):
        filename = args[0].get("filename").split("\\")[-1]
        print(filename)
        filesize = args[0].get("filesize")
        self.request.sendall(bytes("200",encoding="utf8"))
        with open(filename,"wb") as file:
            file_size = 0
            while file_size < filesize:
                recv_date = self.request.recv(1024)
                len_recv_date = len(recv_date)
                file_size +=len_recv_date
                file.write(recv_date)



if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(IP_PORT,MYsocketserver)
    server.serve_forever()
