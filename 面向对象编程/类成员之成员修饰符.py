#成员修饰符
    #共有 #在外部 内部进行访问就是公共的
    #私有 #在字段前面加上2个下划线(__):example self.__name = "zhoutao"”
    #私有 只有类本身成员内部可以访问，其他无法访问

"""
class FOO:
    def __init__(self,name):
        self.name = name #普通字段 =》默认情况是共有的
    def bar(self):
        print(self.name) #


obj = FOO("zhoutao")
print(obj.name) #类的外部进行调用

obj.bar() #类的内部进行调用 #！！！间接通过bar来访问这个name
"""


"""
class FOO:
    def __init__(self,name):
        self.__name = name #普通字段 =》默认情况是共有的
    def bar(self):
        print(self.name,"内部访问") #


obj = FOO("zhoutao")
#会报错obj.bar() #类的内部进行调用 #！！！间接通过bar来访问这个name
class FOO:
    def __init__(self,name):
        self.__name = name #普通字段 =》默认情况是共有的
    def bar(self):
        print(self.__name,"内部访问") #


obj = FOO("zhoutao")
obj.bar()
#会报错obj.bar() #类的内部进行调用 #！！！间接通过bar来访问这个name

"""

"""
#如果有继承关系 比如这样
class FOO:
    def __init__(self,name):
        self.__name = name
    def bar(self):
        print(self.__name)

class FOO2(FOO):
    def f2(self):
        print(self.__name)


obj = FOO2("zhoutao")
# obj.f2()  !!!!#实际是不能的，不管是继承(甭管是谁来就自己能，继承也不行 )
obj.bar()
"""

"""
#私有的静态字段
class FOO:
    __CC="Prv"
    def __init__(self,name):
        self.__name = name
    def bar(self):
        print(self.__name)

result = FOO.CC
print(result) #会报错，私有的静态字段外部是不能访问的
"""

"""
#私有的静态字段2
class FOO:
    __CC="Prv"
    def __init__(self,name):
        self.__name = name
    def bar(self):
        print(self.__name)
    def cc(self):
        print(FOO.__CC) #可以在内部函数中去调用静态字段
obj = FOO("zhoutao")
obj.cc()

"""

"""
#私有的静态字段3，如果不想定义对象直接访问静态字段
class FOO:
    __CC="Prv"
    def __init__(self,name):
        self.__name = name
    def bar(self):
        print(self.__name)
    @staticmethod  #@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
    def cc():
        print(FOO.__CC) #可以在内部函数中去调用静态字段
FOO.cc()

"""

"""
###！！！搞脑子即使是私有的其实也可以访问 不建议用，不到万不得已在外部强制访问私有成员
class FOO:
    __CC="Prv"
    def __init__(self,name):
        self.__name = name
    def bar(self):
        print(self.__name)

obj = FOO("zhoutao")
print(obj._FOO__name)
"""