#对象中封装对象(传递对象) #可以防装多各对象
class C1:
    def __init__(self,name,obj):
        self.name = name
        self.obj = obj

class C2:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def show(self):
          return self.name
class C3:
    def __init__(self,aC1):
        self.name = aC1.obj.name
        self.c1name = aC1.name
        # print(self.name)
        # print(self.c1name)
        self.aC1=aC1
#!!!重要对象传递


c2_obj = C2("ZHOUTAO",18)
#c2下面 name = zhoutao
#C2下面 age = 18
#C2下面 show 方法
c1_obj = C1("zhoutaoc1",c2_obj) #c1对象中的obj等于C2_OBJ这个对象，
#c1下面 name = zhoutaoc1
#  c2_obj
c3_obj = C3(c1_obj)
#c3下面传递了C1_OBJ 这个对象
# c1_obj.obj.show() #执行c1_obj.obj.show(),其实就是执行c2 类下面的show 方法
#如果封装了一个类，同时也把封装类中的参数拿过来
#!!!通过C2_OBJ执行 show方法
# c3_obj.aC1.obj.show()
# c2_obj.show()

#函数里面一定要有返回值才行，比如下面的例子
result= c3_obj.aC1.obj.show()
print(result)
"""
#以上可以在用数据库场景来解释，例子如下

dbinfo = {
    "username":"root",
    "password":"123456",
    "host":"master.mydb.com",
    "port":"3306"
}

class foo:
    def __init__(self):
        self.uname = dbinfo["username"]
        self.upasswd = dbinfo["password"]
        self.dbhost = dbinfo["host"]
        self.uport = dbinfo["port"]
    def select(self):
        print('mysql -u%s -p%s  -h%s -P%s -e "select * from taba"' %(self.uname,self.upasswd,self.dbhost,self.uport))

class foo2():
    def __init__(self,obj):
        self.name = obj.uname
        print(self.name)

obj = foo()
obj.select()

obj2= foo2(obj)

"""

