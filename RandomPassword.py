import random
import time

# 检测是否生成密码
if input("是否生成密码(Y/N): ") == "Y":
    # 询问密码类型
    type = input("请输入密码类型(A.数字 B.数字+字母 C.数字+字母+特殊字符): ")
    # 询问密码长度
    length = int(input("请输入密码长度(8-64): "))

    # 生成密码
    # 判断密码长度
    if length < 8 or length > 64:
        print("密码长度不符合要求，请重新输入")
        time.sleep(1)
        exit()

    # 判断密码类型
    if type == "A":
        # 生成数字密码
        password = "".join([str(random.randint(0, 9)) for i in range(length)])
    elif type == "B":
        # 生成数字+字母密码
        password = "".join([str(random.randint(0, 9)) + chr(random.randint(97, 122)) for i in range(length)])
    elif type == "C":
        # 生成数字+字母+特殊字符密码
        password = "".join([str(random.randint(0, 9)) + chr(random.randint(97, 122)) + chr(random.randint(33, 47)) for i in range(length)])

    # 输出密码
    print("密码: " + password)

    # 检测是否保存密码
    if input("是否保存密码(Y/N): ") == "Y":
        # 保存密码
        with open("password.txt", "w") as f:
            f.write(password)
            f.close()
            print("密码已保存到password.txt文件中")
            time.sleep(1)
            exit()
    elif input("是否保存密码(Y/N): ") == "N":
        # 不保存密码
        print("密码已生成，但未保存")
        time.sleep(1)
    else:
        print("输入错误，请重新输入")
        time.sleep(1)
        exit()

else:
    print("程序结束")
    time.sleep(3000)
    exit()