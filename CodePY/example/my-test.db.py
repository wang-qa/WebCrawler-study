import sqlite3 as sl

# 数据库 连接 db_Name
con = sl.connect('my-test.db')  # 轻量级 如果不存在则自动创建并连接
WEB_URL = 'https://zhuanlan.zhihu.com/p/165371456'
# 数据库 创建 表
with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)

# 数据库 插入
sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
data = [
    (1, 'Alice', 21),
    (2, 'Bob', 22),
    (3, 'Chris', 23)
]
with con:
    con.executemany(sql, data)

# 表单 查询
with con:
    data = con.execute("SELECT * FROM USER ")
    for row in data:
        print(row)
