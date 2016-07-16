import  builtins
import pymysql

def conndb(): #连接数据库
    conn = pymysql.connect(host= "localhost",user="root",password="newbie",db="xudaye")
    cur = conn.cursor()
    a=123
    return conn,cur

def sqlupdate(conn,cur,sql): # #更新或插入操作
    _data = cur(sql)
    conn.commit()
    return  _data

def sqldelete(conn,cur,IDs): #删除
    sta=0
    for eachid in IDs.split(" "):
        sta+=cur.execute("delete from user where id =%d" %(int(eachid)))
    conn.commit()
    return sta

def sqlselect(cur,sql): #查询
    cur.execute(sql)
    return cur

def dbclose(conn,cur):#关闭连接
    cur.close()
    conn.close()



conn,cur = conndb()

while True:
    number = input("请选择以上四个操作：1、修改记录，2、增加记录，3、查询记录，4、删除记录.(按q为退出)")
    if number == "q":
        print("end excuting")
        break
    elif number == "1":
        sql = input("输入修改语句:")
        try:
            sqlupdate(conn,cur,sql)
            print("修改成功")
        except Exception as  ex:
            print(ex)
    elif number == "2":
        sql = input("输入更新语句:")
        try:
            sqlupdate(conn,cur,sql)
            print("更新成功")
        except Exception as ex:
            print(ex)
    elif number == "3":
        sql = input("输入查询语句：")
        try:
            cur = sqlselect(cur,sql)
            for item in cur:
                print(item)
                # print(""Id="+str(item[0])+" name="+item[1]")
        except Exception as ex:
            print(ex)
    elif  number == "4":
        IDs=input("请输入Id，并用空格隔开")
        try:
            sqldelete(conn,cur,IDs)
            print("删除成功")
        except Exception as  ex:
            print(ex)
            print("删除失败")
    else:
        print("输入错误")














