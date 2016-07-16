#只要类后面加上一个括号，比如 foo是一个类， 创建对象obj等于 foo() 的时候 ( ## obj = foo()  ##  )  就会自动执行 类里面的__init__方法

"""
class foo:
    def __init__(self):
        print("自动执行init这个方法")

foo()
"""
#执行的结果为打印出 “自动执行init这个方法”

class sql:
    def __init__(self):
        self.host="192.168.1.1"
    def select(self,sql):
        print(sql)
        print(self.host)
    def update(slef,sql):
        print("update")


obj = sql()
obj.select("select * from someting")
obj.update("update something")

#上面例子其实可以变化成下面这样
class sql:
    def __init__(self,a1,a2,a3):
        self.a1=a1
        self.a2=a2
        self.a3=a3
        print(self.a1)
        print(self.a2)
        print(self.a3)
    def select(self,sql):
        print(sql)
        print(self.a1)
        print(self.a2)
        print(self.a3)
    def update(slef,sql):
        print("update")

obj = sql("123","456","789")
obj2 = sql("ABC","DEF","GHI")
#执行obj=sql("123","456","789")  的时候自动执行 sql类下面的init方法，将，123，456，789 三个参数分别赋值给 a1,a2,a3参数
#然后就可以定义self.a1就等于传入的a1参数





























