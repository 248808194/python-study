import  pymysql

class mysql_helper:
    def __int__(self):
        pass

    def get_dict(self,sql,params):
        conn = pymysql.connect(host= "localhost",user="root",password="newbie",db="xudaye")
        cur = conn.cursor()
        cur.execute(sql)
        # date = cur.fetchall()
        date = cur.fetchone()
        cur.close()
        conn.close()
        return date


helper = mysql_helper()
sql = "select * from user limit 1"
params =1
a=helper.get_dict(sql,params)
print(a,type(a))
