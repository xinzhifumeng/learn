#计算圆的面积

r=float(input('半径r:'))

'''
s=3.1415926*(r**2)
print('%0.2f' %s)
'''
def Area(r):
    PI=3.1415926
    return PI*(r*r)
#print(Area(r))
print('半径为{0}圆的面积：{1}'. format(r,Area(r)))