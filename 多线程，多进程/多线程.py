import time
def foo(arg):
    time.sleep(5)
    print(arg)

import threading
t=threading.Thread(target=foo,args=(123,))
t.setDaemon(True) #表示主线程不等待子线程
t.start() #不代表当前线程会被立即执行
# t.join() #表示主线程到底等待，直线子线程执行完毕，加参数t.join(2)表示主线程最多等待2秒

print("123")

