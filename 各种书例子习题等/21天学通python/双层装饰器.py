#所有都是需要登录的，才能查看，所以必须定义一个装饰器check_login()函数

USER_INFO={}
def check_login(func):
    def inner(*args,**kwargs):
        if USER_INFO.get("is_login",None): #！：1 执行顺序
            ret = func(*args,**kwargs) #！：2 执行顺序      #2层装饰后func代指的就是 check_admin下的inner函数
            return ret #！： 7执行顺序
        else:
            print("pls login first")
    return inner

def check_admin(func):
    def inner(*args,**kwargs):
        if USER_INFO.get("user_type",None) == 2: #！：3执行顺序
            ret = func(*args,**kwargs) #！：4执行顺序          #func代指的就是原来index函数
            return ret #！：6执行顺序
        else:
            print("无权限查看")
    return inner

@check_login
@check_admin
def index():
    print("index") #！:5 执行顺序           #root
#!!!!!!!非常重要
"""
@check_admin
def index(): 他们两个合起来的函数 就是代指的是check_admin下的inner函数
合起来创建新的函数nindex就是代指的是check_admin下的inner函数

在外传又加了一个check_login装饰器后
@check_login
@check_admin
def index(): #他们合起来的函数体就是代指的是check_login下的inner函数
合起来创建新的nnindex就是代指的是check_login下的inner函数

！！！！！经过层层装饰得到的就是最外层的nnindex函数

！！！！！我函数我去调用你，你的return值就要给我

"""


@check_login
def home():
    """
    普通用户
    """
    print("home") #普通用户查看信息

def login():
    user = input("enter username:")
    if user == "admin":
        USER_INFO["is_login"] = True
        USER_INFO["user_type"] = 2
    else:
        USER_INFO["is_login"] = True
        USER_INFO["user_type"] = 1

#主文件

def main():
    while True:
        inp = input("enter1(login):登录;2(home):查看信息,3(index):超级管理员管理\n >>>")
        if inp == "1":
            login()
        elif inp == "2":
            home()
        elif inp == "3":
            index()


main()