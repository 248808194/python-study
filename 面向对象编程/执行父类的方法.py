#通过super主动的执行父类的方法

class C1:
    def f1(self):
        print("C1_F1")

class C2(C1):
    def f1(self):
        print("C2_F1")
        super(C2,self).f1()


obj = C2()
obj.f1()

# 适用那个场景
