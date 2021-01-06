"""
使用简单函数实现学生管理系统

***************************
欢迎使用【学生管理系统】 V0.0.1
    1. 显示所有学生信息
    2. 查询学生信息
    3. 添加学生信息
    4. 修改学生信息
    5. 删除学生信息
    0. 退出系统
***************************
"""

# 所有学生数据 用列表模拟一个数据库表 user_date
student_date = [
    {
        'id': 20210106001,
        'name': '小红',
        'sex': '女',
        'age': 13,

        'city': '香港'
    },
    {
        'id': 20210106002,
        'name': '张三',
        'sex': '男',
        'age': 42,
        'city': '北京'
    },
    {
        'id': 20210106003,
        'name': 'marry',
        'sex': '女',
        'age': 11,
        'city': '沈阳'
    },
    {
        'id': 20210106004,
        'name': 'jery',
        'sex': '男',
        'age': 21,
        'city': '广州'
    },
    {
        'id': 20210106005,
        'name': 'tom',
        'sex': '男',
        'age': 44,
        'city': '上海'
    },

]

''' 封装函数 '''


def step():
    1


# 1. 显示所有学生信息
def show_all():
    for student in student_date:
        print(student)


# 2. 查询学生信息
def find_student():
    name = input("输入查询的学生姓名 > ")
    for student in student_date:  # 遍历 date
        if student['name'] == name:  # 如果 学生姓名与输入的一致
            print(student)
            return  # 返回 student
    else:  # 遍历 date 未找到
        print('查无此人 查询失败')


# 3. 添加学生信息
def create_student():
    print("新增学生信息 ==>")
    name = input("姓名 > ")
    sex = input("性别 > ")
    age = input("年龄 > ")
    city = input("所在地 > ")
    student = {
        'name': name,
        'sex': sex,
        'age': age,
        'city': city
    }
    student_date.append(student)  # 追加 ==> 学生数据
    print("新增学生信息 ==> success")


# 4. 修改学生信息
def modify_student():
    name = input("输入查询的学生姓名 > ")
    for student in student_date:  # 遍历 date
        if student['name'] == name:  # 如果 学生姓名与输入的一致
            print(student)
            student['name'] = input("姓名 > ")
            student['sex'] = input("性别 > ")
            student['age'] = input("年龄 > ")
            student['city'] = input("所在地 > ")
            print("修改结果 ==> success")
    else:  # 遍历 date 未找到
        print('查无此人')


# 5. 删除学生信息
def remove_student():
    name = input("输入查询的学生姓名 > ")
    for student in student_date:  # 遍历 date
        if student['name'] == name:  # 如果 学生姓名与输入的一致
            print(student)
            student_date.remove(student)  # 删除 学生
            return  # 返回 student
    else:  # 遍历 date 未找到
        print('查无此人 删除失败')


# 0. 退出系统

''' 执行过程 '''
while True:
    print("""
        ****************************
        欢迎使用【学生管理系统】 V0.0.1
            1. 显示所有学生信息
            2. 查询学生信息
            3. 添加学生信息
            4. 修改学生信息
            5. 删除学生信息
            0. 退出系统
        ****************************
    """)
    operation = input("请输入操作序号 >>> ")  # 输入序号
    if operation == '1':
        print("显示所有学生信息 ==>")
        show_all()
    elif operation == '2':
        print("查询信息 ==>")
        find_student()
    elif operation == '3':
        print("添加学生信息 ==>")
        create_student()
    elif operation == '4':
        print("修改学生信息 ==>")
        modify_student()
    elif operation == '5':
        print("删除学生信息 ==>")
        remove_student()
    elif operation == '0':
        print("退出系统\n --- end ---\n")
        break  # 结束循环
    else:
        print("输入有误 重新输入 ")
