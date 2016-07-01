# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author: Zhoutao
# # while True:
# #     for i in ["/","-","|","\\","|"]:
# #         print ("%s\r" % i)
#
# # from sys import argv
# # script, first, second, third = argv
# # print "The script is called:", script
# # print "Your first variable is:", first
# # print "Your second variable is:", second
# # print "Your third variable is:", third
#
# root@bbs:~> cat test1.py
# from sys import argv
# script, first, second, third = argv
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third
# You have new mail in /var/spool/mail/root
# root@bbs:~> python test1.py a b c
# The script is called: test1.py
# Your first variable is: a
# Your second variable is: b
# Your third variable is: c
#
#
# # $ python ex13.py first 2nd 3rd
# # The script is called: ex13.py
# # Your first variable is: first
# # Your second variable is: 2nd
# # Your third variable is: 3rd
# # $ python ex13.py cheese apples bread
# # The script is called: ex13.py
# # Your first variable is: cheese
# # Your second variable is: apples