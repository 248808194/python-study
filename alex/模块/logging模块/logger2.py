#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

#create logger
import logging
logger = logging.getLogger("TEST-LOG") #先获取logger对象
logger.setLevel(logging.DEBUG) #定义一个全局的日志基准，其他定义的只能比我高，不能比我低

#输入到什么地方-》屏幕
ch = logging.StreamHandler() #日志打印到屏幕
ch.setLevel(logging.DEBUG) #z只想在屏幕上打印DEBUG
#输入到什么地方 -》 文件
fh = logging.FileHandler("access.log")
fh.setLevel(logging.DEBUG)
fh1 = logging.FileHandler("1access.log")
fh1.setLevel(logging.DEBUG)

#设置输出格式
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
) #定义输出格式
ch.setFormatter(formatter) #给屏幕输出设定一个日志格式 #调用已经设定过的formatter格式
fh.setFormatter(formatter)
fh1.setFormatter(formatter)

logger.addHandler(ch) #把日志打印到指定的handler里面
logger.addHandler(fh)
logger.addHandler(fh1)

#开始打印日志
logger.debug("test debug")
logger.info("test info")
logger.warning("test warning")
logger.critical("test critcal")
logger.error("test error ")
