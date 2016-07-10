#http://www.jb51.net/article/50070.htm
#判断循目录 A/B/C是否存在，如不存在则环创建目录 A/B/C
# 在C目录下写入文件CC
# 在CC文件中写入手机号码
# 检查CC内容中的手机号码是否均是11位，如果不是删除掉不符合的手机号码
#将CC文件重新命名为BB，并且将BB文件移动到B目录下

import re
import fileinput
import os
import sys
import shutil

if os.path.exists("A/B/C") == False:
    os.makedirs("A/B/C")
else:
    with open("A/B/C/CC","w") as ctxt:
        ctxt.writelines("1392916291\n17767076666\n1852234888\n",)

for line in fileinput.input("A/B/C/CC",backup=".bak",inplace=1):
    _phone="\d{11}"
    if re.search(_phone,line):
        print("right number is ",line)


shutil.move("A/B/C/CC","A/B/BB")





