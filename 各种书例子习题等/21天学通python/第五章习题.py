#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

"""
实现用户输入一门课程的两门子课程，第一门课程60分，显示pass，第一门不及格，显示failed，第一门及格，第二门不及格 显示补考

a1=int(input("enter your number:"))
a2=int(input("enter your number:"))
chengji = {}
chengji.update({"yuwen":a1})
chengji.update({"shuxue":a2})
print(chengji)

if chengji.get("yuwen") >= 60 and chengji.get("shuxue") < 60:
    print("bukao")
elif chengji.get("yuwen") >=60:
    print("pass")
else:
    print("failed")

"""

#编程实现用户输入20个数，将所有数收集到一个列表中，然后分别将基数，偶数放入两个列表中去

"""
alllist=[]
oushu=[]
jishu=[]
countnum = 0
while True:
    if countnum < 5:
        a=input("enter a number")
        if a.isdigit():
            a=int(a)
            countnum += 1
            alllist.append(a)
            if (a % 2) == 0:
                oushu.append(a)
            else:
                jishu.append(a)
    else:
        break

print(oushu)
print(jishu)
print(alllist)
"""
#
# alllist=[]
# countnum = 0
# while True:
#     if countnum < 10:
#         a=input("enter a number")
#         if a.isdigit():
#             a=int(a)
#             countnum += 1
#             alllist.append(a)
#     else:
#         break
#
# oushu= [ i for i in alllist if i % 2 == 0 ]
# jishu = [i for i in alllist if i % 2 != 0 ]
# print(oushu)
# print(jishu)

"""



设有以下信息的字符串
myseq=
"""
"""
[a:1,b:2,c:3]
[a:3,b:3,c:8]
[a:7,c:2,m:7,r:4]
[a:2,c:4,m:6,r:4]
[a:3,c:2,m:7,r:5]
"""


myseq="""[a:1,b:2,c:3]
[a:3,b:3,c:8]
[a:7,c:2,m:7,r:4]
[a:2,c:4,m:6,r:4]
[a:3,c:2,m:7,r:5]
"""
myseq=myseq.split()

a=["aa(1)","bb(2)"]



print(a[1])