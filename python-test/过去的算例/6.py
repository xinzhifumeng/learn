#if 的骚操作
while True:
    try:
        num=float(input("输入一个数字："))
        if num>=0:
            if num==0:
                print(0)
            else:
                print("正数")
        else:
            print("负数")
        break
    except ValueError:
        print("erro,do it again")