# encoding: utf-8
from timeit import Timer

import psycopg2
import time


def timeStatics():
    conn = psycopg2.connect(database="i2b2metadata", user="postgres", password="postgres", host="localhost",
                            port="5432")

    with conn:
        # 获取执行查询的对象
        cur = conn.cursor()
        sql = "SELECT count(1) FROM i2b2 " + " WHERE c_name ~ '[^0-9]'AND en_name IS NULL"
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
            r = row[0]
            print("剩余翻译的数量%s" % r)


if __name__ == '__main__':
    while True:
        timeStatics()
        time.sleep(3600)
