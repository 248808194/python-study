#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/5/13:35
# Python 3.5
import sys,time
def view_bar(num, total):
    rate = float(num) / float(total)
    rate_num = int(rate * 100)
    r = '\r%d%%' % (rate_num, )
    sys.stdout.write(r)
    sys.stdout.flush()
for i in range(0, 100):
        view_bar(i, 65535)