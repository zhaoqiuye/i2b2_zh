# encoding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ChildrenDataImport import Children, ObservationFacts, ProviderDimension, EncounterMapping, PatientDimension

enginepsqli2b2 = create_engine("postgresql://postgres:postgres@59.110.164.110:5432/i2b2demodata", max_overflow=5,
                               encoding='utf8', echo=True)
enginepsqlCH = create_engine("postgresql://postgres:postgres@59.110.164.110:5432/CH", max_overflow=5, encoding='utf8',
                             echo=True)


def queryAllData():
    '''
    查询数据
    :return:
    '''
    print "query start ...."
    DBSession = sessionmaker(bind=enginepsqlCH)
    session = DBSession()
    alist = session.query(Children).all()
    qlist = []
    for qs in alist:
        print "病人信息id:%s,num:%s,birth:%s,sex:%s,age:%s" % (qs.PatientId, qs.MrNum, qs.Birthday, qs.Sex, qs.Age)
        qlist.append(Children(qs.MrNum, qs.Concept_dimension, qs.Birthday, qs.Age, qs.Sex))
    insertAllData(qlist)
    session.commit()
    session.close()


def insertAllData(qlist):
    '''
    插入数据
    :param queryList:
    :return:
    '''
    print "insert data ......."
    DBSession = sessionmaker(bind=enginepsqli2b2)
    session = DBSession()
    try:
        for ss in qlist:
            if ss.Concept_dimension == '败血症':
                en = EncounterMapping(ss.MrNum, ss.MrNum, ss.PatientId)
                ob = ObservationFacts(ss.MrNum, ss.PatientId, 'ICD9:038', 'LCS-I2B2:PEDIATRIC')
                obsex = ObservationFacts(ss.MrNum, ss.PatientId, 'DEM|SEX:m', 'LCS-I2B2:PEDIATRIC')
                oblive = ObservationFacts(ss.MrNum, ss.PatientId, 'DEM|VITAL:n', 'LCS-I2B2:PEDIATRIC')
                if ss.Sex == '2':
                    obsex = ObservationFacts(ss.MrNum, ss.PatientId, 'DEM|SEX:f', 'LCS-I2B2:PEDIATRIC')
                patientDimension = PatientDimension(ss.PatientId, ss.Birthday, ss.Sex, ss.Age)
                session.merge(en)
                session.merge(ob)
                session.merge(obsex)
                session.merge(oblive)
                session.merge(patientDimension)
                session.flush()
            session.commit()
            session.close()

    except:
        session.rollback()


if __name__ == '__main__':
    queryAllData()
