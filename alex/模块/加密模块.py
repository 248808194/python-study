#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

import hashlib

obj = hashlib.md5()
obj = hashlib.md5(bytes("asfsdf",encoding="utf-8")) #自定义加密
obj.update(bytes("123",encoding="utf-8"))
result = obj.hexdigest()
print(result)

