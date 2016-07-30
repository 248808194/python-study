class f1:
    def __init__(self,name): #
        self.name = name
        # print(name)
    def show(self):
        print("show")

class f2(f1): #f2类继承了f1类 子继承父，F2就是子类(派生类)，F1就是父类(基类)
    def bar(self):
        print("bar")

class f3(f2):
    def foo(self):
        print("F3")
    def show(self):
        print(self.name) #如果子类中的方法和父类的方法一样，自己的方法优先

FF=f3("zhoutao")
FF.show()

# ！！！！！非常重要
# 继承相当于把里面的东西复制过来，如果f1中传递了name这个变量就相当于吧f1中的init方法复制到f2中去就变成 f2其实就变成了如下这样
# class f1:
#      def __init__(self,name):
#         self.name = name
#         print(name)
#     def show(self):
#         print("show")

class f2(f1):
    def __init__(self,name): #
        self.name = name
        # print(name)
    def show(self):
        print("show")
    def bar(self):
        print("bar")

###非常重要，继承就是把对方的方法拿过来，如果相同自己的方法优先级高
