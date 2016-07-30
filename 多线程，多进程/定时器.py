from  threading import  Timer

def foo():
    print("hello")


t=Timer(1,foo) # 当值等于1，的时候，延时一秒执行
t.start()
