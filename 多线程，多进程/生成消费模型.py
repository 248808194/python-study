import threading
import queue
import time


q=queue.Queue(1000)

def product(arg):
    q.put(arg)

for i in range(1000):
    P=threading.Thread(target=product,args=(i,))
    P.start()


def custmer(arg):
    while True:
        print("拿到的队列是:----->",q.get())
        print("队列中剩余个数+++++++>",q.qsize())
        time.sleep(1)


for j in range(100):
    C=threading.Thread(target=custmer,args=(j,))
    C.start()
