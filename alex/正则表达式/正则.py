#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

import re
#通配符.
c=re.findall("zhou..o",str([1,2,3,4,5,6,"zhoutao","zhoutao123"])) #。表示通配符，
print(c)

#尖角符 ^

#print(re.findall('^zhoutao',str(["zhoutao",1,2,3,4,5,6,"zhoutao","zhoutao123"])))

print(re.findall('^zhoutao',"zhoutao123zhoutao"))

#$符号，最后面
print(re.findall('zhoutao$',"123zhoutao"))

 #          * + ? {} 重复

print(re.findall('ZHOUT.*o',"123zhouto",re.I)) # *匹配0到多次

print(re.findall('zhout.+o',"123zhoutaao")) # + 匹配1到多次

print(re.findall('zhout.?o',"123zhouto")) # + 匹配0到1次]

print(re.findall('zhout.{2}o',"123zhoutaao")) #匹配2次

print(re.findall('zhouta{2}',"123zhoutaao")) # 只是匹配了a

print(re.findall('zhout[ba]o',"123zhoutao")) #匹配b或者是a其中的任意一个
print(re.findall('zhout[ba]o',"123zhoutbo")) #匹配b或者是a其中的任意一个
print(re.findall('zhout[a-z][a-z]',"123zhoutbo")) #a-z中任意一个字符
print(re.findall('zhout[^0-9]o',"123zhoutao")) #^号在中括号中表示非的意思
print(re.findall('zhout[^a-z]o',"123zhout9o")) #^号在中括号中表示非的意思
print(re.findall('zhout[\d]o',"123zhout9o")) #\d表示任意一个数字
print(re.findall('ZHOUT.*o',"123zhoutAAo",re.I)) #大小写不敏感 #re.U编译标志位
"""
re.L 本地化识别 （locale-aware） 匹配
re.I 是匹配对大小写不敏感
re.M 多行匹配 影响 ^ 和 $
re.S 使. 匹配包括换行在内的所以字符

"""



#特别注意. ^ $ * + ? {} 在中括号中没有特殊意义


"""
反斜杠 \
反斜杠后面跟元字符去除特殊功能 （转义）
反斜杠后面跟普通字符实现特殊功能
\d  匹配任何十进制数： 它相当于[0-9]
\D  匹配任何非数字字符 相当 [^0-9]
\s  匹配任何空白字符 相当于 [ \t\n\r\f\v]
\S  匹配任何非空白字符 相当于 [^ \t\n\r\f\v]
\w  匹配任何字母数字字符 相当于 [a-zA-Z0-9_]
\W  匹配任何非字母数字字符 相当于 [^a-zA-Z0-9_]
\b  匹配一个单词边界，也就是单词和空格之间的位置
"""

#\b
print(re.findall(r'I\b',"I AM zhouItao"))


#match re.match(pattern,string,flags=0) 编译3标志位，用于修改正则表达式的匹配方式，如是否区分大小写等

a=re.match("zhoutao","zhoutao is my name zhoutao")
print(a) #<_sre.SRE_Match object; span=(0, 7), match='zhoutao'>
print(re.match("zhoutao","zhoutao is my name zhoutao").group())
print(re.search("zhoutao","zhoutao is my name zhoutao").group())




#re.sub #替换
a=str(["i get a" ,"i got b ","i gut c"])
print(re.sub("g.t","have",a))
print(re.sub("g.t","have",a,1)) #后面1表示最大替换次数
print(re.subn("g.t","have",a)) #后面会打印出一共替换了几次

# print(c)


#split 分隔
print(re.split("\D+","one1two2three3four4"))
print(re.split("\d+","one1two2three3four4"))


#compile 方法 #
#可以把正则表达式编译成一个正则表达式对象，可以把哪些经常使用的正则表达式编译成正则表达式对象，这样可以提高一定的效率

import re
text = "j good is a handsome boy he is cool clever and so on ..."
regex = re.compile(r"\w*oo\w*")
a=regex.findall(text)
print(a)


#匹配分组
import  re
origin = "has asdf1231gdfgd"
r= re.match("h\w+",origin)
print(r.group())
print(r.groups())
print(r.groupdict())

#加上括号变成分组
import  re
origin = "has asdf1231gdfgd"
r= re.match("h(\w+)",origin)
print(r.group())
print(r.groups()) # ('as',)
print(r.groupdict())

# 给组命名
import  re
origin = "has asdf1231gdfgd"
r= re.match("h(?P<name>\w+)",origin) #加上一个?P<keyname> 把匹配到的东西加上一个值就是字典的key
print(r.group())
print(r.groups())
print(r.groupdict())

#findall 分组
import  re
origin = "has hal asdf1231gdfgd"
r= re.findall("h\w+",origin) #
print(r)

import  re
origin = "has123 hal asdf1231gdfgd"
r= re.findall("h(\w+)",origin) #找到has hal 后再在has hal 中匹配，但不包括h
print(r)


import  re
origin = "hasaabc halaabc asdf1231gdfgd"
r= re.findall("h(\w+)a(ab)c",origin) #整体先匹配hasaabc halaabc ，先匹配完后再匹配分组，先匹配(\w+)拿到值为as ，然后还有一个分组的值为ab  [('as', 'ab'), ('al', 'ab')]

print(r)

# 无分组
origin = "hello alex bcd alex lge alex acd 19"
r = re.split("alex", origin)
print(r)
r1 = re.split("alex", origin,1) #以alex作为分割，不拿alex
print(r1)

# 有分组

origin = "hello alex bcd alex lge alex acd 19"
r1 = re.split("(alex)", origin, 1)
print("r1",r1)
r2 = re.split("(al(e(x)))", origin, 1)  #从外向内匹配，先匹配大的alex 在再alex中匹配ex,在在ex中匹配x
print(r2)


























# origin = "hello alex bcd alex lge alex acd 19"
# r1 = re.split("(alex)", origin, 1)
# print(r1)
# r2 = re.split("(al(ex))", origin, 1)
# print(r2)