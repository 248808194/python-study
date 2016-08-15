import socket
ip_port = ("127.0.0.1",9999)


#买手机
s=socket.socket()

#拨号

s.connect(ip_port) #打给服务端
welcome_msg = s.recv(1024)
welcome_msg = str(welcome_msg,encoding="utf8")

#发消息
while True:
    send_date=input(">>:".strip()) #定义消息内容
    if len(send_date) == 0: continue
    s.send(bytes(send_date,"utf8"))
    if send_date == "exit":break #必须放在此处为了让服务器段也知道，我客户端关闭，首先客户端必须发送exit让服务端知晓

    #收消息
    rece_date = s.recv(1024)
    rece_date = str(rece_date,encoding="utf8")
    print(rece_date)
    #由于发送的是bytes流所以server端也是返回的bytes流
    # 所以需要str转换字符串

s.close()


















