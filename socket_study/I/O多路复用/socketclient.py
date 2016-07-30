import socket
ip_port = ("127.0.0.1",9999)


#买手机
s=socket.socket()

#拨号

s.connect(ip_port) #连接服务器端，如果服务端有链接，挂起


while True:
    a=input(">>>>>: ")
    s.sendall( bytes(a,encoding="utf8") )
    print(s.recv(1024))

s.close()
