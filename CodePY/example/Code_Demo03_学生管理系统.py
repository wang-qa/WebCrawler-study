from datetime import datetime
import sqlite3 as sl  # 使用轻量级 SQLite


# 初始化数据库 添加初始数据
class Demo_data:
    student_date = [
        {
            'name': '小红',
            'sex': '女',
            'birthday': '20010101'
        },
        {
            'name': '张三',
            'sex': '男',
            'birthday': '20140102'
        },
        {
            'name': 'Marry',
            'sex': '女',
            'birthday': '20110103'
        },
        {
            'name': 'marry',
            'sex': '男',
            'birthday': '202160104'
        },
        {
            'name': 'tom',
            'sex': '男',
            'birthday': '20000105'
        },

    ]

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


# 模拟数据
student_date = [
    {
        'name': '小红',
        'sex': '女',
        'birthday': '20010101'
    },
    {
        'name': '张三',
        'sex': '男',
        'birthday': '20140102'
    },
    {
        'name': 'Marry',
        'sex': '女',
        'birthday': '20110103'
    },
    {
        'name': 'marry',
        'sex': '男',
        'birthday': '202160104'
    },
    {
        'name': 'tom',
        'sex': '男',
        'birthday': '20000105'
    },

]


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

    # 美化输出
    def beauty_print(self, data_list):
        for index, student in enumerate(data_list):  # 自定义打印格式   index索引 enumerate()枚举
            print(f'序号：{index}', end='\t')
            print(f'姓名：{student.name}', end='\t')
            print(f'性别：{student.sex:2}', end='\t')  # 指定长度
            print(f'生日：{student.birthday}', end='\t')
            print(f'年龄：{student.get_age()}')


