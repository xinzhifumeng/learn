#最大公约数算法
def hcf(x,y):
    #定义一个函数，返回两个数最大公约数
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if ((x%i==0))and (y%i==0):
            hcf=i
    return hcf

num1= int(input("first number:"))
num2= int(input("second number:"))
print(num1,"and",num2,"最大公约数",hcf(num1,num2))