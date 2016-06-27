#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

#__doc__ 获取文件注释

__file__

#print(__file__)
import os
from lib import commons
#print(os.path.abspath(__file__))

#获取上层目录
#print(os.path.dirname(os.path.abspath(__file__)))
#print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(commons.__package__)



