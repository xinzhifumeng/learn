# Filename :2
# auther：xinzhi
 
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

# 导入 cmath(复杂数学运算) 模块



'''
import cmath
a=float(input('a:'))
b=float(input('b:'))
c=float(input('c:'))

d=b*b-4*a*c

sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print(sol1,sol2 )
print('{0}  {1}'.format(sol1,sol2))
'''
#part2
#计算三角形面积 边长a、b、c

a=float(input('边长a:'))
b=float(input('边长b:'))
c=float(input('边长c:'))

s=(a+b+c)/2  #计算半周长

area=(s*(s-a)*(s-b)*(s-c))**0.5
print('面积为%0.2f' %area)
