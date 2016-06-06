def logger(func):
    def inner(*args,**kwargs):
        print "arguments were: %s,%s" %(args,kwargs)
        return func(*args,**kwargs)
    return inner


foo1