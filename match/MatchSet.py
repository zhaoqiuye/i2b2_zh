# encoding: utf-8
import sys

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

reload(sys)
sys.setdefaultencoding('utf8')
from sqlalchemy import create_engine, Column, String, Integer, Text, TIMESTAMP, and_

enginepsqli2b2 = create_engine("postgresql://postgres:postgres@localhost:5432/i2b2metadata", max_overflow=5,
                               encoding='utf8', echo=True)
enginepsqlChinese = create_engine("postgresql://postgres:postgres@localhost:5432/medicine", max_overflow=5,
                                  encoding='utf8',
                                  echo=True)
Base = declarative_base()


class Mecidine(Base):
    __tablename__ = 'i2b2'

    c_hlevel = Column(Integer, primary_key=True)
    c_name = Column(String(2000), primary_key=True)
    c_fullname = Column(String(700), primary_key=True)
    c_synonym_cd = Column(String, primary_key=True)
    c_visualattributes = Column(String(1), primary_key=True)
    c_totalnum = Column(Integer)
    c_basecode = Column(String)
    c_metadataxml = Column(Text)
    c_facttablecolumn = Column(String(50),primary_key=True)
    c_tablename = Column(String(50),primary_key=True)
    c_columnname = Column(String(50),primary_key=True)
    c_columndatatype = Column(String(50),primary_key=True)
    c_operator = Column(String(10))
    c_dimcode = Column(String(700))
    c_comment = Column(Text)
    c_tooltip = Column(String(900))
    m_applied_path = Column(String(700))
    update_date = Column(TIMESTAMP(6))
    download_date = Column(TIMESTAMP(6))
    import_date = Column(TIMESTAMP(6))
    sourcesystem_cd = Column(String(50))
    valuetype_cd = Column(String(50))
    m_exclusion_cd = Column(String(25))
    c_path = Column(String(700))
    c_symbol = Column(String(50))
    tempName = Column(String(2000))
    tempNameAttr = Column(String(50))

    def __init__(cls, c_hlevel, c_name, c_fullname, c_synonym_cd, c_visualattributes, c_totalnum,
                 c_basecode, c_metadataxml, c_facttablecolumn, c_tablename, c_columnname, c_columndatatype,
                 c_operator, c_dimcode, c_comment, c_tooltip, m_applied_path, update_date, download_date,
                 import_date, sourcesystem_cd, valuetype_cd, m_exclusion_cd, c_path, c_symbol,
                 tempName, tempNameAttr):
        self = cls
        self.c_name = c_name
        self.tempName = tempName
        self.tempNameAttr = tempNameAttr
        self.c_hlevel = c_hlevel
        self.c_fullname = c_fullname
        self.c_visualattributes = c_visualattributes
        self.sourcesystem_cd = sourcesystem_cd
        self.c_synonym_cd = c_synonym_cd
        self.c_totalnum = c_totalnum
        self.c_basecode = c_basecode
        self.c_metadataxml = c_metadataxml
        self.c_facttablecolumn = c_facttablecolumn
        self.c_tablename = c_tablename
        self.c_columnname = c_columnname
        self.c_columndatatype = c_columndatatype
        self.c_operator = c_operator
        self.c_dimcode = c_dimcode
        self.c_comment = c_comment
        self.c_tooltip = c_tooltip
        self.m_applied_path = m_applied_path
        self.update_date = update_date
        self.download_date = download_date
        self.import_date = import_date
        self.valuetype_cd = valuetype_cd
        self.m_exclusion_cd = m_exclusion_cd
        self.c_path = c_path
        self.c_symbol = c_symbol


class ChinesePharma(Base):
    __tablename__ = 'ChinesePharma'

    m_name = Column(String(255), primary_key=True)
    type = Column(String(255))


def queryMeciData(flag):
    """
    查询metadata数据
    :rtype: object
    :param: flag
    :return:
    """
    print "query start ...."
    DBSession = sessionmaker(bind=enginepsqli2b2)
    session = DBSession()
    print flag
    if flag == 'exp1':
        print 'exp1'
        alist = session.query(Mecidine).filter(Mecidine.c_fullname.like('%Medications%')).all()
    if flag == 'exp2':
        print 'exp2'
        alist = session.query(Mecidine).filter(
            and_(Mecidine.c_fullname.like('%Medications%'), Mecidine.tempNameAttr == None)).all()
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


def insertMeciData(cName, zname, flag):
    """
    update数据添加flag
    :param cName:
    :param flag:
    :return:
    """
    print "update data start ...."
    DBSession = sessionmaker(bind=enginepsqli2b2)
    session = DBSession()
    melist = session.query(Mecidine).filter(Mecidine.c_name == cName).all()
    for m in melist:
        me = Mecidine(m.c_hlevel, m.c_name, m.c_fullname, m.c_synonym_cd, m.c_visualattributes, m.c_totalnum,
                      m.c_basecode, m.c_metadataxml, m.c_facttablecolumn, m.c_tablename, m.c_columnname,
                      m.c_columndatatype,
                      m.c_operator, m.c_dimcode, m.c_comment, m.c_tooltip, m.m_applied_path, m.update_date,
                      m.download_date,
                      m.import_date, m.sourcesystem_cd, m.valuetype_cd, m.m_exclusion_cd, m.c_path, m.c_symbol,
                      zname, flag)
        session.merge(me)
        session.flush()
        session.commit()
    session.close()
