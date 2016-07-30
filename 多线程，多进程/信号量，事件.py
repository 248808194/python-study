#使用多线程 让一个变量自减1，
import  threading
import time


#BoundedSemaphore
#创建自减函数
# num=100
# def foo(l,i):
#     global num
#     l.acquire() #上锁
#     time.sleep(10)
#     num -=1
#     print(num,i)
#     l.release() #解锁
#
# #使用线程锁
# lock=threading.BoundedSemaphore(5) #一次性最多允许5个线程执行
#
# #通过foo循环产生100个子进程，执行自减函数
# for i in range(30):
#     t=threading.Thread(target=foo,args=(lock,i)) #将threading下的Lock方法，传递给foo函数调用
#     t.start()


#event #批量将线程挡住，修改一个标识，放行线程，类似红绿灯


def foo(i,e):
    print(i)
    e.wait() #检测是什么等，如果是红灯，则停，如果eve.set(）则变成绿灯，则放行
    print(i)


eve = threading.Event() #
for i in range(10):
    t=threading.Thread(target=foo,args=(i,eve,))
    t.start()
    ####
eve.clear() #停止
inp = input(">>>>:")
if inp == "1":
    eve.set() #执行eve.set，等待的全部通过#绿灯

