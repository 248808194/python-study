import socket
ip_port = ("localhost",9999)


#买手机
s=socket.socket()

#拨号

s.connect(ip_port) #连接服务器端，如果服务端有链接，挂起

#发消息
while True:
    send_date=input(">>:".strip()) #基于connect建立的连接来循环发送消息
    if len(send_date) == 0: continue
    s.send(bytes(send_date,"utf8"))
    if send_date == "exit":break #必须放在此处为了让服务器段也知道，我客户端关闭，首先客户端必须发送exit让服务端知晓

    #解决粘包问题
    ready_tag = s.recv(1024) #Ready| 9998
    ready_tag = str(ready_tag,encoding="utf8")
    if ready_tag.startswith("Ready"):
        msg_size = int(ready_tag.split("|")[-1])
    start_tag = "Strat"
    s.send(bytes(send_date,encoding="utf8"))
    #收消息
    rece_date = s.recv(1024)
    rece_date = str(rece_date,encoding="utf8")
    print(rece_date)
    #由于发送的是bytes流所以server端也是返回的bytes流
    # 所以需要str转换字符串

s.close()
