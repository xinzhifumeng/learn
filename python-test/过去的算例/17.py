#递归函数，斐波那契数列
def recur_fibo(n):
    if n<=1:
        return 1
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

neterms=int(input("输出项数:"))
if neterms <=0:
    print("输入整数：")
else:
    print("斐波那契数列：")
    for i in range (neterms):
        print(recur_fibo(i))