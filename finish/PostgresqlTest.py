# encoding: utf-8
# 将需要翻译取出来放到翻译列表中
import psycopg2
import codecs
import pymysql


def DataToMysql(list):
    conn = pymysql.connect("127.0.0.1", user='root', db='translate', password="root")

    cur = conn.cursor()
    i = 0
    result = cur.execute("SELECT * FROM  translation")
    # if result >= 64:
    #     for a in list:
    #         sql = "UPDATE translation SET en='" + a + "' WHERE en='" + a + "'"
    #         cur.execute(sql)
    # else:
    cur.executemany("INSERT INTO translation(en) VALUES(%s)", list)

    conn.commit()
    cur.close()
    conn.close()


def selectI2b2Data(birn):
    conn = psycopg2.connect(database="i2b2metadata", user="postgres", password="postgres", host="192.168.249.131",
                            port="5432")  # 获取执行查询的对象
    cur = conn.cursor()
    sql = "SELECT DISTINCT c_name FROM " + birn + " WHERE c_name ~ '[^0-9]'"
    print sql
    # 执行那个查询，这里用的是select语句
    cur.execute(sql)

    # 使用cur.rowcount获取结果集的条数
    numrows = int(cur.rowcount)
    print numrows
    list = []
    # 循环numrows次，每次取出一行数据
    for i in range(numrows):
        # 每次取出一行，放到row中，这是一个元组(id,name)
        row = cur.fetchone()
    # 直接输出两个元素
    list.append(row[0])
    DataToMysql(list)


if __name__ == '__main__':
    selectI2b2Data("table_access")
