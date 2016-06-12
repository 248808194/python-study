old_dict = {
    "#1":8,
    "#2":4,
    "#4":2,
}

new_dict = {
    "#1":4,
    "#2":4,
    "#3":2,
}

new_set=set(new_dict.keys())
old_set=set(old_dict.keys())
# print(new_set)
# print(old_set)

remove_set = old_set.difference(new_set) #找出new_set中不存在的
add_set = new_set.difference(old_set) #找出old_set中不存在的
update_set = old_set.intersection(new_set) # #返回一个新的set包含 old_set 和 new_set中的公共元素
print(remove_set)
print(add_set)
print(old_set)

s = set()

'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset'
 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

s1 = {11,22,33}
s2 = {11,22,44}
ss1=s1.difference(s2) #s1中的元素不在s2中挑出来
print(ss1)

s1.difference_update(s2) #s1中的元素不在s2中,并且把找到的元素更新到s1中去
print(s1)
s1 = {11,22,33}
s2 = {11,22,44}
s3=s1.intersection(s2) #找出s1，s2中都有的元素给到s3
print(s3)

s1.intersection_update(s2)
print(s1) #找出s1，s2中都有的元素,更新到s1中去

s1 = {11,22,33}
s2 = {11,22,44}
s4=s1.isdisjoint('11') #如果 11 元素在s1中就返回true
print(s4)

s1 = {11,22,33}
s2 = {11,22,44,33}
s3=s1.issubset(s2) #测试s1中每一个元素都在s2中

s1 = {11,22,33}
s2 = {11,22,44,33}
s3=s2.issuperset(s1) #和issubset相反，测试s2中有没有s1的所以元素
print(s3)


s1 = {11,22,33}
s2 = {11,22,44,33}
s3=s1.symmetric_difference(s2) #不存在在s1中的元素 #44
print(s3)
s1.symmetric_difference_update(s2)
print(s1)  #不存在在s1中的元素 #44 ,并且更新s1
#
# t.add('x')            # 添加一项
# s.update([10,37,42])  # 在s中添加多项
# t.remove('H') # 删除一项
# len(s)  # set 的长度
# x in s # 测试 x 是否是 s 的成员
# x not in s   # 测试 x 是否不是 s 的成员
# s.issubset(t)
# s <= t  # 测试是否 s 中的每一个元素都在 t 中
# s.issuperset(t)
# s >= t  # 测试是否 t 中的每一个元素都在 s 中
# s.union(t)
# s | t  # 返回一个新的 set 包含 s 和 t 中的每一个元素
# s.intersection(t)
# s & t  # 返回一个新的 set 包含 s 和 t 中的公共元素
# s.difference(t)
# s - t  # 返回一个新的 set 包含 s 中有但是 t 中没有的元素
# s.symmetric_difference(t)
# s ^ t  # 返回一个新的 set 包含 s 和 t 中不重复的元素
# s.copy()  # 返回 set “s”的一个浅复制