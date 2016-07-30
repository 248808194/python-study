#使用多线程 让一个变量自减1，
import  threading

#创建自减函数
num=100
def foo(l):
    global num
    l.acquire() #上锁
    num -=1
    print(num)
    l.release() #解锁

#使用线程锁
lock=threading.RLock()

#通过foo循环产生100个子进程，执行自减函数
for i in range(100):
    t=threading.Thread(target=foo,args=(lock,)) #将threading下的Lock方法，传递给foo函数调用
    t.start()