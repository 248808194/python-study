import  threading

class Mythread(threading.Thread):
    def __init__(self,func,arg):
        self.func= func
        self.arg = arg
        super(Mythread,self).__init__()


    def run(self):
        self.func(self.arg)

def f2(arg):
    print(arg)

obj = Mythread(f2,123)
obj.start()

