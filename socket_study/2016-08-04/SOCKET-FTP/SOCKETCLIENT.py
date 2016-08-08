#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/4/13:20
# Python 3.5



import json,os,sys,socket,time

IP_PORT=("127.0.0.1",9999)

s=socket.socket()
s.connect(IP_PORT)
def view_bar(num, total):
    rate = float(num) / float(total)
    rate_num = int(rate * 100)
    r = '\r%d%%' % (rate_num, )
    sys.stdout.write(r)
    sys.stdout.flush()

while True:
    inp = input(">>>:")
    send_list = inp.strip().split()
    send_msg = {
        "filename":send_list[1],
        "action":send_list[0],
        "filesize": os.stat(send_list[1]).st_size
    }
    print(send_msg.get("filesize"))
    s.sendall(bytes(json.dumps(send_msg),encoding="utf8"))
    res_date = s.recv(1024)
    print(res_date,type(res_date))
    resp_date = str(res_date,encoding="utf8")
    print(resp_date,type(resp_date))
    if resp_date == "200":
        with open(send_msg.get("filename"),"rb") as sfile:
            send_total = 0
            print(send_msg.get("filesize"))
            for i in sfile:
                s.send(i)
                send_total += len(i)
                view_bar(send_total,send_msg.get("filesize"))
            print("send file done")
    s.close()


