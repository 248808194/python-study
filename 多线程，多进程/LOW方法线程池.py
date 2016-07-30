"""
1:线程为一个容器
2：取到一个少一个
3：无线程时候会等待
4：线程执行完毕，交还线程
"""

import queue
import threading
import time
class threadingpool:
    """
    1:threadingpool中利用 queue,threading来创建 一个最大包括5的队列 self._q
    2:getthread 从队列中取到一个队列值 其实就是线程类(threading.Thread)
    3：addthread 往队列中添加一个 threading.Thread线程类
    """
    def __init__(self,maxsize=5):
        self.maxsize = 5
        self._q = queue.Queue(maxsize)
        for i in range(maxsize):
            self._q.put(threading.Thread)

    def getthread(self):
        return self._q.get()

    def addthread(self):
        self._q.put(threading.Thread)
pool = threadingpool(5) #创建pool对象 将maxsize重新赋值为5

def task(arg,p):
    print(arg)
    time.sleep(1)
    p.addthread()#task2个变量一个是for 的i 值，，另外一个是pool对象
                    #1：打印出i值
                    #2：间隔一秒
                    #3：执行p.addthread()类中的方法，因为一个线程执行完毕后需要在创建一个线程，以满足，用完一个线程，归还线程的原则



for i in range(100):
    t = pool.getthread()
    obj = t(target=task,args=(i,pool,))
    obj.start()
    """
    1：获得一个队列，开启一个子线程，去执行 task函数，

    """
