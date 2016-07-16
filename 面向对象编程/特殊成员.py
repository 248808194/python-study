"""
class f1:
    def __init__(self):
        print("init")
    def __del__(self):
        pass
    def __call__(self, *args, **kwargs):
        print("call")

# obj= f1() #类后面加（）执行__init__方法
# obj()     #对象后面加()执行 __call__方法
f1()() #f1()执行init方法在执行call方法 #这个是python变态的一个地方那个

"""
#str方法
"""
class f1:
    def __init__(self):
        print("init")
    def __str__(self):
        a="3"
        c="3"
        return a+c
    def __call__(self, *args, **kwargs):
        print("call")

obj = f1()
print(obj)
#如果定义了str方法，默认print(obj) 就是print str的时候默认是输出的对象在内存中的地址
#定义str方法，str中return什么就会输出什么
"""
#add方法
"""
class f1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        a="3"
        c="3"
        return a+c
    def __call__(self, *args, **kwargs):
        print("call")
    def __add__(self, other):
        temp = "%s + %d "% (self.name,other.age)
        return temp


obj1 = f1("zhoutao",30)
obj2 = f1("zhoutao1",33)
#obj1 = add 中的self
#obj2 = add中的other
result = obj1+obj2
print(result)# 结果就是zhoutao + 33


#__dict__拿到对象中封装所以的字段,并且以字典的形式呈现出来

a=obj1.__dict__
print(a)
"""
#__getitem__ ,__setitem__ ,__delitem__
#用于索引操作，如字典。以上分别表示获取、设置、删除数据
class FOO:
    def __getitem__(self, key):
        print("__getitem",key,type(key))
        print(key.start) # 如果通过切片方式访问的话，key.start就是切片的起始位置，ret1 = OBJ[1:4:9] 就是1
        print(key.stop)  # 如果通过切片方式访问的话，key.start就是切片的结束位置，ret1 = OBJ[1:4:9] 就是4
        print(key.step)  # 如果通过切片方式访问的话，key.start就是切片的补偿，ret1 = OBJ[1:4:9] 就是4

    def __setitem__(self, key, value):
        print("__setitem__",key,value)

    def __delitem__(self, key):
        print("__delitem__",key)


OBJ = FOO()
# result = OBJ["k1"] #自动执行 __getitem__方法
# OBJ["K2"] = "ZHOUTAO" #自动执行 __setitem__方法
# del OBJ["K1"] #自动执行__delitem__方法
ret1 = OBJ[1:4:9] #如果通过切片方式访问的话，key的类型就是slice类型#
OBJ[1:4] = [11,22,33]
del OBJ[1:4]
#__getitem slice(1, 4, None) <class 'slice'>

#__iter__实现类似迭代器

# class FOO:
#     def __iter__(self):
#         return iter([11,22,33,44])
#
# OJB = FOO()
#
# for item in OJB:
#     print(item)

class FOO:
    def __iter__(self):
        yield list([11,22,33,44])

OJB = FOO()

for item in OJB:
    print(item)


