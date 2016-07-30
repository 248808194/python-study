class f1:
    def foo(self):
        print("f1_foo")

class f2(f1):
    def bar(self):
        print("f2_bar")
        super(f2,self).foo() #直接在自己里面，执行父类的foo方法


#执行类中的某个方法

f2().bar()
