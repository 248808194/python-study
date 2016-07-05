#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

import sys
import time
def view_bar(num,total):
    # print("num",num)
    # print("total",total)
    rate = num/total
    rate_num = int(rate * 100)
    r1 = "\r%s>%d%%" %("="*num,rate_num)
    sys.stdout.write(r1)
    sys.stdout.flush()


if __name__ == "__main__":
    for  i in range(0,100):
        time.sleep(0.1)
        view_bar(i,100)