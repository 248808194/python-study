class foo:
    a="123"
    print(a,type(a))
    def __init__(self,a):
        self.a=a
        print(self.a)

obj =foo(456)

