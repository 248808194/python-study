#!/usr/bin/env python

# Author: Zhoutao

import os
#from XXX import  XXX as XXXX_XX
#XXXX_XX.XX()


# os.system("dir")
#保存命令读出来
cmd_res = os.popen("dir").read()
print(type(cmd_res))
print(cmd_res)