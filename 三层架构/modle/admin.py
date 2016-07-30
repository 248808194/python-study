from utility.sql_helper import mysql_helper


class Admin():
    def __int__(self):
        self.__helper = mysql_helper()

    def get_name(self,id):
        sql = "select * from user where id = %s"

