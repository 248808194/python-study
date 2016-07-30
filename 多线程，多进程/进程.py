#进程，进程之间的数据共享
#默认进程之间是无法共享数据的


from multiprocessing import  Process


def foo(i):
    print("hi",i)


if __name__ == "__main__":
    for i in range(10):
        p = Process(target=foo,args=(i,))
        p.start()

