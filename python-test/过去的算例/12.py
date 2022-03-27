import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint  ##主要在numpy库上增加一些库函数

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def diff(y, x):
    return np.array(x)
    # 上面定义的函数在odeint里面体现的就是dy/dx = x
    #描写函数、初值和需要求解函数值对应的的时间点。接收数组形式。这个函数，要求微分方程必须化为标准形式，即dy/dt=f(y,t,)。from scipy import odein
x = np.linspace(0, 10, 100)  # 给出x范围
y = odeint(diff, 0, x)  # 设初值为0 此时y为一个数组，元素为不同x对应的y值
# 也可以直接y = odeint(lambda y, x: x, 0, x)
plt.plot(x, y[:, 0])  # y数组（矩阵）的第一列，（因为维度相同，plt.plot(x, y)效果相同）
plt.grid()
plt.show() 



g = 9.8
l = 1
def diff2(d_list, t):
    omega, theta = d_list
    return np.array([-g/l*theta, omega])
t = np.linspace(0, 20, 2000)
result = odeint(diff2, [0, 35/180*np.pi], t)
# 结果是一个两列的矩阵， odeint中第二个是初始单摆角度35度
plt.plot(t, result[:, 0])  # 输出omega随时变化曲线
plt.plot(t, result[:, 1])  # 输出theta随时变化曲线，即方程解
plt.show()
