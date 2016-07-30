#队列之间数据共享常见的有三种方式
#queues
#arrey
#Manager。dict
#
# from multiprocessing import  Process
# from multiprocessing import  queues
# import multiprocessing
#
# def foo(i,arg):
#     arg.put(i)
#     print(i,arg.qsize())
#
#
# if __name__ == "__main__":
#     li = queues.Queue(20,ctx=multiprocessing)
#     for i in range(10):
#         p = Process(target=foo,args=(i,li))
#         p.start()



#
# from multiprocessing import  Process
# from multiprocessing import  queues
# import  multiprocessing
# from multiprocessing import  Array
#
# def foo(i,arg):
#     arg[i] = i+ 100
#     for item in arg:
#         print(item)
#     print("-------------")
#
#
# if __name__ == "__main__":
#     li = Array("i",10)
#     for i in range(10):
#         p = Process(target=foo,args=(i,li,))
#         p.start()




from multiprocessing import  Process
from multiprocessing import  queues
import multiprocessing
from multiprocessing import Manager
import  time
def foo(i,arg):
    arg[i] = i+100
    print(arg)


if __name__ == "__main__":
    li = Manager().dict()
    for i in range(10):
        p = Process(target=foo,args=(i,li))
        p.start()
        p.join() #如果不加join或者超时，因为li是主进程创建的主进程结束后，子进程就无法去访问主进程的数据

    # time.sleep(10)