class sql:
    def select(self,sql):
        print(sql)
        print(self.host)
    def update(slef,sql):
        print("update")


obj = sql()
obj.host="192.168.1.1"
obj.select("select * from someting")
obj.update("update something")

obj1 = sql()
obj1.host="192.168.1.111"
obj1.select("select * from someting111")
obj1.update("update 111something")



