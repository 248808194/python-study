#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/12/15:34
# Python 3.5

import paramiko


#SSHClient 封装 Transport）推荐
transport = paramiko.Transport( ("192.168.77.129",22) )
# private_key=paramiko.RSAKey.from_private_key_file("id_rsa")
transport.connect(username="root",password="newbie")


sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put("id_rsa","/tmp/id_rsa")
sftp.get("test.py","test.py")

transport.close()