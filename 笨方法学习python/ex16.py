#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

print("""
这个程序打开一个文件，然后用truncate方法把这个文件清空(即删除文件内容)，
然后请用户输入3行内容，再使用write方法把用户的输入写入到这个文件，
最后使用close关闭这个文件。对这里面的每一个文件读写命令，请使用pydoc工具检查其用法。
""")
from sys import argv

srcipt, filename = argv

print ("we are going to erase %s:" %(filename) )

print("if you don't want that hit CTRL-C(^C)")

input("?")
print("opening the file...")

target = open(filename,'r+') #可读可写 不会创建不存在的文件 从顶部开始写 会覆盖之前此位置的内容
#target = open(filename,'w+') #w+ 可读可写 如果文件存在 则覆盖整个文件 不存在则创建
#target = open(filename,'a+') #a+ 可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建


print(target.read())
#print("truncating the file , goodbye")
#target.truncate()#清空文件
print("Now I'm going to ask you for three lines")

line1=input("line1:")
line2=input("line2:")
line3=input("line3:")
print ("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print ("And finally, we close it.")
target.close()
print( "check files %r" %(filename) )

print(open(filename).read())
