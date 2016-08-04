#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/4/13:20
# Python 3.5

import socket,json,os

ip_port = ("127.0.0.1",9999)
s=socket.socket()
s.connect(ip_port)

while True:
    send_date = input(">>>:").strip()
    if len(send_date):continue
    cmd_list = send_date.split()
    if len(cmd_list) < 2: continue
    task_type=cmd_list[0]
    if task_type == "put":
        abs_filepath = cmd_list[1]
        if os.path.isfile(abs_filepath):
            file_size = os.stat(abs_filepath).st_size
            filename = abs_filepath.split("\\")[-1]
            msg_date  = {
                "action":"put",
                "filename":filename,
                "file_sieze":file_size,
            }
            s.sendall( bytes(json.dumps(msg_date),encoding="utf8") )
            server_confirmation_msg = s.recv(4096)
            confirm_date = json.loads(server_confirmation_msg.decode())
            if confirm_date["status"] == 200:
                with open(abs_filepath,"rb") as sendfile:
                    for line in sendfile:
                        s.sendall(line)
                    print("send file done")

        else:print("file not exsits");continue

    else:print("task not suported");continue
    recv_date = s.recv(1024)
    print(str(recv_date,encoding="utf8"))

s.close()




