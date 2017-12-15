# encoding: utf-8
import sys

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

reload(sys)
sys.setdefaultencoding('utf8')
from sqlalchemy import create_engine, Column, String, Integer

enginepsqli2b2 = create_engine("postgresql://postgres:postgres@59.110.164.110:5432/i2b2metadata", max_overflow=5,
                               encoding='utf8', echo=True)
enginepsqlChinese = create_engine("postgresql://postgres:postgres@59.110.164.110:5432/medicine", max_overflow=5,
                             encoding='utf8',
                             echo=True)
Base = declarative_base()


class Mecidine(Base):
    __tablename__ = 'i2b2'
    c_name = Column(String(2000))
    c_fullname = Column(String(2000), primary_key=True)

    def __init__(cls, c_name, c_fullname):
        self = cls
        self.c_fullname = c_fullname
        self.c_name = c_name


class ChinesePharma(Base):
    __tablename__ = 'ChinesePharma'
    name = Column(String(255), primary_key=True)
    type = Column(String(50))

    def __init__(cls, name, type):
        self = cls
        self.name = name
        self.type = type


def queryMeicData():
    '''
    查询数据
    :rtype: object
    :return:
    '''
    print "query start ...."
    DBSession = sessionmaker(bind=enginepsqli2b2)
    session = DBSession()
    alist = session.query(Mecidine).filter(Mecidine.c_fullname.like('%Medications%')).all()
    qlist = []
    for qs in alist:
        qlist.append(qs.c_name)
    session.commit()
    session.close()
    return qlist


def queryChineseData():
    '''
    查询数据
    :rtype: object
    :return:
    '''
    print "query start ...."
    DBSession = sessionmaker(bind=enginepsqlChinese)
    session = DBSession()
    alist = session.query(Mecidine).filter(Mecidine.c_fullname.like('%Medications%')).all()
    qlist = []
    for qs in alist:
        qlist.append(qs.c_name)
    session.commit()
    session.close()
    return qlist


if __name__ == '__main__':
    result = queryMeicData()
    for i in result:
        print i
