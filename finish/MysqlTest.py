# encoding: utf-8
import MySQLdb as mdb
import sys

# 获取mysql的链接对象
con = mdb.connect('localhost', 'root', 'root', 'test', charset="utf8");

with con:
    # 获取执行查询的对象
    cur = con.cursor()

    # 执行那个查询，这里用的是select语句
    cur.execute("SELECT * FROM user")

    # 使用cur.rowcount获取结果集的条数
    numrows = int(cur.rowcount)

    # 循环numrows次，每次取出一行数据
    for i in range(numrows):
        # 每次取出一行，放到row中，这是一个元组(id,name)
        row = cur.fetchone()
        # 直接输出两个元素
        print row[0], row[1]
