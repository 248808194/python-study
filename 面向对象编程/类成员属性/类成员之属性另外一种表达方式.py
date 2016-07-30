
class pager:
    def __init__(self,all_count):
        self.all_count = all_count
    def f1(self):
        print("F1")
    def f2(self,value):
        print(value)

    def f3(self):
        print("F3")

    foo = property(fget=f1,fset=f2,fdel=f3) #只能传函数名 property fset fget fdel 都是 python 定义的
p = pager(101)
a=p.foo #这样就会自动执行 类中的f1方法 get
p.foo = "zhoutao"  #这样就会自动执行 类中的f2方法 set
del p.foo  #这样就会自动执行 类中的f3方法 del