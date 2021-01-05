# python 语法

print("python3 python >>> 循环语法")

print("\n" * 2 + "begin >>>  \n")
'''if-elif-...-else  判断正负数'''
print("-" * 10 + " if-elif-...-else  判断正负数 " + "-" * 10)
number = int(input("输入整数："))
if number > 0:
    print("正数")
elif number == 0:
    print("当前为 0")
else:
    print("负数")

print("\n" * 2 + "end\n")

'''for 遍历'''
print("-" * 10 + " for 遍历 " + "-" * 10)

for j in range(5):
    print(j)
print(" " * 5 + " 从 0 到 5, range(5)")
for i in range(4, 10):
    print(i)
print(" " * 5 + " 从 4 到 10, range(4, 10)")
for i in range(3, 20, 2):
    print(i)
print(" " * 5 + "从 3 到 20 ， 2递增值, range(3, 20, 2)")

print("\n" * 2 + "end\n")

'''while 循环'''
print("-" * 10 + " while 循环 " + "-" * 10)
n = 1
while n < 5:
    print("当前 N 的值为" + str(n))
    n = n + 1
else:
    print("while 循环结束： N => 5")

print("\n" * 2 + "end\n")

# 循环嵌套  demo：输出乘法口诀
# for 后跟的是 序列
# while 后跟的是条件
''' for 循环嵌套 '''
print("-" * 10 + " for 循环嵌套 " + "-" * 10)
for A in range(1, 10):  # 乘数A 从1到9结束
    for B in range(1, A + 1):  # 乘数B 从1到 A+1 ---不包括结束值所以 +1
        print(f'{A}*{B}={A * B}', end=" ")  # 内部循环 以空格结束
    print()  # 外部循环 默认换行

''' while 循环嵌套 '''
print("-" * 10 + " while 循环嵌套 " + "-" * 10)
AA = 1
while AA <= 9:
    BB = 1
    while BB <= AA:
        print(f'{AA}*{BB}={AA * BB}', end=" ")
        BB += 1
    AA += 1
    print()

print("\n" * 2 + "--- end \n")

''' while + for 循环嵌套 '''
print("-" * 10 + " while + for  循环嵌套 " + "-" * 10)
AAA = 1
while AAA <= 9:
    for BBB in range(1, AAA):
        print(f'{AAA}*{BBB}={AAA * BBB}', end=" ")
    AAA += 1
    print()

print("\n" * 2 + "--- end \n")

print("python3 python >>> 循环控制")
print("\n" * 2 + "begin >>>  \n")
# 循环控制 break
# # break 结束循环
'''break 结束循环'''
print("-" * 10 + " break 结束循环 " + "-" * 10)
while True:  # 如果为真
    demo_break = input('输入[__] 退出[0] >>>  ')
    if demo_break == '0':  # 如果输入为 0 结束循环
        break
    print("你输入的是 >>>  " + demo_break)
print("\n" * 2 + "--- end \n")

# 循环控制 continue
# # continue 跳过后面代码 立刻进入下次循环
'''continue 直接开始下次循环'''
print("-" * 10 + " continue 直接开始下次循环 " + "-" * 10)
for demo_continue in [0, 1, 2, 3, 4]:
    if demo_continue == 2:
        continue  # 结束 这次循环 进入 循环
    print(demo_continue)  # 不输出2跳过
print("\n" * 2 + "--- end \n")
