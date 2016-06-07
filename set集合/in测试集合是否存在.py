#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
drink = {
'martini':{'vodka','vermouth'},
'black russian':{'vodka','kahlua'},
'white russian':{'cream','kahlua','vodka'},
'manhattan':{'rye','vermouth','bitters'},
'screwdriver':{'orange juice','vodka'}
}

for name,contents in (drink.items()):
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)
#    print("name is %r ,contents is %r" %(name,contents))
#    print(name)


print("""
python的set和其他语言类似, 是一个无序不重复元素集,
基本功能包括关系测试和消除重复元素.
集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算
sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。
因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作
""")
x = set('spam')
y = set(['h','a','m'])
print(x,y)

print("交集&,交集就是找出2个集合相同的元素")
a=x&y
print(a)
print(type(a))


print("并集|,屏迹就是合并去重")
a=x|y
print(a)
print(type(a))

print("差集-，")
print(x)
print(y)
a=x-y #找出x在网络中没有的x，p没有
b=y-x #找出y在x中没有的 h没有
print("print a")
print(a)
print(type(a))
print("print b")
print(b)
print(type(b))