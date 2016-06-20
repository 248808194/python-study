'''
6–2.
字符串标识符.修改例 6-1 的 idcheck.py 脚本,使之可以检测长度为一的标识符,并且
可以识别 Python 关键字,对后一个要求,你可以使用 keyword 模块(特别是 keyword.kelist)来帮你.
'''


import string
import keyword

alphas = string.ascii_letters + "_" #返回大小写 + _  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_
nums = string.digits #返回0-9数字
key_list = keyword.kwlist #得到python所有关键字列表 #False True if else 等等

print("welcome to id check ")
print("testees must be ai least 2 chars long")


myinput = input("enter your ID:")

if len(myinput) >= 1:
    if myinput[0] not  in alphas: #检查字符串第一个元素是否在alphas中
        print("invalid : first symbol must be alphabetic")
    elif myinput in key_list:#检查输入的是否是在key_list 关键字中
        print("invalid: the input id is a Python's keyword")
    else:
        alphnums = alphas + nums
        for otherchar in myinput[1:]: #遍历字符串myinput从第二个函数开始到最后一个开始检查，如果都不在alphnums下则break掉
            if otherchar not in alphnums:
                print(" invalid: remaining symbols must be alphanumeric")
                break
        else:
            print("okay it's an id ")