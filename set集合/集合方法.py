#set集合方法
#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
#  'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset'
#  'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

#集合中增加一个元素
a=set()
a.add('123abc')
print(a)

#更新一个集合
a=set('123')
b=set('abc')
a.update(b)
print(a)
a.update('456')
print(a)

#删除集合中某个元素
a={'5', 'c', '1', '2', 'a', '6', 'b', '4', '3'}
a.remove('5')
print(a)
#discard(obj)中的obj如果是set中的元素,就删除,如果不是,就什么也不做,do nothing.新闻就要对比着看才有意思呢.这里也一样.

a.discard('c')
a.discard("asdf") #没有元素的话使用discard是不会报错的
a.clear()
print(a)