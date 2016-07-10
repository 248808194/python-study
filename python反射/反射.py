
#example 1
def run():
    inp = input("enter you input:")
    m,f = inp.split('/')
    obj = __import__(m,fromlist=True)
    print(obj)
    if hasattr(obj,f):
        func=getattr(obj,f)
        func()
    else:
        print("404")


# run()
def run():
    while True:
        inp = input("enter you input:")
        m,f = inp.split('/')
        obj = __import__("lib."+m,fromlist=True)
        print(obj)
        if hasattr(obj,f):
            func=getattr(obj,f)
            func()
        else:
            print("404")


run()

