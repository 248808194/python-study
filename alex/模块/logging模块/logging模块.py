#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

import logging

def f1():
    logging.basicConfig(filename="test.log",level=logging.INFO,
                        format="%(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %I:%M:%S %p"
                        )
    logging.debug("this is debug level")
    logging.info("this is info level")
    logging.warning("this is warning level")

f1()
