#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/4/13:20
# Python 3.5

import socket,json,os,time,sys
import multiprocessing

ip_port = ("127.0.0.1",9999)
s=socket.socket()
s.connect(ip_port)

def view_bar(num, total):
    rate = float(num) / float(total)
    rate_num = int(rate * 100)
    r = '\r%d%%' % (rate_num, )
    sys.stdout.write(r)
    sys.stdout.flush()

while True:
    send_date = input(">>>:").strip()
    print(len(send_date))
    if len(send_date) == 0:continue
    print(123)
    cmd_list = send_date.split()
    print(cmd_list)
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
                "file_size":file_size,
            }
            s.sendall( bytes(json.dumps(msg_date),encoding="utf8") )
            server_confirmation_msg = s.recv(4096)
            confirm_date = json.loads(server_confirmation_msg.decode())
            if confirm_date["status"] == 200:
                already_send_total = 0
                with open(abs_filepath,"rb") as sendfile:
                    for line in sendfile:
                        s.sendall(line)
                        already_send_total += len(line)
                        view_bar(already_send_total,file_size)
                    print("send file done")

        else:print("file not exsits");continue

    else:print("task not suported");continue
    recv_date = s.recv(1024)
    print(str(recv_date,encoding="utf8"))

s.close()




