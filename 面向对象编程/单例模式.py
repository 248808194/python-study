
#通过一个静态字段保存下它的状态，以后调用的时候都先去拿这个字段
class FOO:
    instance = None
    def __init__(self,name):
        self.name = name


    @classmethod
    def get_instance(cls):
        if cls.instance:
            return cls.instance
        else:
            obj = cls("zhoutao")
            cls.instance = obj
            return obj


a=FOO.get_instance()
a1=FOO.get_instance()
print(a)
print(a1)
