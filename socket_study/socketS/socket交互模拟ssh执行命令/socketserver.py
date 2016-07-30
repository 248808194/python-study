import subprocess #导入执行命令模块
import socket
ip_port = ("localhost",9999) #定义元组

#买手机
s=socket.socket() #绑定协议生成套接字

#买手机卡
s.bind(ip_port)  #绑定ip+协议+端口，用来唯一标识一个进程，ip_port必须是元组

#开机
s.listen(1) #定义最大连接数

#待机，等待电话呼入

while True: #用来重复收到新的连接
    conn,addr = s.accept()  #接受客户端请求，返回conn（相当于一个特定的连接  ） addr是客户端ip+port
    #收消息
    while True: #用来基于一个链接重复收发消息
        try: #扑捉客户端异常关闭(ctrl+c)
            recv_date = conn.recv(1024) #收消息，阻塞
            if len(recv_date) == 0:break #如果客户端退出，服务段还出于conn阶段，为此判断reve_data如果是0的话直接break跳出循环
            if str(recv_date,encoding="utf8") == "exit":break  #服务端接受到exit，直接跳出循环breakbreak

            #发消息
            p = subprocess.Popen(str(recv_date,encoding="utf8"),shell=True,stdout=subprocess.PIPE) #执行系统命令win平台命令输出标准是gbk，需要转换
            res = p.stdout.read() #获取标准输出
            if len(res) == 0: #如果执行错误命令返回的是空，需要做判断，如果为空手动给一个send_date
                send_date = "command not found"
            else:
                send_date=str(res,encoding="gbk")#命令执行成功，转换成str格式 #字节gbk----->str----->字节 utf8
            send_date=bytes(send_date,encoding="utf8")

            #解决粘包问题
            ready_tag = "R|%s" %len(send_date)
            conn.send(bytes(ready_tag,encoding="utf8"))#1：server端告知client准备接受数据，发送R+接受数据的大小
            feedback = conn.recv(1024)
            feedback = str(feedback,encoding="utf8")
            if feedback.startswith("Start"): #4：server端接受到数据后，判断是否带有start关键字，如果有执行发送数据
                conn.send(send_date)

        except Exception:
            break

#挂电话
conn.close()
