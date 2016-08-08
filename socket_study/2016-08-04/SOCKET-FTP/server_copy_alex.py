#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/5/14:41
# Python 3.5

import socketserver,json
IP_PORT=("127.0.0.1",9999)


class MYsocket_ftp_server(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            print("123")
            date = self.request.recv(1024)
            if len(date) == 0:break
            task_date = json.loads(date.decode()) #bytes ----> str #loads json_str ----> python_dict
            task_action = task_date.get("action") #get dict value
            if hasattr(self,"task_%s" %task_action):
                func =getattr(self,"task_%s" % (task_action))
                func(task_date)
            else:
                print("task %s not supported" %(task_action))

    def task_put(self,*args,**kwargs):
        print("------put",args,kwargs)
        filename = args[0].get("filename")
        print(filename)
        filesize = args[0].get("file_size")
        print(filesize,type(filesize))
        server_response  = {"status":200}
        self.request.send(bytes(json.dumps(server_response),encoding="utf8"))
        with open(filename,"wb") as ftpfile:
            recv_size = 0
            while recv_size < filesize:
                date = self.request.recv(1024)
                ftpfile.write(date)
                recv_size += len(date)


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(IP_PORT,MYsocket_ftp_server)
    server.serve_forever()