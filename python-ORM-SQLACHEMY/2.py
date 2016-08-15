#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:newbie@127.0.0.1:3306/world", max_overflow=5)

Base = declarative_base()

# 创建单表
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(16))

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )


# 一对多
class Favor(Base):
    __tablename__ = 'favor'
    nid = Column(Integer, primary_key=True)
    caption = Column(String(50), default='red', unique=True)


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    favor_id = Column(Integer, ForeignKey("favor.nid"))


# 多对多
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)


class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)


class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))


def init_db():
    Base.metadata.create_all(engine) #创建表函数


def drop_db():
    Base.metadata.drop_all(engine) #删除表删除表函数

init_db()

Session =sessionmaker(bind=engine) #通过session创建连接来操作表
session = Session()

#增

obj = Users(name="zt",extra="zttt")
session.add(obj)
session.add_all([
    Users(name="zhoutao",extra="newbie"),
    Users(name="zhoutao1",extra="newbie1"),
])
session.commit()



#删
# session.query( Users ).filter( Users.id > 2 ).delete()
# session.commit()


#改

# session.query(Users).filter(Users.id > 2).update({"name" : "099"})
# session.query(Users).filter(Users.id > 2).update({Users.name: Users.name + "099"}, synchronize_session=False) 在原有基础上修改，#False - 不对session进行同步，直接进行delete or update操作
session.query(Users).filter(Users.id > 2).update({"num": Users.num + 1}, synchronize_session="evaluate") #synchronize_session=“evaluate”用于数字
session.commit()


ret = session.query(Users).all() #查询所有
ret = session.query(Users.name, Users.extra).all() #
ret = session.query(Users).filter_by(name='alex').all()
ret = session.query(Users).filter_by(name='alex').first()