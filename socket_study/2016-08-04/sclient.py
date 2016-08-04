#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = '2016/8/4'
# Python 3.5

import socket


while True:
    ip_port = ("127.0.0.1",9999)
    s=socket.socket()
    s.connect(ip_port)
    wel_msg = s.recv(1024)
    wel_msg = str(wel_msg,encoding="gbk")
    print(wel_msg)
    inp = input("enter your cmd:")
    if len(inp) == 0: continue
    s.sendall(bytes(inp,encoding="utf8"))
    recv_date = s.recv(1024)
    str_msg_date = str(recv_date,encoding="gbk")
    print(str_msg_date)
    recv_msg_size = int(str_msg_date.strip().split("|")[-1])
    print(recv_msg_size)
    if str_msg_date.startswith("R"):
        send_start=bytes("S",encoding="utf8")
        s.sendall(send_start)

    recv_date_all = b""
    recv_date_size = 0
    while recv_date_size < recv_msg_size:
        recv_date=s.recv(1024)
        recv_date_all +=recv_date
        recv_date_size +=len(recv_date)

    print(str(recv_date_all,encoding="gbk"))
    s.close()


s.close()



