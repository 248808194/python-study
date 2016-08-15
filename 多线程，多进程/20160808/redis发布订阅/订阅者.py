#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/9/14:10
# Python 3.5

import fabudingyue


obj = fabudingyue.RedisHelper()
date=obj.subscribe("fm103.7")
print(date.parse_response())