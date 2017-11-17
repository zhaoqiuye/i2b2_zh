# encoding: utf-8
import psycopg2
import codecs
import pymysql
import time
import TranslationRequests as translationApi


def selectI2b2(table):
    """
        从指定数据表中查询
        _:param table 指定数据表
    """
    conn = psycopg2.connect(database="i2b2metadata", user="postgres", password="postgres", host="192.168.249.131",
                            port="5432")
    # 获取执行查询的对象
    cur = conn.cursor()
    sql = "SELECT c_name FROM " + table + " WHERE c_name ~ '[^0-9]'limit 10"
    # 执行那个查询，这里用的是select语句
    cur.execute(sql)

    # 使用cur.rowcount获取结果集的条数
    numrows = int(cur.rowcount)
    # print numrows
    list = []
    # 循环numrows次，每次取出一行数据
    for i in range(numrows):
        # 每次取出一行，放到row中，这是一个元组(id,name)
        row = cur.fetchone()
        # 直接输出两个元素s
        r = row[0]
        s = translationApi.getZnFromApi(r)
        updateZn(s, r, table)


def selectZn(en):
    """
        传入英文获取中文
        _:param 英文
    """
    conn = pymysql.connect("127.0.0.1", user='root', db='translate', password="root", charset="utf8")
    en = en.replace('\'', '\\\'')
    cur = conn.cursor()
    sql = "SELECT zn FROM translation WHERE en='%s'" % en
    # print sql
    cur.execute(sql)
    # 使用cur.rowcount获取结果集的条数
    numrows = int(cur.rowcount)
    # print numrows
    for i in range(numrows):
        # 每次取出一行，放到row中，这是一个元组(id,name)
        row = cur.fetchone()
        # 直接输出两个元素s
        r = row[0]
        if not r:
            return None
        else:
            return row[0]


def updateZn(zn, en, table):
    """
        进行数据更新
        _:param zn
        _:param en
        _:param table
    """
    conn = psycopg2.connect(database="i2b2metadata", user="postgres", password="postgres", host="192.168.249.131",
                            port="5432")
    # 获取执行查询的对象
    cur = conn.cursor()
    en = en.replace('\'', '\'\'')
    if zn is None:
        sql = "UPDATE " + table + " SET c_name='%s' WHERE c_name='%s'" % (en + '待翻译', en)
        cur.execute(sql)
    else:
        sql = "UPDATE " + table + " SET c_name='%s' WHERE c_name='%s'" % (zn, en)
        cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    t1 = time.time()
    selectI2b2("table_access")
    t2 = time.time()
    time = t2 - t1
    print time
