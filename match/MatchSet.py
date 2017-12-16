# encoding: utf-8
import sys

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

reload(sys)
sys.setdefaultencoding('utf8')
from sqlalchemy import create_engine, Column, String

enginepsqli2b2 = create_engine("postgresql://postgres:postgres@192.168.249.131:5432/i2b2metadata", max_overflow=5,
                               encoding='utf8', echo=True)
enginepsqlChinese = create_engine("postgresql://postgres:postgres@59.110.164.110:5432/medicine", max_overflow=5,
                                  encoding='utf8',
                                  echo=True)
Base = declarative_base()


class Mecidine(Base):
    __tablename__ = 'i2b2'
    c_name = Column(String(2000))
    c_fullname = Column(String(2000), primary_key=True)
    tempName = Column(String(2000))
    tempNameAttr = Column(String(2000))

    def __init__(cls, c_name, tempName, tempNameAttr):
        self = cls
        self.c_name = c_name
        self.tempName = tempName
        self.tempNameAttr = tempNameAttr


class ChinesePharma(Base):
    __tablename__ = 'ChinesePharma'

    m_name = Column(String(255), primary_key=True)
    type = Column(String(255))


def queryMeciData():
    """
    查询metadata数据
    :rtype: object
    :return:
    """
    print "query start ...."
    DBSession = sessionmaker(bind=enginepsqli2b2)
    session = DBSession()
    alist = session.query(Mecidine).filter(Mecidine.c_fullname.like('%Medications%')).all()
    qlist = []
    for qs in alist:
        qlist.append(qs.c_name)
    print "元素数量%s" % len(qlist)
    session.commit()
    session.close()
    return qlist


def queryChineseData():
    """
    查询中国药典数据
    :rtype: object
    :return:
    """
    print "query start ...."
    DBSession = sessionmaker(bind=enginepsqlChinese)
    session = DBSession()
    alist = session.query(ChinesePharma).all()
    qlist = []
    for qs in alist:
        qlist.append(qs.m_name)
    session.commit()
    session.close()
    return qlist


def insertMeciData(data):
    """
    insert数据
    :param data:
    :return:
    """
    print "insert data start ...."
    DBSession = sessionmaker(bind=enginepsqli2b2)
    session = DBSession()
    session.merge(data)
    session.commit()
    session.close()
