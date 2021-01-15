from datetime import datetime
import sqlite3 as sl  # 使用轻量级 SQLite


# 初始化数据库 添加初始数据
class Demo_data:

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
                        birthday TEXT
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


# 学生类
class Student:
    '''学生信息'''

    # 学生初始化
    def __init__(self, name, sex, birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday

    # 计算年龄
    def get_age(self):
        if self.birthday:
            this_year = datetime.now().year  # 获取当前年份
            age = this_year - int(self.birthday[:4])  # 取前4位并转为int
            return age
        else:
            return "保密"


# 数据库语句
class DB_sql:
    def find_all(self):  # 查找-全部
        sql_find_all = f"SELECT * FROM StudentINFO "
        print("sql: find_all success  ==> ", sql_find_all)
        return sql_find_all

    def find_only(self, name):  # 查找-匹配
        sql_find_only = f"SELECT * FROM StudentINFO where name LIKE '%{name}%'"
        print("sql: find_only success  ==> ", sql_find_only)
        return sql_find_only

    def add_only(self, name, sex, birthday):  # 添加
        sql_insert = f"-- INSERT INTO StudentINFO (name,sex,birthday)  VALUES ('{name}','{sex}','{birthday}')"
        print("sql: update success  ==> ", sql_insert)
        return sql_insert

    def update_only(self, name, sex, birthday, find_name):  # 更新
        sql_update = f"UPDATE StudentINFO SET name='{name}',sex= '{sex}',birthday='{birthday}' where name='{find_name}'"
        print("sql: update success  ==> ", sql_update)
        return sql_update

    def delete_only(self, find_name):  # 删除
        sql_delete = f"DELETE FROM StudentINFO where name = '{find_name}'"
        print("sql: delete success  ==> ", sql_delete)
        return sql_delete

    def find_max_id(self):  # 查找最新id
        sql_find_maxid = f"SELECT * FROM StudentINFO order by id desc limit 1"
        print("sql: find maxID success  ==> ", sql_find_maxid)
        return sql_find_maxid


class Model:  # info:校验 格式
    # 校验 姓名
    def input_name(self):
        while True:
            name = input("姓名 > ").strip()  # 去除输入的空格
            if name:  # 如果有
                return name
            else:
                continue  # 循环输入

    # 校验 性别
    def choose_sex(self):
        while True:
            sex = input("选择性别 > [1]男 | [2]女 > ").strip()  # 去除输入的空格
            if sex:  # 不为空
                return "未识别"
            elif sex == "1":
                return "男"
            elif sex == "2":
                return "女"
            else:  # 未输入
                return "not write"


# 系统类
class StudentSystem:
    """ 系统实现与加载数据 """

    # 系统初始化
    def __init__(self, name):
        self.name = name  # 系统名称

        # 数据库 connect 返回字典
        def dict_factory(cursor, row):
            d = {}
            for index, col in enumerate(cursor.description):
                d[col[0]] = row[index]
            return d

        self.con = sl.connect('my-test.db')  # 轻量级 如果不存在则自动创建并连接
        self.con.row_factory = dict_factory

    model = Model()  # 实例化 模版
    sql = DB_sql()

    # 显示菜单
    def show_menu(self):  # 定义菜单

        print(f"""
            ******************************
            欢迎使用【 {self.name} 】 V0.0.3
                1. 所有学生信息
                2. 查询学生信息
                3. 添加学生信息
                4. 修改学生信息
                5. 删除学生信息
                0. 退出系统
            ******************************
        """)

    # 启动系统
    def start(self):
        while True:  # 一直运行
            self.show_menu()  # 调用菜单功能函数
            operation = input("选择操作：")
            if operation == "1":  # 查询所有
                self.show_all_student()
            elif operation == "2":  # 查找学生
                self.find_student()
            elif operation == "3":  # 新建学生
                self.create_student()
            elif operation == "4":  # 修改学生
                self.modify_student()
            elif operation == "5":  # 删除学生
                self.remove_student()
            elif operation == "0":  # 退出
                print(f" close {self.name}      --- bye bye ---")
                break
            else:  # 其他
                print("输入有误 重新输入")
                continue

    '''菜单功能实现'''

    # 1.所有学生信息
    def show_all_student(self):
        print(" ==> 查询 all ", self.sql.find_all())
        with self.con:
            print("--------------------sql_find_all--------------------")
            data_findall_end = self.con.execute(self.sql.find_all()).fetchall()  # sql run end
            # 格式化打印
            for index, list_sql in enumerate(data_findall_end):
                print(f"序号: {index + 1} 姓名: {list_sql['name']:7} 性别: {list_sql['sex']:4} 生日: {list_sql['birthday']}")

    # 2. 查询学生信息
    def find_student(self):
        print(" ==> 查询 ")
        name = self.model.input_name()
        with self.con:
            print("--------------------sql_find_allonly--------------------")
            data_findonly_end = self.con.execute(self.sql.find_only(name)).fetchall()  # sql run end
            # 格式化打印
            for index, list_sql in enumerate(data_findonly_end):
                print(f"序号: {index + 1}  姓名: {list_sql['name']:6} 性别: {list_sql['sex']} 生日: {list_sql['birthday']}")

    # 3. 添加学生信息
    def create_student(self):
        print(" ==> 新增 ")
        name = self.model.input_name()
        sex = self.model.choose_sex()
        birthday = input("生日 > ")
        print(sex)
        with self.con:
            print("--------------------sql_insert--------------------")
            # 插入信息 回显
            self.con.execute(self.sql.add_only(name, sex, birthday)).fetchall()
            data_find_maxid = self.con.execute(self.sql.find_max_id()).fetchall()
            # 格式化打印
            for index, list_sql in enumerate(data_find_maxid):
                print(
                    f"最新信息 ==>序号: {index + 1}  姓名: {list_sql['name']:6} 性别: {list_sql['sex']} 生日: {list_sql['birthday']}")
        # print("新增学生信息 ==> success")

    # 4. 修改学生信息
    def modify_student(self):
        print(" ==> 修改")
        with self.con:
            print("--------------------sql_update--------------------")
            find_name = input("查找对应姓名")
            # 先模糊找数据
            data_find_only = self.con.execute(self.sql.find_only(find_name)).fetchall()
            # 格式化打印
            for index, list_sql in enumerate(data_find_only):
                print(
                    f"找到信息 ==> 序号: {index + 1}  姓名: {list_sql['name']:6} 性别: {list_sql['sex']} 生日: {list_sql['birthday']}")
            # 输入准确信息
            name = input("new name : ").strip()
            if name:
                new_name = name
            sex = self.model.choose_sex()
            birthday = input("new birhtday : ")
            data_update_only = self.con.execute(self.sql.update_only(name, sex, birthday, find_name)).fetchall()
            print(data_update_only)  # sql run end
            print("--------------------")
            # 查找修改后的数据
            sql_find_only2 = f"SELECT * FROM StudentINFO where name='{new_name}'"
            data_find_only2 = self.con.execute(sql_find_only2).fetchall()
            print(data_find_only2)
            # 格式化打印
            for index, list_sql in enumerate(data_find_only2):
                print(
                    f"信息 ==>序号: {index + 1}  姓名: {list_sql['name']:6} 性别: {list_sql['sex']} 生日: {list_sql['birthday']}")
            ''' 脑袋疼 绕迷糊了 现在是 姓名一样的 都改了'''

    # 5. 删除学生信息
    def remove_student(self):
        print(" ==> 刪除")
        with self.con:
            print("--------------------sql_delete--------------------")
            find_name = input("查找对应姓名")
            # 先模糊找数据
            sql_find_only = f"SELECT * FROM StudentINFO where name like '%{find_name}%'"
            data_find_only = self.con.execute(sql_find_only).fetchall()
            print(data_find_only)  # sql run end
            # 格式化打印
            for index, list_sql in enumerate(data_find_only):
                print(
                    f"信息 ==>序号: {index + 1}  姓名: {list_sql['name']:6} 性别: {list_sql['sex']} 生日: {list_sql['birthday']}")
                print("--------------------")
            # 输入准确信息
            name = input("delete name : ").strip()
            data_delete_only = self.con.execute(self.sql.delete_only(name)).fetchall()
            print(data_delete_only)  # sql run end
            print("delete success")
            ''' 脑袋疼 绕迷糊了 现在是 姓名一样的 都删了'''


if __name__ == '__main__':
    student_sys = StudentSystem('Demo 学生系统')  # 系统名称
    student_sys.start()
