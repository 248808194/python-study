"""
属性：
    具有方法的写作形式
    具有字段的访问形式
    通过字段的形式访问/执行了一个方法
    属性只伪造了字段的访问形式而已

    删除不是从内存中删除，是需要自己写代码去删除

"""

#"""
all = "zhoutao"

class SF1:
    country = "CN"
    def __init__(self,name):
        self.name = name
    def show(self):
        return self.name[3] #传递的是字符串zhoutao第三个元素
obj= SF1(all)
a=obj.show()
print(a)
#"""
#通过方法完成分页功能
class pager:
    def __init__(self,all_count):
        self.all_count = all_count
        print(self.all_count)
    @property
    def all_page(self):
        a1,a2 = divmod(self.all_count,10)
        if a2 == 0:
            return a1
        else:
            return a1+1
    @all_page.setter #
    def all_page(self,value):
        print(value)
    @all_page.deleter
    def all_page(self):
        print("del all_page")

p = pager(101)

# a=p.all_page()
# print(a)
####！！！！非常重要如果方法中加了一个@property 装饰器,可以不用括号来访问方法
b=p.all_page #自动执行20行-25行的方法
print(b)
a=p.all_count #
print(a)

p.all_count =102 #对字段重新赋值
print(p.all_count)
p.all_page = 111 #自动执行 27-28的方法
del p.all_page #删除属性 #自动执行30行-31行的方法
#！！！属性中如果想取值加上装饰器@property
#！！！属性中如果向重新设置值的话加上 setter属性就 ok了

#字段可以进行获取，设置，删除，