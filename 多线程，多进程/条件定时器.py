#条件

import threading

# def func(i,con):
#     print(i)
#     con.acquire()
#     con.wait()
#     print(i+100)
#     con.release()
#
# c=threading.Condition()
#
# for i in range(10):
#     t=threading.Thread(target=func,args=(i,c,))
#     t.start()
#
#
# while True:
#     inp = input(">>>>:")
#     if inp  == "q":
#         break
#     c.acquire()
#     c.notify(int(inp)) #这三行为格式,当notify条件传了几个就出去几个
#     c.release()


#条件的另外一种方式
def condition():
    ret = False
    inp = input(">>>:")
    if inp == "true":
        ret = True
    else:
        ret = False
    return ret



def func(i,con):
    print(i)
    con.acquire()
    con.wait_for(condition) #源码里面自己会去执行这个函数
    print(i+100)
    con.release()

c=threading.Condition()

for i in range(10):
    t=threading.Thread(target=func,args=(i,c,))
    t.start()


