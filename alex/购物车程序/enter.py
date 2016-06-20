#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#读出当前存在的用户名和密码，并生成字典
with open('users','rU') as u_1:
    ss = u_1.readlines()
    dic = dict()
    for lind in ss:
        lind = lind.strip().split(':')
        dic[lind[0]] = lind[1]

#用户欢迎登陆模块
def welcome(wel):
    sent = "!\033[31m{users}\033[0m!Welcome to the shopping mall"  # 设置欢迎信息
    aa = (sent.format(users=wel)) #欢迎信息
    scr = 80 #设置一个长度
    text = len(aa) -9
    box=text
    left = (scr-box) // 2
    print  # 输出空
    print(' ' * left + '+' + '-' * (box) + '+')
    print(' ' * left + '|'+ ' '*text + '|')
    print(' ' * left + '|'+aa + '|')
    print(' ' * left + '|'+ ' '*text + '|')
    print(' ' * left + '+'+ '-'*(box) + '+')

#用户登陆验证模块

def user():
    import operate
    while True:
        user_1 = input("username:") #输入用户名
        user_2 = input("passwd:") #输入密码
        operate.gouwche.append(user_1) #定义是谁的购物车
        if user_1 in dic.keys(): #判断如果输入的user_1在dic的keys中
            passw = dic[user_1] #将正确的用户密码赋值给passw
            if user_2 == passw: #如果用户输入的密码等于数据库中存储的密码的话
                welcome(user_1) #执行welcome()函数
                break
            else:
                print("\033[35m您~输入的账号或密码错误\033[0m")
                print("")
        else:
            print("\033[35m您输入的账号或密码错误\033[0m")  # 不匹配则重新输出
            print("")

#购买模块
def shopp():
    import operate
    if not operate.gouwche: #判断huo是否为空,huo是设置为空的字典，存放当前用户所添加的东西，
        #判断字典，是否为空的方法，if dict: 或者 if not dict:
        print("\033[35m-------------------------------购物车没货物-------------------------------\033[0m")
    else:  #不为空则结算
        cart()#加载显示购物车物品的函数
        shop_1 = input("结算Y/N:")
        if shop_1 == 'Y':
            deal()
        elif shop_1 == 'n':
            print("已退出购物车")

#显示购物车内容

def cart():
    import operate
    shop_1 = 1
    for sho_1 in operate.gouwche.keys(): #从用户的存放货物的字典逐个读取货物名称
        if sho_1 in operate.gouwche.keys():#分别读取货物的键值对，这里的逻辑不太好没时间更改，后续更改
            sh_2 = len(sho_1)  # 计算长度
            sh_3 = 50 - sh_2  # 设置下划线长度
            ca_4 = ("[{s_1}]商品名称:{s_2}" + "_" * sh_3 + "{s_3}元")  # 设置提示信息
            print(ca_4.format(s_1=shop_1,s_2=sho_1,s_3=operate.huo[sho_1]))
            shop_1 += 1  # 将货物编号加一


#支付模块
def deal():
    import  operate,lists #加载operate,lists
    # 支付过程
    aas = int(lists.die[2])  #将lists的2索引（金额），转换成int类型
    for sa in operate.gouwche.keys():#sa从字典huo取key
        sa_1 = int(operate.gouwche[sa]) #sa_1等于转换类型后的huo[sa]的值（购物车商品金钱
        if aas >= sa_1: #判断文件中的当前用户金额是否大于等于huo[sa]的值
            aas = aas - sa_1 #如果大于则进行运算用已存金额减去商品金额
            lists.die[2] = aas #并将列表爹die[2]（也就是用户的资金）更新成买完商品的
            del operate.gouwche[sa] #然后删除该商品
            ss_1 = '支付商品\033[35m{n}\033[0m成功,实付金额为:\033[31m{n_1}\033[0m元！' #设置提示信息
            print(ss_1.format(n=sa,n_1=sa_1))  #设置提示信息
        else:
            ss_2 = '支付商品\033[35m{n}\033[0m失败,应付金额为:\033[31m{n_1}\033[0m元！请充值！' #设置提示信息
            print(ss_2.format(n=sa,n_1=sa_1)) #设置提示信息
            # 写入文件过程，创建一个当前所有存在用户的列表，这样就可以判断当前用户在文件的第几行
    clo = lists.die.index(list_aaa)
    f = open('users', 'r+')  # 打开文件
    flist = f.readlines()  #按行读取
    aa = '{a_1}:{a_2}:{a_3}\n'  # 设置文件内容
    flist[clo] = aa.format(a_1=lists.die[0], a_2=lists.die[1],a_3=lists.die[2])  # clo就是当前用户所在的文件行数，后面加上内容，a_1 当前用户 a_2 当前用户密码 a_3 当前用户余额
    f = open('users', 'w')  # 以w的方式打开文件
    f.writelines(flist)  # 写入
    f.close()  # 关闭
    print("退出购物车")

