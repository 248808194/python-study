import socketserver
import subprocess

class MyServer(socketserver.BaseRequestHandler):
    def handle(self): #方法的名字必须是handle方法，必须是，定死的
        self.request.sendall(bytes("welcom to the 10086 ,按1转人工: ",encoding="utf8"))
        while True:
            data= self.request.recv(1024)
            print("[%s] says: %s" %(self.client_address,data.decode() ))
            cmd = subprocess.Popen(data.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            cmd_res = cmd.stdout.read()
            if not cmd_res:
                cmd_res = cmd.stderr.read()
            if len(cmd_res) == 0:
                cmd_res = bytes("cmd has not output",encoding="utf8")
            self.request.sendall(cmd_res)




if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("0.0.0.0",9999),MyServer)
    server.serve_forever()


#每进来一个新连接，就实例化一次MyServer这个类

