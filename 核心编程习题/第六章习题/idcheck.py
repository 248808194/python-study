#输出一个字符串，必须满足开头的是字母，后面必须是字母加数字_的组合

import string

zimu = string.ascii_letters+"_"
shuzi = string.digits


while True:
    inp = input("enter a string:")
    if len(inp) > 1:
        if inp[0] in zimu:
            for otherstring in inp[1:]:
                if otherstring not in zimu+shuzi:
                    print("有一个或多个字符不满足字母+数字要求")
                    break
            else:
                print("check  okay")
        else:
            print("第一个字符必须是字母")
    else:
        print("string must > 1")

