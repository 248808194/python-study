"""
python中类成员
字段
    1：静态字段 #类中,静态字段在代码加载的时候已经创建
    2：动态字段 #对象中
方法
属性

"""

class Foo:
    CC = 123 #也是字段(静态字段)
    def __init__(self):
        self.name = "zhoutao" #普通字段(动态字段)
    def show(self):
        print(self.name)
"""
里面就包含两个方法一个字段，
方法1 __init__
方法2 show
字段 self.name
字段保存在对象里面
self.name = "zhoutao" #普通字段(动态字段)
CC = 123 #也是字段(静态字段)
静态字段属于类，动态字段属于这个对象
"""

#静态字段和动态字段的区别
class shengfen:

    def __init__(self,name):
        self.name = name
        self.country = "CN" #如果country保存为动态字段，如果有多个对象的时候，就会有很多self.country会浪费内存空间
        print(self.name)



class shengfen:
    country = "CN" #如果把country =CN定义为静态字段的话，只需要保存一份就行了。
    def __init__(self,name):
        self.name = name
        print(self.name)

#一般情况下自己访问自己的字段
obj = shengfen("上海")
obj = shengfen("江苏")
print(shengfen.country,"ABC") #一般情况下自己访问自己的字段 静态字段保存在类中就用类去访问，，
# ###!!!非常重要在python中静态字段可以用类访问，也可以用对象去访问，如下
# ###!!!非常重要,以后访问的话，动态字段只能用对象访问，
# ###!!!非常重要,以后访问的话，静态字段只能用类去访问，(万不得已的时候可以使用)
print(obj.country)
obj = shengfen("浙江")

#！！！非常重要，如果不创建对象的话，当类中定义了静态字段，也可以用类直接来访问这个字段如下所示
#!!!!! 内存中是没有self.name的 因为没有
# 没有创建对象不能自动执行__init__方法所有就没有
class SF:
    country = "CN"
    def __init__(self,name):
        self.name = name
        print(self.name)
print( SF.country)
# print(self.name) #会 报错


#额外自己想的,通过列表定义省名，然后通过for来循环调用对象
all = ["上海","浙江","江苏","安徽"]

class SF1:
    country = "CN"
    def __init__(self,name):
        self.name = name
        self.country="asdf"
        print(SF1.country,self.country,self.name)


for name in all:
    ojb= SF1(name)


