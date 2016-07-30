
"""
练习一：在终端输出如下信息

小明，10岁，男，上山去砍柴
小明，10岁，男，开车去东北
小明，10岁，男，最爱大保健
老李，90岁，男，上山去砍柴
老李，90岁，男，开车去东北
老李，90岁，男，最爱大保健

"""

class foo:
    def __init__(self,name,age,xingbie):
        self.name=name
        self.age=age
        self.xingbie=xingbie
    def kc(self):
        print("%s %s %s 上山去砍柴 " %(self.name,self.age,self.xingbie))
    def qdb(self):
        print("%s %s %s 开车去东北 "  %(self.name,self.age,self.xingbie))
    def dbj(self):
        print("%s %s %s 最爱大保健 "  %(self.name,self.age,self.xingbie))

obj = foo("小明",'18岁',"男")
obj.kc()
obj.qdb()
obj.dbj()

