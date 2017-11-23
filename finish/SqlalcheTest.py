# encoding: utf-8
# sqlalchemy 测试
from lib2to3.pytree import Base
from random import randint

from sqlalchemy import create_engine, Column, Integer, String, Text, MetaData, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base

'''
mysql method 
mysql+pymysql://fuzj:123123@127.0.0.1:3306/fuzj
postgresql
postgresql://scott:tiger@localhost/mydatabase
'''
enginepsql = create_engine("postgresql://postgres:root@localhost:5432/translation", max_overflow=5, encoding='utf8')
enginemysql = create_engine("mysql://root:root@localhost:3306/translate?charset=utf8", max_overflow=5, encoding='utf8')

Base = declarative_base()


class App(Base):
    def __init__(self):
        super(App, self)

    def __init__(cls, zn, en, id):
        cls.zn = zn
        cls.en = en
        cls.id = id

    __tablename__ = 'checklist'
    id = Column(Integer, primary_key=True, autoincrement=True)
    zn = Column(String(255))
    en = Column(String(255))

    __table_args__ = (
        UniqueConstraint('id', 'zn', name='uix_id_zn'),
        Index('ix_id_zn', 'zn', 'en'),
    )


def __str__(self):
    return "id:" + self.id + self.en + self.zn


def creatDatabaseMysql():
    Base.metadata.create_all(enginemysql)


def queryAllData():
    """
        查询数据
    """
    DBSession = sessionmaker(bind=enginepsql)
    session = DBSession()
    alist = session.query(App).all()
    qlist = []
    for qs in alist:
        qlist.append(App(qs.zn, qs.en, qs.id))
    insertAllData(qlist)
    session.commit()
    session.expunge_all()
    session.close()


def insertAllData(queryList):
    """
        插入数据
    """
    print "insert data ......."
    DBSession = sessionmaker(bind=enginemysql)
    session = DBSession()
    # session.add_all(queryList)
    # app=App()
    for ss in queryList:
        session.merge(ss)
    # session.add_all(queryList)

    session.commit()


if __name__ == '__main__':
    # creatDatabaseMysql()
    queryAllData()