# 系统类
class StudentSystem:
    """ 系统实现与加载数据 """

    # 系统初始化
    def __init__(self, name):
        self.con = sl.connect('my-test.db')
        self.name = name  # 系统名称
        self.data = []

    # 实现 加载数据
    def load_date(self):
        for studentinfo in student_date:  # 遍历数据
            student = Student(studentinfo['name'], studentinfo['sex'], studentinfo['birthday'])  # 实例化对象
            self.data.append(student)  # 列表追加

    model = Model()  # 实例化 模版

    # 查找 根据姓名
    def find_student_by_name(self):
        name = self.model.input_name()
        find_list = []  # 可能有多个结果
        for student in self.data:  # 遍历 date 查找
            if name.lower() in student.name.lower():  # 如果 学生姓名与输入的一致
                find_list.append(student)

        if find_list:  # 结果为真
            return find_list  # 返回 find_list
        else:  # 结果为假
            print(f' 查询失败 ---< {name} >--- 不存在')

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
        self.load_date()  # 系统启动 加载数据
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
        print(" ==> 查询 all ")
        # for student in self.data: # 在`beauty_print`中已遍历 此处不需要
        self.model.beauty_print(self.data)
        with self.con:
            print("--------------------sql_find_all--------------------")
            sql_find_all = f"SELECT name,sex,birthday FROM StudentINFO "
            print(sql_find_all)
            data_findall_end = self.con.execute(sql_find_all).fetchall()  # sql run end
            # 格式化打印
            for index, list_sql in enumerate(data_findall_end):
                print(f"序号: {index + 1}  姓名: {list_sql[0]:6} 性别: {list_sql[1]} 生日: {list_sql[2]}")

    # 2. 查询学生信息
    def find_student(self):
        print(" ==> 查询 ")
        # for student in self.data:  # 遍历 date
        #     if student.name == name:  # 如果 学生姓名与输入的一致
        #         self.beauty_print([student])

        # else:  # 遍历 date 未找到
        #     print('查无此人 查询失败')

        # # 优化封装为`find_list`
        # find_list = self.find_student_by_name()
        # if find_list:
        #     self.model.beauty_print(find_list)
        name = self.model.input_name()
        with self.con:
            print("--------------------sql_find_allonly--------------------")
            sql_find_only = f"SELECT * FROM StudentINFO where name LIKE '%{name}%'"
            print(sql_find_only)
            data_findonly_end = self.con.execute(sql_find_only).fetchall()  # sql run end
            # 格式化打印
            for index, list_sql in enumerate(data_findonly_end):
                print(f"序号: {index + 1}  姓名: {list_sql[1]:6} 性别: {list_sql[2]} 生日: {list_sql[3]}")

    # 3. 添加学生信息
    def create_student(self):
        print(" ==> 新增 ")
        name = self.model.input_name()
        sex = self.model.choose_sex()
        birthday = input("生日 > ")
        # student = Student(name, sex, birthday)
        # self.data.append(student)  # 追加 ==> 学生数据
        print(sex)
        with self.con:
            print("--------------------sql_insert--------------------")
            # 插入信息
            sql_insert = f"INSERT INTO StudentINFO (name,sex,birthday)  VALUES ('{name}','{sex}','{birthday}')"
            print(sql_insert)  # sql run end
            # 查找插入内容 回显
            sql_find_only = f"select * from StudentINFO order by id desc limit 1"
            data_end_insert = self.con.execute(sql_find_only).fetchall()
            print(data_end_insert)  # sql run end
            # 格式化打印
            for index, list_sql in enumerate(data_end_insert):
                print(f"新增信息 ==>序号: {index + 1}  姓名: {list_sql[1]:6} 性别: {list_sql[2]} 生日: {list_sql[3]}")

        print("新增学生信息 ==> success")

    # 4. 修改学生信息
    def modify_student(self):
        print(" ==> 修改")
        # find_list = self.find_student_by_name()
        # if find_list:
        #     self.model.beauty_print(find_list)
        #     index = int(input("修改序号 > "))
        #     student = find_list[index]
        #     print("\n 当前修改的是 >>>")
        #     self.model.beauty_print([student])
        #     name = input("new name : ").strip()
        #     sex = self.model.choose_sex()
        #     birthday = input("new birhtday : ")
        #     if name:
        #         student.name = name
        #     student.sex = sex
        #     student.birthday = birthday
        with self.con:
            print("--------------------sql_update--------------------")
            find_name = input("查找对应姓名")
            # 先模糊找数据
            sql_find_only = f"SELECT * FROM StudentINFO where name like '%{find_name}%'"
            data_find_only = self.con.execute(sql_find_only).fetchall()
            print(data_find_only)  # sql run end
            # 格式化打印
            for index, list_sql in enumerate(data_find_only):
                print(f"信息 ==>序号: {index + 1}  姓名: {list_sql[1]:6} 性别: {list_sql[2]} 生日: {list_sql[3]}")
                print("--------------------")
            # 输入准确信息
            name = input("new name : ").strip()
            if name:
                new_name = name
            sex = self.model.choose_sex()
            birthday = input("new birhtday : ")
            sql_update = f"UPDATE StudentINFO SET name='{name}',sex= '{sex}',birthday='{birthday}' where name='{list_sql[1]}'"
            data_update_only = self.con.execute(sql_update).fetchall()
            print(data_update_only)  # sql run end
            print("--------------------")
            # 查找修改后的数据
            sql_find_only2 = f"SELECT * FROM StudentINFO where name='{new_name}'"
            data_find_only2 = self.con.execute(sql_find_only2).fetchall()
            print(data_find_only2)
            # 格式化打印
            for index, list_sql in enumerate(data_find_only2):
                print(f"信息 ==>序号: {index + 1}  姓名: {list_sql[1]:6} 性别: {list_sql[2]} 生日: {list_sql[3]}")
            ''' 脑袋疼 绕迷糊了 现在是 姓名一样的 都改了'''

    # 5. 删除学生信息
    def remove_student(self):
        print(" ==> 刪除")
        # find_list = self.find_student_by_name()
        # if find_list:
        #     self.model.beauty_print(find_list)
        #     index = int(input("remove ID > "))
        #     print("\n remove 的是 >>>")
        #     student = find_list[index]
        #     self.model.beauty_print([student])
        #     self.data.remove(student)
        #     print("remove success")
        with self.con:
            print("--------------------sql_delete--------------------")
            find_name = input("查找对应姓名")
            # 先模糊找数据
            sql_find_only = f"SELECT * FROM StudentINFO where name like '%{find_name}%'"
            data_find_only = self.con.execute(sql_find_only).fetchall()
            print(data_find_only)  # sql run end
            # 格式化打印
            for index, list_sql in enumerate(data_find_only):
                print(f"信息 ==>序号: {index + 1}  姓名: {list_sql[1]:6} 性别: {list_sql[2]} 生日: {list_sql[3]}")
                print("--------------------")
            # 输入准确信息
            name = input("new name : ").strip()
            sql_delete = f"DELETE FROM StudentINFO where name = '{name}'"
            data_delete_only = self.con.execute(sql_delete).fetchall()
            print(data_delete_only)  # sql run end
            print("delete success")
            ''' 脑袋疼 绕迷糊了 现在是 姓名一样的 都删了'''


if __name__ == '__main__':
    student_sys = StudentSystem('Demo 学生系统')  # 系统名称
    student_sys.start()
