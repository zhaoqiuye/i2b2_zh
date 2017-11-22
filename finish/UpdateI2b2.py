# encoding: utf-8
import psycopg2


def updateOrInsert(en, table):
    conn = psycopg2.connect(database="i2b2metadata", user="postgres", password="postgres", host="localhost",
                            port="5432")
    cur = conn.cursor()
    en = en.replace('\'', '\'\'')

    sql = "UPDATE " + table + " SET en_name='%s' WHERE c_name='%s'" % (en, en)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

