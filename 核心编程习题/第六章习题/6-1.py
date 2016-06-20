"""
字符串，string模块中是否有一种字符串方法
或者函数可以帮我们鉴定下一个是否是另外一个大字符串的一部分

"""
#
a="zhoutao is a man"
if  "zhoutao" in a:
    print("in it")
else:
    print("no in")

#或者
b=a.find("zhoutao")
print(b) #第0个元素，如果没有会返回-1

b=a.count("zhoutao")
print(b) #count用于统计出现的次数

b=a.index("zhoutao") #检查是否包含子串，如果不包含，会抛出一个异常
print(b)