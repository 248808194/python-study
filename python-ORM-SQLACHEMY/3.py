#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date = 2016/8/15/15:14
# Python 3.5


from  sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,ForeignKey,UniqueConstraint,Index
from sqlalchemy.orm import  sessionmaker,relationship
from sqlalchemy import  create_engine

engine = create_engine("mysql+pymysql://zhoutao:123@192.168.77.129:3306/S13",max_overflow=5)

Base = declarative_base()


#一对多

class Group(Base):
    __tablename__ = "group"
    nid = Column(Integer,primary_key=True,autoincrement=True)
    caption = Column(String(32))
    __table_args__={
        "mysql_engine":"innodb",
        "mysql_charset":"utf8"
    }


class User(Base):
    __tablename__="user"
    nid = Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String(32))
    groupid=Column(ForeignKey("group.nid"))
    #仅用于查询方便
    group=relationship("Group",backref="uuu") #uuu指的是组里面所有用户
    __table_args__={
        "mysql_engine":"innodb",
        "mysql_charset":"utf8"
    }
    def __repr__(self): #利用类repr方法，返回 可阅读类型
        temp = "%s|%s|%s"%(self.nid,self.username,self.groupid)
        return  temp



def init_db():
    Base.metadata.create_all(engine)
init_db()

Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()
session.query(Group).delete()
session.commit()
session.add_all([
    Group(nid=3,caption="SA"),
    User(username="zhoutao",groupid=3)
])

session.commit()

ret =session.query(User).join(Group) #生成的sql语句
print(ret)
result = session.query(User.username,Group.caption).join(Group,isouter=True).all() #一对多连表查询 ,查询user表中的username 和group表里的caption
print(result)
#select * from user left join group on user.group_id = group.nid

#反向查找

obj = session.query(Group).filter(Group.caption == 'SA').first()
print(obj.nid)
print(obj.caption)
print(obj.uuu)