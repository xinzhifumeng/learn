'''
学习目标
    初步认识最小二乘法在拟合数据、物理参数提取中的作用

学习内容
    宇宙微波背景辐射
    使用 python 从文件中读数据、画图
    根据黑体辐射公式编写函数，计算给定频率、温度时的光谱
    匹配公式与观测数据的单位
    使用最小二乘法拟合数据，提取模型参数
    最小二乘法系统介绍
    
    
'''
#In[1] 导入数据
#读入数据文件，画出宇宙微波背景辐射的能谱与 $\nu$ 的关系曲线
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv("data/cosmic_microwave_background.csv")
df.head()

nu = df["nu[1/cm]"]
Inu = df["I[MJy/sr]"]
err = df["Error[kJy/sr]"] * 0.001
plt.errorbar(nu, Inu, yerr=err, fmt="ro-")


#In[6] 定义 Planck 黑体辐射公式

from scipy.constants import Planck
from scipy.constants import Boltzmann
from scipy.constants import speed_of_light as C 
Planck      # unit = J s
#6.62607015e-34
Boltzmann  # unit = J / K
#1.380649e-23
C          # unit = m/s
#299792458.0

def blackbody(nu, T=1.0):
    ''':nu: [1/ cm], frequency
     :T: [K] temperature 
     :return: I(nu, T) unit=[Mjy/Sr]'''
    nu = nu * C * 100   # to HZ (/s) 这里对应提取出来的nu，100是单位转换
    coef = 2 * Planck * nu**3 / C**2
    tmp = (Planck * nu) / (Boltzmann * T)
    # I_Jm2 : unit [J/m^2/sr]
    
    I_Jm2 = coef / (np.exp(tmp) - 1)
    to_Mjy_per_Sr = 10**20
    
    return I_Jm2 * to_Mjy_per_Sr
    #普朗克黑体辐射定律公式
    # I(\nu,T) = {2 * Planck * nu**3 / C**2} / {e**((Planck * nu) / (Boltzmann * T)-1)}
    # 单位时间单位立体角所对应辐射行进截面积及单位频率下辐射的能量   
        
nu_ = np.linspace(2, 22, 200)

plt.errorbar(nu, Inu, yerr=err, fmt="ko", label="exp-")
plt.plot(nu_, blackbody(nu_, T=2.0), label="T=2 K")
plt.plot(nu_, blackbody(nu_, T=2.73), label="T=2.73 K")
plt.plot(nu_, blackbody(nu_, T=3.0), label="T=3.0 K")

plt.legend(loc='best')
plt.xlabel(r"$\nu\ [cm]^{-1}$")
plt.ylabel(r"$I(\nu, T)$ [MJy/Sr]")


#In[12] 使用最小二乘法，拟合出宇宙微波背景辐射温度
#前面利用黑体辐射公式画出了不同温度下的辐射图
# 逆向求解出来了T，不知道更最小二乘法有啥关系？？
def ylog(nu, Inu):
    nu = nu * C * 100   # to unit HZ=(s^-1)
    coef = 2 * Planck * nu**3 / C**2
    # I_Jm2 : unit [J/m^2/sr]
    to_Mjy_per_Sr = 10**20
    temp = 1 + coef * to_Mjy_per_Sr / Inu

    return np.log(temp.astype(float))
    
    
def a2T(a):
    '''convert a to T by: T=h/(k a)
    Look out the unit transformation'''
    return Planck * C * 100 / (Boltzmann * a)

xarr = nu
yarr = ylog(xarr, Inu)

a = (xarr*yarr).sum() / (xarr**2).sum()

a2T(a)
#2.7235115127887295


# %%
