from multiprocessing import  Pool
import  time

def foo(arg):
    time.sleep(1)
    print(arg)






if __name__ == "__main__":
    pool = Pool(5)
    for i in range(10):
        pool.apply_async(func=foo,args=(i,))
    pool.close() #所有任务完成允许close
    # time.sleep(2)
    # pool.terminate() #表示立即终止任务
    pool.join()