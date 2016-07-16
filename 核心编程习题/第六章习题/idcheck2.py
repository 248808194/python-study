#kwlist  --  Python 关键字列表 如：nlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 等
#输出一个字符串，必须满足下面几个条件
#1：字符长度必须大于0
#2:字符串必须不是python关键字
#3：判断字符串第一个字符是否为字母
#4：判断其他字符是否满足字母+数字要求

from keyword import kwlist
import  string

zimu = string.ascii_letters+"_"
print(zimu)
shuzi = string.digits
print(shuzi)

zimushuzi = zimu+shuzi
def check():
    inp = input("enter a string:")

    if len(inp)  == 0:
        print("字符串长度必须大于0")
        return

    if inp in kwlist:
        print("字符串不能是python关键字")
        return

    for index,inpstr in enumerate(inp):
        if index == 0 and inpstr not in zimu:
            print("第一个字符必须是字母或者下划线")
            break
        if inpstr not in zimushuzi:
            print("除第一个外，后面的字符必须是字母或者数字或者下划线")
    else:
        print("满足要求")

print(__name__)

if __name__ == "__main__":
    check()


