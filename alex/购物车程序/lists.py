#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
import operate
aaa = operate.gouwche[0]
with open('users','rU') as u_2:
    ss = u_2.readlines()
    die = []
    for line in ss:
        if aaa in line:
            line = line.strip().split(':')
            die.append(line[0])
            die.append(line[1])
            die.append(line[2])

with open('users','rU')as u_3:
    ads = u_3.readlines()
    dia = []
    for lin in ads:
        lin = lin.strip().split(':')
        dia.append(lin[0])

