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

exit_flag = False
product_list = [
    ('iphone',100),
    ('moto',200),
    ('xp',300),
    ('mac book',300),
    ('mac air',500),
    ('mac pro',400),
    ('itouch',150)
] #定义一个字典，字典中每一个元素为元祖(出于安全考虑商品价格不能随意修改，固用使用元祖)

shop_list = [] #提前定义一个空的购物车列表


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

while exit_flag is not True:
    print("product list".center(50,'-'))
    for item in enumerate(product_list): #打印出索引值+列表元素 (元祖表示出来)
        index = item[0]
        p_name = item[1][0] #
        p_price = item[1][1]
        print(index,'.',p_name,p_price)
    user_chose = input("[q=quit/c=check],waht do you want buy:")
    if user_chose.isdigit():
        user_chose=int(user_chose)
        if user_chose < len(product_list):
            p_item = product_list[user_chose]
            if p_item[1] <= salary: #买不起
                shop_list.append(p_item)
                salary -= p_item[1]
                print("Added [%s] into shop list ,you current balance is [%s]" %(p_item,salary) )
            else:
                print("your banance is [%s],cannot afford this.." %(salary) )
    else:
        if user_chose == 'q' or user_chose == 'quit':
            print("purchased products as below".center(40,'*') )
            for item in shop_list:
                print(item)
            print("END".center(40,'*') )
            print("your balance is [%s]" %(salary) )
            print("Bye")
            exit_flag = True
        elif user_chose == 'c' or user_chose == 'check':
            print("purchased products as below".center(40,'*') )
            for item in  shop_list:
                print(item)
                print("END".center(40,"*"))
                print("Your balance is %s" %(salary))

