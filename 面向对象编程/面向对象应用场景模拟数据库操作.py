#连接mysql数据库 分别执行
# 1：select * from taba,
# 2：update taba set a=a where a=0
# 3：insert into taba (id, username, password) VALUES (1,user1,123456)
# 4: delete from taba where a=0

#数据库信息
# 用户名 root
#密码    123456
#地址 master.mydb.com
#端口 3306
dbinfo = {
    "username":"root",
    "password":"123456",
    "host":"master.mydb.com",
    "port":"3306"
}

class foo:
    def __init__(self):
        self.uname = dbinfo["username"]
        self.upasswd = dbinfo["password"]
        self.dbhost = dbinfo["host"]
        self.uport = dbinfo["port"]
    def select(self):
        print('mysql -u%s -p%s  -h%s -P%s -e "select * from taba"' %(self.uname,self.upasswd,self.dbhost,self.uport))
    def update(self):
        print('mysql -u%s -p%s  -h%s -P%s -e "update taba set a=a where a=0"' %(self.uname,self.upasswd,self.dbhost,self.uport))
    def insert(self):
        print('mysql -u%s -p%s  -h%s -P%s -e "insert into taba (id, username, password) VALUES (1,user1,123456)"' %(self.uname,self.upasswd,self.dbhost,self.uport))
    def delete(self):
        print('mysql -u%s -p%s  -h%s -P%s -e "delete from taba where a=0"' %(self.uname,self.upasswd,self.dbhost,self.uport))

obj = foo()
obj.select()
obj.update()
obj.insert()
obj.delete()