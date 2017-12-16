# encoding: utf-8
import sys

from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.elements import and_

reload(sys)
sys.setdefaultencoding('utf8')
from sqlalchemy import create_engine, Column, String, Integer, Text, TIMESTAMP

from sqlalchemy.orm import sessionmaker

enginepsqli2b2 = create_engine("postgresql://postgres:postgres@59.110.164.110:5432/i2b2metadata", max_overflow=5,
                               encoding='utf8', echo=True)
Base = declarative_base()


class Mecidine(Base):
    __tablename__ = 'i2b2'

    c_hlevel = Column(Integer)
    c_name = Column(String(2000))
    c_fullname = Column(String(700), primary_key=True)
    c_synonym_cd = Column(String)
    c_visualattributes = Column(String(1))
    c_totalnum = Column(Integer)
    c_basecode = Column(String)
    c_metadataxml = Column(Text)
    c_facttablecolumn = Column(String(50))
    c_tablename = Column(String(50))
    c_columnname = Column(String(50))
    c_columndatatype = Column(String(50))
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


def insertMeciData():
    """
    insert数据
    :param data:
    :param data:
    :return:
    """
    print "insert data start ...."
    DBSession = sessionmaker(bind=enginepsqli2b2)
    session = DBSession()
    alist = session.query(Mecidine).filter(
        and_(Mecidine.c_fullname.like('%Medications%'), Mecidine.tempNameAttr != None)).all()
    print alist
    session.commit()
    session.close()


if __name__ == '__main__':
    flag=5
    if flag==2:
        ali=[1,5]
    if flag==5:
        ali=[2,9]
    print ali