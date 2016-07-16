#如果class C3(C1,C2) 写成这样就是C3把C1, C2 全部继承过来了。这是最基本的多继承
"""
class C1:
    def f1(self):
        pass

class C2:
    def f2(self):
        pass

class C3(C1,C2):
    def f3(self):
        pass
"""


#在多继承中，如果继承的父类中有2各同样的方法，按照继承关系则左边的优先级最高(最前面)

"""
class C1:
    def f2(self):
        print("C1F2")

class C2:
    def f2(self):
        print("C2F2")

class C3(C1,C2):
    def f3(self):
        pass

obj = C3()

obj.f2()
"""

#多继承中的嵌套单继承
class C0:
    def f2(self):
        print("C0F2")

class C1(C0):
    def f2(self):
        print("C1F2")

class C2:
    def f2(self):
        print("C2F2")

class C3(C1,C2):
    def f3(self):
        pass

obj = C3()

obj.f2()

#!!!!非常重要。寻找方式其实就是子类寻找如果没有就去父类找，如果父类是其他类的子类就继续向上找父类，找到低如果没有，就去同类中找 (理解为，一条道走到黑)