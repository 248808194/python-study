import socket
ip_port = ("localhost",9999)


#买手机
s=socket.socket()

#拨号
s.connect(ip_port) #链接服务端，如果服务端有已经存在一个链接的话，挂起

#发消息
while True: #基于connect建立的连接来循环发送消息
    send_date=input(">>:".strip()) #定义消息内容
    if send_date == "exit":break
    if len(send_date) == 0: continue#必须放在此处为了让服务器段也知道，我客户端关闭，首先客户端必须发送exit让服务端知晓
    s.send(bytes(send_date,"utf8"))
    #收消息
    ready_tag = s.recv(1024)
    ready_tag = str(ready_tag,encoding="utf8")
    if ready_tag.startswith("R"): #2：客户端收到R开口的数据 将即将接受的数据长度赋值给msg_size
        msg_size =int(ready_tag.split("|")[-1])
    start_tag="Start"
    s.send(bytes(start_tag,encoding="utf8")) #3：客户端发送start 数据，请求server端发送数据

    recv_size = 0
    recv_msg=b''
    while recv_size < msg_size: #5：客户端循环接受数据，知道接受数据的大小大于或者小于 数据的长度，则停止接受
        recv_date =s.recv(1024)
        recv_msg+=recv_date
        recv_size+=len(recv_date)
        print(recv_msg)
        print("MSG SIZE %s RECE SIZE %s" %(msg_size,recv_size))
    print( str(recv_msg,encoding="UTF8") )

s.close()




















