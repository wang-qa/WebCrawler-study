# python demo games

"""
在 1-50 中产生一个随机数
根据用户输入提示“猜大了”“猜小了”
猜对结束游戏
"""
input_Num = int(input("猜数字游戏 输入序号\n无限制[1]  有限制[2] \n  >>> "))
if input_Num == 1:
    print(" Demo_Game01     猜数字[1-50]   无限制")
    import random  # 随机数模块

    tmpNum01 = random.randint(1, 50)  # 随机范围 1-50
    Demo_Game01_count = 0
    while True:
        Demo_Game01 = int(input("输入 1-50 内的整数 >>> "))
        if Demo_Game01 > tmpNum01:
            print("猜大了")
        elif Demo_Game01 < tmpNum01:
            print("猜小了")
        else:
            print("猜对了\n\n" + "一共用了 >>> " + str(Demo_Game01_count) + " <<< 次猜对\n")
            break  # 猜对后结束游戏
        Demo_Game01_count = Demo_Game01_count + 1  # 当前次数 +1
    print(5 * "-" + " Demo_Game01  >>> end  \n")
elif input_Num == 2:
    print(" Demo_Game01     猜数字[1-50]   限制次数")
    import random  # 随机数模块

    tmpNum02 = random.randint(1, 50)  # 随机范围 1-50
    Demo_Game02_total = 5  # 可以猜的次数
    Demo_Game02_count = 0  # 当前次数
    while True:
        Demo_Game02 = int(input("输入 1-50 内的整数 >>> "))

        if Demo_Game02 > tmpNum02:
            print("猜大了")
        elif Demo_Game02 < tmpNum02:
            print("猜小了")
        else:
            print("猜对了\n\n" + "一共用了 >>> " + str(Demo_Game02_count) + " <<< 次猜对\n")
            break  # 猜对后结束游戏

        Demo_Game02_count = Demo_Game02_count + 1  # 当前次数 +1
        if Demo_Game02_count >= Demo_Game02_total:
            print(f'\n允许猜 {Demo_Game02_total} 次 \n已猜了 {Demo_Game02_count} 次\n 游戏结束')
            break  # 达到条件后结束游戏
    print(5 * "-" + " Demo_Game02  >>> end  \n")
else:
    print("输入错误 已结束 请重试")
