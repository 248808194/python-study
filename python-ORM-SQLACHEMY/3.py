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


class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

#执行创建表操作
def init_db():
    Base.metadata.create_all(engine)
init_db()
