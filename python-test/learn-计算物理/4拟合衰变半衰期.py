############################################################
# 虽然涉及了一元最小二乘法拟合，但是没对算法进行深入研究
# 正交多项式做最小二乘法拟合仍需要进一步学习
############################################################
#In[]
# 数据从 宁平治老师的《原子核物理学简明教程》中获取，
# 保存为 csv 格式的代码如下


import pandas as pd

# 母原子核，
Nucleus = ['Po206', 'Po208', 'Po210', 'Po212', 'Po214', 'Po216', 
           'U228', 'U230', 'U232', 'U234', 'U236', 'U238',
           'Pu238', 'Pu240', 'Pu242', 'Pu244', 
           'Cm240', 'Cm242', 'Cm244', 'Cm246']

# the energy of alpha particle
Ealpha = [5.22, 5.11, 5.31, 8.78, 7.68, 6.78,
          6.69, 5.89, 5.32, 4.77, 4.49, 4.20,
          5.50, 5.17, 4.90, 4.66,
          6.29, 6.12, 5.80, 5.39]

# halflife
tau_half = [8.8, 2.9, 138, 0.3, 164, 0.15,
            9.1, 20.8, 72, 2.47E5, 2.39E7, 4.51E9,
            86, 6.58E3, 3.79E5, 8.0E7, 26.8, 163, 17.6, 5.5E3]

# units of halflife
tau_units = ['day', 'year', 'day', 'microsecond', 'microsecond', 'second',
            'month', 'day', 'year', 'year', 'year', 'year',
            'year', 'year', 'year', 'year', 
            'day', 'day', 'year', 'year']


df1 = pd.DataFrame({"nucleus":Nucleus,
                    "Ealpha":Ealpha,
                    "tau_half":tau_half,
                    "tau_units":tau_units})

df1.to_csv("alpha_decay.csv", index=False)


'''数据格式
	nucleus	Ealpha	tau_half	tau_units	tau_insecond
0	Po206	5.22	8.800000e+00	day	7.603200e+05
1	Po208	5.11	2.900000e+00	year	9.145440e+07
2	Po210	5.31	1.380000e+02	day	1.192320e+07

'''
#################################################################


#In[]
# 读取写好的半衰期数据，并改日期格式

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建文件夹 data, 将 alpha_decay.csv 文件放在 data/ 文件夹下
df = pd.read_csv("data/alpha_decay.csv")


# 这段代码用于单位转换
units = df['tau_units']

def cond(unit):
    '''将所有单位统一为秒'''
    if unit=='day': return 24*3600
    if unit=='year': return 365*24*3600
    if unit=='month': return 30*24*3600
    if unit=='microsecond': return 1.0E-6
    if unit=='second': return 1

# unit_trans 保存了所有半衰期单位到秒的转化
unit_trans = [cond(u) for u in units]

# tau 转换为 second （秒）的单位
tau_insecond = df['tau_half'] * np.array(unit_trans)

# 在 DataFrame 中新开辟一列数据
df['tau_insecond'] = tau_insecond

df.head()


#In[]
# 排序并画图
# 对 DataFrame 按找 Ealpha 的值排序，可有可无好像
df = df.sort_values('Ealpha')
W = np.log(2) / df['tau_insecond']
Ealpha = df['Ealpha']
plt.figure(figsize=(6, 4))
plt.plot(1/np.sqrt(Ealpha), np.log10(W), 'ro')
plt.xlabel(r'$1/\sqrt{E_{\alpha}}$')
plt.ylabel(r'$\log_{10} W$')


##############################################################
#In[]
# 最小二乘法拟合
# 网上找个了python 实现拟合一元最小二乘法的python代码，改了数据部分直接用了
# https://blog.csdn.net/deramer1/article/details/79055281

import matplotlib.pyplot as plt
from pylab import mpl
"""一元线性拟合
采用的拟合数据为xi=1,2,3,4,5,6,7
对应的相应函数值yi=0.5,2.5,2,4,3.5,6,5.5
"""
W = np.log(2) / df['tau_insecond']
Ealpha = df['Ealpha']
plt.plot(1/np.sqrt(Ealpha), np.log10(W), 'ro')
x = 1/np.sqrt(Ealpha)
y = np.log10(W)
 
 
"""完成拟合曲线参数计算"""
def liner_fitting(data_x,data_y):
      size = len(data_x)
      i=0
      sum_xy=0
      sum_y=0
      sum_x=0
      sum_sqare_x=0
      average_x=0
      average_y=0
      while i<size:
          sum_xy+=data_x[i]*data_y[i]
          sum_y+=data_y[i]
          sum_x+=data_x[i]
          sum_sqare_x+=data_x[i]*data_x[i]
          i+=1
      average_x=sum_x/size
      average_y=sum_y/size
      return_k=(size*sum_xy-sum_x*sum_y)/(size*sum_sqare_x-sum_x*sum_x)
      return_b=average_y-average_x*return_k
      return [return_k,return_b]
 
 
"""完成完后曲线上相应的函数值的计算"""
def calculate(data_x,k,b):
    datay=[]
    for x in data_x:
        datay.append(k*x+b)
    return datay
 
 
"""完成函数的绘制"""
def draw(data_x,data_y_new,data_y_old):
    plt.plot(data_x,data_y_new,label="拟合曲线",color="black")
    plt.scatter(data_x,data_y_old,label="离散数据")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title("一元线性拟合数据")
    plt.legend(loc="upper left")
    plt.show()
 
 
parameter = liner_fitting(x,y)
draw_data = calculate(x,parameter[0],parameter[1])
draw(x,draw_data,y)

# %%
