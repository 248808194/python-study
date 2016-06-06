#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

num = 20
counter = 0 #counter 为计数器
while True:
    if counter < 3:
        gus_num = int ( input("pls input a number:") )
        if gus_num == num:
            break
        elif gus_num > num:
            print("bigger think again")
        else:
            print("smaller think again")
    else:
        continue_confirm = input("Do you want to continue: Y/N")
        if continue_confirm == 'Y':
            counter = 0
            continue
        else:
            print("bye")
            break
    counter = counter +1



# else:
#     print("wrong enter pls try again")

