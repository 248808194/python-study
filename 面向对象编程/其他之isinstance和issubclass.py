#isinstance 查看对象是否是某个类创建的
class BAR:
    pass


class FOO(BAR):
    pass

obj = FOO()
ret = isinstance(obj,FOO)
print(ret)

ret1 = issubclass(FOO,BAR) #前面子，后面父
print(ret1)

ret2 = isinstance(obj,BAR) #如果是obj类型的父类，也可以是true
print(ret2)

#查看类是不是某个类的子类就用issubclass