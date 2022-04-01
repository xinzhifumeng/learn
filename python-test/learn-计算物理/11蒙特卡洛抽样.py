################################################
'''
学习目标
    认识蒙特卡洛方法
    掌握蒙特卡洛抽样
学习内容
    统计学的基础知识与随机数使用举例
    抽取满足给定分布的随机数
        直接法
        舍选法 (Rejection Sampling)
    蒙卡抽样在高能核物理中的应用
        碰撞参数的抽样: 注意 平方概率
        核子在原子核内分布的抽样（Woods-Saxon 与  θ ,  ϕ ) 注意 cos(theta) 满足均匀分布，而非 theta
        分子动力学模拟中给定温度抽取粒子动量（速度）分布
        Boltzmann 分布，Fermi-dirac，Bose-Einstein 分布，Cooper-Frye 公式
    蒙特卡洛方法后续课程
        更多概率分布密度函数介绍
        更多蒙特卡洛抽样在高能物理中的应用举例
        变换法抽样与流模型
        马尔可夫链蒙特卡洛 Metropolis Hastings
        贝叶斯分析做全局拟合，提取模型参数
'''
################################################

#In[]
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.integrate import simps
import pandas as pd
import numpy as np
from scipy.stats import norm
# 从 [0, 1] 区间的均匀分布抽样
from numpy.random import rand

# 从标准正态分布抽样
from numpy.random import randn

from ipywidgets import interact

plt.style.use(['science', 'notebook', 'no-latex'])
# %%
