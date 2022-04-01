###############################################
'''
学习内容
冯康是谁
什么是哈密顿系统
什么是辛算法 (Symplectic Algorithm)
常微分方程的传统解法
'''
################################################
#%matplotlib inline

from IPython.display import Image
import matplotlib.pyplot as plt
import numpy as np

# odeint 用于求解常微分方程
from scipy.integrate import odeint

plt.style.use(['science', 'notebook', 'no-latex'])