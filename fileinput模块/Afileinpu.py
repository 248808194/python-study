"""
参考资料
http://www.tuicool.com/articles/VrmiUbV
fileinput.input()       #返回能够用于for循环遍历的对象
fileinput.filename()    #返回当前文件的名称
fileinput.lineno()      #返回当前已经读取的行的数量（或者序号）
fileinput.filelineno()  #返回当前读取的行的行号
fileinput.isfirstline() #检查当前行是否是文件的第一行
fileinput.isstdin()     #判断最后一行是否从stdin中读取
fileinput.close()       #关闭队列
files:                  #文件的路径列表，默认是stdin方式，多文件['1.txt','2.txt',...]
inplace:                #是否将标准输出的结果写回文件，默认不取代
backup:                 #备份文件的扩展名，只指定扩展名，如.bak。如果该文件的备份文件已存在，则会自动覆盖。
bufsize:                #缓冲区大小，默认为0，如果文件很大，可以修改此参数，一般默认即可
mode:                   #读写模式，默认为只读
openhook:               #该钩子用于控制打开的所有文件，比如说编码方式等;
"""
#利用fileinput读取文件所有行
"""
import  fileinput
for line in fileinput.input("log"):
    # print(line)
    print(fileinput.filename()," |" "LineNumber:",fileinput.lineno(),line)
"""
#利用fileinput对多文件进行操作，并原地修改内容
"""
import fileinput
def process(line):
    return "this is line %s " %(fileinput.lineno()) + line.rstrip()
for line in fileinput.input(["log","log2"],inplace=1,openhook=None):
    print(process(line))
"""

#利用fileinput实现文件内容替换，并将原文件作备份
"""
import fileinput
for line in fileinput.input("log",backup=".bak",inplace=1):
    print(line.replace("hello","hi"))

"""
#利用fileinput对文件简单处理
"""
import sys
import fileinput
for line in fileinput.input("INFO",backup=".bak",inplace=1):
    sys.stdout.write(line)
    sys.stdout.write("=>")

"""

#利用fileinput及re做日志分析: 提取所有含日期的行
"""
import re
import fileinput
import sys
_date="\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

for line in fileinput.input("log",backup=".bak",inplace=1):
    if re.search(_date,line):
        sys.stdout.write("FOUND==>>")
        sys.stdout.write(line)
"""


#利用fileinput及re做分析: 提取符合条件的电话号码

"""
import re
import fileinput

_phone="\d{11}"

for line in fileinput.input("phone",backup=".bak"):
    if re.search(_phone,line):
        print("正确的电话号码为"+line)
"""
