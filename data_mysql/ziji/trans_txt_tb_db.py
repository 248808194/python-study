import os
import sys
import random
import time
from CustomDatabase import  CustomDatabase
import string

def get_target_file_name():
    return [ x for x in os.listdir("./source_file") if os.path.splitext(x)[1] == ".txt" ]
"""
# print(os.path.isfile("data_1.txt")) #判断是否是文件返回的结果是True
# print(os.path.splitext("menu.py")[0]) #分割文件名与扩展名得到test
# print(os.path.splitext("menu.py")[1]) #分割文件名与扩展名得到py
获取文件名，返回的是一个列表['data_1.txt', 'data_10.txt', 'data_11.txt'...........]
"""

def get_randon_char():
    return random.sample(list(string.ascii_letters+string.digits),1 )[0]
    """
    string.accii_letters 获得 a-z的小写字符串
    string.accii_digits 获得0-9的字符串
    string.ascii_letters+string.digits 组合字符串
    用list内置函数转换列表得到【a-z0-9】
    randon.sample(在list中获取一个元素，拿到第0各元素)
    """

#
def handle_each_file(file_name):
    with open(file_name,"r",encoding="utf8") as f:
        flag = 0
        route_id = 0
        sell_out = 0
        info = {}
        for each_line in f.readlines():
            each_line=each_line.strip()
            if flag == 2:
                each_line_commit = each_line.replace(":",":",1).strip().split(":",1)#将中文分号替换成英文分号，并且以分号分割成列表,之分割一次，
                if len(each_line_commit) != 2:
                    return  False
                user_name = each_line_commit[0]
                user_commit = each_line_commit[1]
                info[user_name] = user_commit
                print(user_name)
                print(user_commit)

            if "route_id" in each_line and "@@" in each_line: #获得route_id和sell_out尝试用反射来做看看，后话
                flag =1
                try:
                    route_id = each_line.split("@@")[1].strip()
                    print(route_id)
                except Exception as  ex:
                    print(ex)

            if "sell_out" in each_line and "@@" in each_line:
                flag=2
                try:
                    sell_out=each_line.strip("@@")[1].strip()
                    print(sell_out)
                    print(flag,type(flag))
                except Exception as  ex:
                    print(ex)


def get_random_time(): #获取随机事件
    """
     #'2015-12-01 18:05:09'
    # 1448964309
    #
    # '2016-04-20 18:05:09'
    # 1461146709.0
    """
    random_time = random.randint(1448964309,1461146709)
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(random_time))

def import_data_to_db(data):
    for each_key in ["route_id","sell_out"]:
        if each_key not in data:
            return  False,9,u"key 有误"
    route_id = data["route_id"]
    sell_out = data["sell_out"]
    data.pop("route_id")
    data.pop("sell_out")
    user_name_list=data.key()
    db=CustomDatabase() #import CustomDatabase  定义db这个对象等于CustomDatabase这个类
    route_id_query = "select id from route_product where id = %d %route_id"
    route_id_result = db.query(route_id_query)
    if route_id_result is False:
        return False, 1, u'查询出错'
    if len(route_id_result) == 0:
        return False, 2, u'route_id对应数据不存在'
    route_sell_out_insert_sql = "insert into vr_route (route_id, sell_out) VALUES (%d, %d)" % (route_id, sell_out)
    route_insert_result= db.insert(route_sell_out_insert_sql)

    if route_insert_result is False:
        return 3,u"插入错误"
    for each_user in user_name_list:
        temp_each_user_name = each_user
        user_query_sql= "select id from user where nick = '%s' % temp_each_user_name"
        user_query_result=db.query(user_query_sql)
        try_time=0
        while True:
            if user_query_result is False:
                return False, 4, u'查询出错'
            if len(user_query_result) == 0:
                break
            if len(user_query_result) > 0:
                user_query_sql =  "select id from user where nick = '%s'" % temp_each_user_name
                user_query_result = db.query(user_query_sql)
            try_time+=1
            if try_time >10:
                return  False,5, u'插入次数过去'
        insert_user_sql="insert into user (nick, account_status) VALUES ('%s', 2)" % temp_each_user_name
        user_insert_id = db.insert(insert_user_sql)
        if user_insert_id is False:
            return False, 7, u'插入 comment 表出错'
            insert_vr_comment_sql = "insert into vr_comment (user_id, route_id, vr_route_id, message," \
                                    " dateline) VALUES (%d, %d, %d, '%s', '%s')" \
                                    % (
                                        user_insert_id, route_id, route_insert_result,
                                        data[each_user],
                                        get_random_time())
            vr_comment_insert_result = db.insert(insert_vr_comment_sql)
            if vr_comment_insert_result is False:
                return False, 8, u'插入 vr_comment 表出错'
    return 0,u,"批量插入成功"




if __name__ == "__main__":
    insert_fail_file_dict = {}
    current_abspath = os.path.abspath("./") #显示上层目录






# os.chdir(os.path.join(os.path.abspath("../")),"source_file")
a=os.path.join(os.path.abspath("../"))
a=os.path.join(os.path.abspath("./"),"source_file") #目录拼接
print(os.getcwd())



