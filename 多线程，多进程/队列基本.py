import queue

q=queue.Queue(20) #加参数表示最多接受多少个队列
q.put("11")
q.put("11")
q.put("13",block=False,timeout=3) #等3秒在将数据加入到队列中去# block 表示是否堵塞，block为False表示有堵塞就抛出异常
print(q.qsize())
print(q.get(block=False,timeout=3)) #get的时候默认是阻塞状态，
print(q.qsize())

#join,task_done 阻塞进程，当队列中任务执行完毕后，不阻塞