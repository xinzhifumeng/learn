# 最小公倍数算法
 
#定义函数
def lcm(x,y):
    if x>y:
        greater=x
        smaller=x
    else:
        greater = y
        smaller= y
    while(True):
        if ((greater % x==0) and (greater %y==0)):
            lcm = greater 
            break
        greater+=smaller
    return lcm

num1=int(input("first numberL "))
num2=int(input("second numberL "))

print(num1,"and",num2,"最小公倍数",lcm(num1,num2))