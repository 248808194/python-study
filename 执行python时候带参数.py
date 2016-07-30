#执行脚本 test.py filename
#打印出file文件的行出来

#!/usr/bin/env python
import sys,os

def print_lines():
    scriptname,filename = sys.argv
    with open(filename,"r") as f:
        for lines in f.readlines():
            lines = lines.strip()
            print(lines)

print_lines()

