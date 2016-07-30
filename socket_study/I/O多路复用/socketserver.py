import socket
import select

sk = socket.socket()
sk.bind(("127.0.0.1",9999))
sk.listen(5)

inputs = [sk] #默认sinpus里面只有连接对象自己
outputs = []
messages = {}
while True:
    rlist,wlist,e = select.select(inputs,outputs,[sk,],1) #while循环使用select.select来坚挺sk这个socket对象，第二个参数写什么 w参数就是什么值
    print(len(inputs),len(rlist),len(wlist),len(outputs))
    #监听sk（服务端）对象，如果sk发生变化，则表示有客户端连接进来，此时r值为sk
    #监听conn，如果conn发生变化，表示客户端有新系消息发过来，此时rlist值为（客户端）

    for  r in rlist:
        if r == sk:#1：新客户端来连，2：当rlist有内容，循环执行1：先打印出r，在将conn,addree = r.accept() 来接受客户端请求，然后在发送给客户端hello消息
            conn,address = r.accept() #conn通信管道，也是一个socket对象，一个连接过来会创建一个conn，如果A客户端连接过来，会为a创建一个conn对象
            inputs.append(conn) #发送完hello之后，回到while循环继续监听
            messages[conn] = []
            conn.sendall(bytes("hello",encoding="utf8"))
        else:#有人给我发消息
            try: #用户断开连接，判断接受的返回值，如果是none，则在inputs列表中移除conn
                ret = r.recv(1024)
                if not ret:
                    raise Exception("connect close")
                else:
                    outputs.append(r)
                    messages[r].append(ret)
            except Exception as e:
                inputs.remove(conn)
                del messages[r]

    for w in wlist:
        msg = messages[w].pop()
        resp = msg+bytes("respones",encoding="utf8")
        w.sendall(resp)
        outputs.remove(w)

#默认自由sk自己，有几个人来连接inputs就会加几，
#建立连接rlist收到后会加1，消息收完，在置为0
