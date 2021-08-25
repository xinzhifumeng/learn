

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 20:24:28 2020

@author: Kangshifu reader:suzhixin
"""
#######导入我们需要的库
from math import sin, cos ##基本数学运算
import numpy as np        ##基本矩阵操作
from scipy.integrate import odeint  ##主要在numpy库上增加一些库函数
import matplotlib.animation as animation ##与numpy scipy 三个代替matleb用
import matplotlib.pyplot as pl

#######这里是重力加速度
g = 9.85

#######面向对象编程，把这个双摆模型定义成一个类，包括四个参数，两个微分方程，但是由于微分方程是
#######二阶的无法直接求解，把原来二阶的微分方程转化为一阶的状态方程来求解
class DoublePendulum(object):
    def __init__(self, m1, m2, l1, l2):
        self.m1, self.m2, self.l1, self.l2 = m1, m2, l1, l2
        self.init_status = np.array([0.0, 0.0, 0.0, 0.0])

    def equations(self, w, t):
        """
        微分方程公式
        """
        m1, m2, l1, l2 = self.m1, self.m2, self.l1, self.l2
        th1, th2, v1, v2 = w
        dth1 = v1
        dth2 = v2

        #eq of th1
        a = l1 * (m1 + m2)  # dv1 parameter
        b = m2 * l2 * cos(th1 - th2)  # dv2 paramter
        c = (m2 * l2 * sin(th1 - th2) * dth2 * dth2 + (m1 + m2) * g * sin(th1))

        #eq of th2
        d = l1 * cos(th1 - th2)  # dv1 parameter
        e = l2  # dv2 parameter
        f = (-l1 * sin(th1 - th2) * dth1 * dth1 + g * sin(th2))
        #######这里注意一下，因为我们的方程里面含有两个二次导数项，这里是为了把
        #######每个方程变为只含有一个二次倒数项的形式
        dv1, dv2 = np.linalg.solve([[a, b], [d, e]], [-c, -f]) 
        ##求解线性方程组Ax=b,其中A为矩阵b为一维或二维数组x未知
        ##\theta 的二阶项作为未知数，abde作为含未知数的系数矩阵，其余项是行列式的值
        '''
        a*dv1+b*dv2=-c
        d*dv1+e*dv2=-f
        '''

        return np.array([dth1, dth2, dv1, dv2])
        #odeint需要的导数形式，此处将一阶二阶导数传递出去，其中二阶由一阶和\theta构成，故可以计算
        #在提供初始值时，由于带入了一阶的导数，故需要同时输入一阶和0阶的初始状态 


######这里是调用odeint函数求解双摆的动力学方程
def double_pendulum_odeint(pendulum, ts, te, tstep):
    """
    对双摆系统的微分方程组进行数值求解，返回两个小球的X-Y坐标
    """
    t = np.arange(ts, te, tstep) #利用数组返回的值代表时间演化
    track = odeint(pendulum.equations, pendulum.init_status, t)
    th1_array, th2_array = track[:, 0], track[:, 1]#解出来两个\theta角
    l1, l2 = pendulum.l1, pendulum.l2
    x1 = l1 * np.sin(th1_array)
    y1 = -l1 * np.cos(th1_array)
    x2 = x1 + l2 * np.sin(th2_array)
    y2 = y1 - l2 * np.cos(th2_array)
    pendulum.init_status = track[-1, :].copy()  #将最后的状态赋给pendulum
    return [x1, y1, x2, y2]


if __name__ == "__main__":
    pendulum = DoublePendulum(1.0, 2.0, 1.0, 2.0)
    ########初始角度m m theta1=1 theta2=2 这里的单位为弧度
    th1, th2 = 1.0, 2.0
    #####定义初始条件，这里认为初始两个球的速度为零，时间60秒，步长0.02
    dt = 0.02
    pendulum.init_status[:2] = th1, th2  ###
    x1, y1, x2, y2 = double_pendulum_odeint(pendulum, 0, 60, dt)
    fig = pl.figure(figsize=(5, 5), dpi=80)

##########下面将我们的求解结果进行可视化
fig = pl.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-4, 4), ylim=(-4, 4))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


##########下面是函数animation.FuncAnimation使用模板
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i * dt))
    return line, time_text


ani = animation.FuncAnimation(fig, animate,range(1, len(y1)),interval= dt * 1000,blit=True,init_func=init)
ani.save('shuangbai1.gif', writer='pillow')
pl.show()
