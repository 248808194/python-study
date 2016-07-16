def foo(func):
    def bar():
        print("before")
        func()
        print("after")
    return  bar

@foo
def f1():
    print("f1")

f1()