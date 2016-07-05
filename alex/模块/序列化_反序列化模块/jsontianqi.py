#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
import requests
import json
r=requests.get("http://wthrcdn.etouch.cn/weather_mini?city=上海")
r.encoding = "utf-8"
print(r.text)

print(type(r.text))
dic = json.loads(r.text)
print(dic,type(dic))


