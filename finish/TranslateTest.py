# encoding: utf-8
import psycopg2
import codecs
import pymysql
import time
import TranslationRequests as translationApi
import UpdateI2b2 as updateApi
import OpenFile as openfileApi


def selectI2b2(table):
    """
        从指定数据表中查询
        _:param table 指定数据表
    """
    conn = psycopg2.connect(database="i2b2metadata", user="postgres", password="postgres", host="localhost",
                            port="5432")
    # 获取执行查询的对象
    cur = conn.cursor()
    sql = "SELECT c_name FROM " + table + " WHERE c_name ~ '[^0-9]'and en_name is null"
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
        # 待翻译的英文
        r = row[0]
        print r
        #翻译的中文
        s = translationApi.getZnFromApi(r)
        print s
        updateZn(s, r, table)


def updateZn(zn, en, table):
    """
        进行数据更新
        _:param zn
        _:param en
        _:param table
    """
    print("zn:"+zn+"en:"+en)
    updateApi.updateOrInsert(en, table)
    conn = psycopg2.connect(database="i2b2metadata", user="postgres", password="postgres", host="localhost",
                            port="5432")
    # 获取执行查询的对象
    cur = conn.cursor()
    en = en.replace('\'', '\'\'')
    # zn = zn.replace('\'', '\'\'')
    if zn is None:
        sql = "UPDATE " + table + " SET c_name='%s' WHERE c_name='%s'" % (en + '待翻译', en)
        print sql
        cur.execute(sql)
    else:
        sql = "UPDATE " + table + " SET c_name='%s' WHERE c_name='%s'" % (zn, en)
        print sql
        cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    print "beginning ......"
    t1 = time.time()
    tb = openfileApi.openfile()
    print tb
    selectI2b2(tb)
    t2 = time.time()
    time = t2 - t1
    print time
