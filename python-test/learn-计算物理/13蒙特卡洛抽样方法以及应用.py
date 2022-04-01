##########################################
'''
学习目标与内容
    回顾蒙特卡洛抽样的直接法与舍选法
    学习蒙特卡洛抽样的变换法
    马尔可夫链与随机行走
    马尔可夫链蒙特卡洛方法 MCMC
    MCMC: Metropolis-Hastings 抽样
    ** Gibbs 抽样
    ** Hybrid Monte Carlo 抽样
'''
#########################################

#In[]The python modules used in this notebook
import matplotlib.pyplot as plt
from IPython.display import IFrame
from IPython.display import Image
from scipy.integrate import simps
from scipy.stats import norm
import numpy as np

from tqdm import tqdm 

# 从 [0, 1] 区间的均匀分布抽样
from numpy.random import rand
# 从标准正态分布抽样
from numpy.random import randn

from ipywidgets import interact, widgets

plt.style.use(['science', 'notebook', 'no-latex'])