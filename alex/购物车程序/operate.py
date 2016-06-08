#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#逻辑结构
#主要判断用户的输入，根据输入的关键字，调用不同的函数

#初始化商品

shangpin = {
"iphone6splus": 6000,
"huaweimate8": 3700,
"asus": 4299,
"alienware": 21999,
"strix-gtx970": 3649
}

#初始化空的购物车
gouwche = []
#功能判断函数
def welcome():
    import enter
    import os
    import lists
    s_1 = input("请输入操作:")
    if s_1 == 'car':
        enter.catg()
    elif s_1 == 'help':
        print('''
       car___________________商品
       help__________________帮助
       buy___________________添加至购物车
       shop__________________购物车结算
       und___________________购物车移除商品
       top___________________充值
       bal___________________余额
       enr___________________注册用户
       exit__________________返回
        ''')
    elif s_1 == 'buy':
        enter.shopp()
    elif s_1 == 'und':
        enter.dele()
    elif s_1 == 'top':
        enter.topup()
    elif s_1 == 'bal':
        b_1 =  "\033[36m---------------------当前用户：{b_2}，余额为:{b_3}----------------------\033[0m"
        print(b_1.format(b_2 = gouwche[0],b_3 = lists.die[2]))
    elif s_1 == 'enr':
        enter.login()
    elif s_1 == 'exit':
        os._exit(0)



