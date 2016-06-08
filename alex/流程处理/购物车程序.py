#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
salary = input("Input your gongzi:") #输入你的收入
if salary.isdigit(): #判断字符串是否为数字构成
    salary = int(salary) #如果是将数字转换成int类型
else:
    exit("invild data type") #如果不是直接exit退出

welcome = "Welcome to shop".center(50,'-')
print(welcome)

exit_flag = False 																							#先设定一个退出变量设置为False
product_list = [
    ('iphone',100),
    ('moto',200),
    ('xp',300),
    ('mac book',300),
    ('mac air',500),
    ('mac pro',400),
    ('itouch',150)
]
# 0 ('iphone', 100)
# 1 ('moto', 200)
# 2 ('xp', 300)
# 3 ('mac book', 300)
# 4 ('mac air', 500)
# 5 ('mac pro', 400)
# 6 ('itouch', 150)
# index = item[0]
# p_name = item[1][0]
# p_price = item[1][1]

shop_list = [] 	#提前定义一个空的购物车列表

while exit_flag is not True: #判断是否退出，如果exit_flag不为真的话，往下执行
    print("product list".center(50,'-'))
    for item in enumerate(product_list):#打印出索引值+列表元素 (元祖表示出来)
        index = item[0]
        p_name = item[1][0] #
        p_price = item[1][1]
        print(index,'.',p_name,p_price)
    user_chose = input("[q=quit/c=check],waht do you want buy:")	#让用户输入需要购买什么/CHECK检查购物车/退出
    if user_chose.isdigit(): #判断用户输入的如果是数字
        user_chose=int(user_chose) #转换成数字类型
        if user_chose < len(product_list): #判断选择商品号是否在product_list中#如果是
            p_item = product_list[user_chose] #定义p_item变量记录商品名称，
            if p_item[1] <= salary: #判断商品的价格是否大于工资收入  #如果小于工资收入
                shop_list.append(p_item) #将选择的商品追加到shop_list列表中去
                salary -= p_item[1] #工资收入减去商品价格，得到剩余工资
                print("Added [%s] into shop list ,you current balance is [%s]" %(p_item,salary) ) #打印出购物车中的商品，打印出剩余工资
            else:
                print("your banance is [%s],cannot afford this.." %(salary) )
    else: #如果用户输入的不是数字，判断是否为 q退出，或者为c check检查
        if user_chose == 'q' or user_chose == 'quit': #如果用户输入的是退出
            print("purchased products as below".center(40,'*') )
            for item in shop_list:#打印出已购商品列表
                print(item)
            print("END".center(40,'*') )
            print("your balance is [%s]" %(salary) ) #打印出余额
            print("Bye") #打印出再见
            exit_flag = True #将退出变量设为true
        elif user_chose == 'c' or user_chose == 'check': #如果用户选择的是c检查商品和余额
            print("purchased products as below".center(40,'*') )
            for item in  shop_list:
                print(item) #打印出已选商品列表
                print("END".center(40,"*"))
                print("Your balance is %s" %(salary)) #打印出余额


#用户启动时先输入工资
#用户启动后打印商品列表
#允许用户选择购买商品
#允许用户不断的购买商品
#购买时检测余额是否足够，够直接扣款，不够，打印余额不够
#允许用户主动退出，退出时候打印已购商品列表
