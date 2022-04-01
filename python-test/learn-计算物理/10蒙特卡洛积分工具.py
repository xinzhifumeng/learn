#######################################################
'''
学习目标
    掌握高维蒙特卡洛积分工具 vegas
    理解蒙特卡洛积分原理
学习内容
    vegas 库的安装、调用、输出结果分析
    蒙特卡洛积分的原理
    vegas 蒙卡积分的缺陷及替代方案'''

########################################################

## vegas 库用作高维蒙特卡洛积分
import vegas

import math
import numpy as np
from ipywidgets import interact
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.integrate import quad
from IPython.display import Image

plt.style.use(['science', 'notebook', 'no-latex'])