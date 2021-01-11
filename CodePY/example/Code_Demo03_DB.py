import sqlite3 as sl

student_date = [
    {
        'name': '小红',
        'sex': '女',
        'birthday': '20010101'
    }]


class DB:
    def __init__(self):
        # 数据库 初始化连接
        self.con = sl.connect('my-test.db')  # 轻量级 如果不存在则自动创建并连接

    # 数据库 创建 表
    def new_table(self):
        with self.con:
            # 定义表格式
            self.con.execute("""
                CREATE TABLE StudentINFO (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT INTEGER NOT NULL  ,
                    sex TEXT,
                    birathday TEXT
                );
            """)

        # 数据库 插入

    def add_data(self):
        sql = 'INSERT INTO StudentINFO (name, sex, birthday) values(?, ?, ?)'
        data = [
            ('Alice', '男', 20200101),
            ('Bob', '男', 19991212),
            ('Joey', '女', 19940102),
            ('Tom', '女', 19800408),
            ('Marry', '女', 20202020)
        ]
        with self.con:
            self.con.executemany(sql, data)

    # 表单 查询
    def select_table(self):
        with self.con:
            data = self.con.execute("SELECT * FROM USER ")
            for row in data:
                print(row)


if __name__ == '__main__':
    db = DB()
    a = sl.connect('my-test.db')
    db.new_table()
    db.add_data()
