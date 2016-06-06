#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

import random
import string

while True:
    enterstr = input("Please input START_GAME(S)/QUIT_GAME(Q):").upper() #enterstr用过.upper()全部定义为大写
    num = random.randint(0,100) #在0-100里面生成一个随机数字
    counter = 0
    if (enterstr == 'Q'):
        break
    elif (enterstr == "S"):
        while True: #判断部分，通过while if 比较输入大小猜数字
            if counter < 3: #计数器
                gus_num = int ( input("pls input a number:") )
                if gus_num == num:
                    break
                elif gus_num > num:
                    print("bigger think again")
                else:
                    print("smaller think again")
            else:
                countinue_confire = input("do you want to continue Y/N:")
                if countinue_confire == 'Y':
                    counter = 0
                    continue
                else:
                    break
            counter = counter + 1
    else:
        print("wrong enter pls try again")

