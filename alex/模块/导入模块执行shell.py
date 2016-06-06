#!/usr/bin/env python

# Author: Zhoutao

import os

# os.system("dir")
#保存命令读出来
cmd_res = os.popen("dir").read()
print(type(cmd_res))
print(cmd_res)