#从购物车删除模块

def dele():
    import operate
    if not operate.gouwche:
        print("购物车没有物品")
    else:
        cart()  # 否则调用显示购物车模块
        while True:
            saa = input("请输入删除商品的名称：")
            if saa == 'exit':
                break
            elif saa in operate.gouwche.keys():
                del operate.gouwche[saa]
                print("删除商品成功!!")
                #退出删除判断
                saa_1 = input("是否退出Y/N:")
                if saa_1  == 'y':
                    break
            else:
                print("您输入有误请重新输入")

#充值模块这里还可以写只有admin可以充值，或者验证充值用户的密码
def topup():
    import lists
    clb = lists.dia.index(lists.aaa)
    while True:
        q_1 = input("请输入充值金额以整数为单位（元）：")
        q_2 = str.isdigit(q_1)
        if q_1 == 'exit':
            break
            if q_2 == True:
                q_1 = int(q_1)
                q_3 = type(q_1)
                if q_3 == int:
                    lists.die[2] = int(lists.die[2])
                    lists.die[2] = lists.die[2] + q_1
                    f=open('users','r+')
                    flist = f.readlines()
                    aa='{a_1}:{a_2}:{a_3}\n'
                    flist[clb] =aa.format(a_1=lists.die[0],a_2=lists.die[1],a_3=lists.die[2])
                    f=open('users','w')
                    f.writelines(flist)
                    f.close()
                    vv_1 = ('充值成功，充值金额为\033[31m{vv}\033[0m，当前余额为\033[31m{v_1}\033[0m')
                    print(vv_1.format(vv=q_1,v_1=lists.die[2]))
                    break
                else:
                    print("\033[31m您输入的金额过大\033[0m")
            else:
                print("输入有误")

#商品模块
def catg():
    import operate
    print("购物商品")
    car = 1
    for ca_1 in operate.shangpin:
        ca_2 = len(ca_1)
        ca_3 = 50-ca_2
        ca_4 = ("[{s_1}]商品名称:{s_2}"+"_"*ca_3+"{s_3}元")#输出信息
        print(ca_4.format(s_1=car,s_2=ca_1,s_3=operate.shangpin[ca_1]))
        car += 1
        print("-购物商品-")

#添加模块
def mone():
    import operate
    while True:
        mon = input("请输入加入购物车产品的名称：")
        if mon in operate.shangpin.keys():
            print("\033[31m------------------------商品已经添加请先到购物车结算----------------------------\033[0m")
        elif mon in operate.gouwche.keys():
            print("\033[35m---------------------------添加成功请到购物车结算-------------------------------\033[0m")
        elif mon == 'exit':
            print("\033[35m---------------------------------退出购物---------------------------------\033[0m")
            break
        else:
            print("添加失败，请核对")

#注册用户模块，这里还可以写只有admin可以创建用户

def login():
    import lists
    while True:
        with open("user",'rU') as u_3:
            ads = u_3.readline()
            diz = []
            for lin in ads:
                lin = lin.strip().split(':')
                diz.append(lin[0])
        w_1 = input("create username:")
        if w_1 in diz:
            print("user exists")
        elif w_1 == 'exit':
            break
        else:
            w_2 = input("create user password:")
            w_3 = len(w_2)
            if w_3 > 5:
                output = open('users','a')
                aa = '{a_1}:{a_2}:{a_3}\n'
                flist = aa.format(a_1=w_1,a_2=w_2,a_3=10000)
                output.write(flist)
                output.close()
                ll = "-成功创建用户：{l_1}"
                print(ll.format(l_1=w_1))
                break
            else:
                print("密码长度过短")








