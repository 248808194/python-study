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