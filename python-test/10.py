#获取最大值函数
#print(max(1,2))
#质数判断
'''
while True:
    try:
        num=int(input('input number:'))
        if num<=1:continue
    except ValueError :continue
    for i in range(2,num):
        if (num%i)==0:
            print(num,"不是质数因子({0},{1})".format(i,int(num/i)))
            break
    else:print(num,"是质数")
    break
'''
#输出指定范围内的质数
while True:
    try:
        lower=int(input("lower:"))
        upper=int(input("upper:"))
    except ValueError:continue
    for num in range(lower,upper):
        if num>1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:print(num,'is prime number')
    break
                    