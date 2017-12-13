# encoding: utf-8
# sqlalchemy 测试
import random
import time
from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint, Index, TIMESTAMP, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
b_list = range(200000, 299999)


class PatientDimension(Base):
    '''
    patient 映射
    '''
    __tablename__ = 'patient_dimension'

    patient_num = Column(Integer, primary_key=True)
    vital_status_cd = Column(String(50))
    birth_date = Column(TIMESTAMP(6))
    death_date = Column(TIMESTAMP(6))
    sex_cd = Column(String(50))
    age_in_years_num = Column(Integer)
    language_cd = Column(String(50))
    race_cd = Column(String(50))
    marital_status_cd = Column(String(50))
    religion_cd = Column(String(50))
    zip_cd = Column(String(10))
    income_cd = Column(String(50))
    statecityzip_path = Column(String(700))
    update_date = Column(TIMESTAMP(6))
    download_date = Column(TIMESTAMP(6))
    import_date = Column(TIMESTAMP(6))
    sourcesystem_cd = Column(String(50))

    def __init__(cls, patient_num):
        self = cls
        self.patient_num = patient_num


class Children(Base):
    '''
    病案首页
    '''

    __tablename__ = '病案首页20170928'

    PatientId = Column('id', Integer, primary_key=True, autoincrement=True)
    MrNum = Column('病案号', Text)
    Concept_dimension = Column('出院诊断其他诊断4', Text)

    def __init__(cls, MrNum, concept_dimension):
        self = cls
        self.PatientId = random.sample(b_list, 1)[0]
        self.MrNum = MrNum
        self.Concept_dimension = concept_dimension


class EncounterMapping(Base):
    '''
    encounter_mapping映射
    '''
    __tablename__ = 'encounter_mapping'

    encounter_ide = Column(String(200), primary_key=True)
    encounter_ide_source = Column(String(50), primary_key=True)
    project_id = Column(String(50), primary_key=True)
    encounter_num = Column(Integer)
    patient_ide = Column(String(200), primary_key=True)
    patient_ide_source = Column(String(50), primary_key=True)
    encounter_ide_status = Column(String(50))
    upload_date = Column(TIMESTAMP)
    update_date = Column(TIMESTAMP)
    download_date = Column(TIMESTAMP)
    import_date = Column(TIMESTAMP)
    sourcesystem_cd = Column(String(50))

    def __init__(cls, encounter_ide, encounter_num, patient_ide):
        '''
        初始化并赋值
        :param encounter_ide:
        :param encounter_num:
        :param patient_ide:
        '''
        self = cls
        self.patient_ide = str(patient_ide)
        self.encounter_num = encounter_num
        self.encounter_ide = encounter_ide
        self.download_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.import_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.update_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.upload_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.encounter_ide_source = 'HIVE'
        self.patient_ide_source = 'HIVE'
        self.encounter_ide_status = 'A'
        self.project_id = 'demo'


class ProviderDimension(Base):
    '''
    provider_dimension 映射
    '''
    __tablename__ = 'provider_dimension'
    provider_id = Column(String(50), primary_key=True)
    provider_path = Column(String(700), primary_key=True)
    name_char = Column(String(850))
    provider_blob = Column(Text)
    update_date = Column(TIMESTAMP)
    download_date = Column(TIMESTAMP)
    import_date = Column(TIMESTAMP)
    sourcesystem_cd = Column(String(50))
    upload_id = Column(Integer)

    def __init__(cls):
        self = cls
        self.provider_id = 'LCS-I2B2:D100002017'
        self.provider_path = '\\i2b2\\Providers\\beijing,children hospital'
        self.name_char = 'beijing,children hospital'
        self.download_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.import_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.update_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.sourcesystem_cd = 'DEMO'
        self.upload_id = 29


class ObservationFacts(Base):
    '''
    observation_facts
    '''
    __tablename__ = 'observation_fact'
    encounter_num = Column(Integer, primary_key=True)
    patient_num = Column(Integer, primary_key=True)
    concept_cd = Column(String(50), primary_key=True)
    provider_id = Column(String(50), primary_key=True)
    start_date = Column(TIMESTAMP)
    modifier_cd = Column(String(100))
    instance_num = Column(Integer)
    valtype_cd = Column(String(50))
    tval_char = Column(String(255))
    text_search_index = Column(Integer)
    ob_list = range(100000, 199999)

    def __init__(cls, encounter_num, patient_num, concept_cd, provider_id):
        self = cls
        self.concept_cd = concept_cd
        self.patient_num = patient_num
        self.encounter_num = encounter_num
        self.provider_id = provider_id
        self.start_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.modifier_cd = '@'
        self.instance_num = 1
        self.valtype_cd = 'N'
        self.tval_char = 'E'
        self.text_search_index = random.sample(self.ob_list, 1)[0]

# creatDatabaseMysql()
# pa=PatientDimension()
# pa.patient_num="45681"
# pa.age_in_years_num=14
# pa.sex_cd="M"
# pa.birth_date="2016-01-15"
# pa.marital_status_cd="single"
# pa.race_cd="asian"
# insertAllData(pa)
