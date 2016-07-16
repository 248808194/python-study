import db_config
import pymysql
import time
import logging
#http://blog.csdn.net/u012734441/article/details/42047715

class CustomDatabase:
    error_code = ''  # MySql 错误号码
    error_msg = ''  # MySql 错误信息
    _conn = None  # 数据库 conn
    _cur = None  # 数据库游标
    _TIMEOUT = 30  # 默认超时 30 秒
    _timeout = 0  # 默认超时 基数

    def __init__(self,):
        self.dbname=db_config.db_config["DB_NAME"]
        self.dbport=db_config.db_config["DB_PORT"]
        self.dbhost=db_config.db_config["DB_HOST"]
        self.dbuser=db_config.db_config["DB_USER"]
        self.dbpasswd=db_config.db_config["DB_PASSWORD"]

        try:
            self.conn = pymysql.connect(
                host=self.dbhost,
                user=self.dbuser,
                password=self.dbpasswd,
                db=self.dbname
            )
        except Exception as ex:
            if self._timeout < self._TIMEOUT: #尝试失败连接
                jishuqi =10
                self._timeout += jishuqi
                self.__init__()
            else:
                self._conn = False
                self._cur = False
                print(ex)
        self.cur=self.conn.cursor()


    def query(self,sql):
        """
        查询操作
        """
        try:
            self.cur.execute("SET NAMES utf8")
            result = self.cur.execute(sql)
            return self.cur.fetchall()
        except Exception as ex:
            print(ex)
            return False

    def update(self,sql):
        """
    更新操作
        """
        try:
            self.cur.execute("SET NAMES utf8")
            result = self.cur.execute(sql)
        except Exception as  ex:
            result = False
            print(ex)

    def instrt(self,sql):
        """
        插入数据操作
        """
        emp_no = False
        try:
            self.cur.execute("SET NAMES utf8")
            self.cur.execute(sql)
            emp_no=self.cur.lastrowid
            self.conn.commit()
        except Exception as ex:
            print(ex)
            emp_no = False
        finally:
            return emp_no

    def __del__(self):
        pass


OBJ=CustomDatabase()
