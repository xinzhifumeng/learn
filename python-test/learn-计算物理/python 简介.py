'''
显示计算进程
使用 numba.jit 加速
字典类型
函数-lorentz_gamma
递归函数 勒让德多项式
读写文件
'''



#In[19]显示计算进程
import numpy as np
import math
import matplotlib.pyplot as plt 

x_sum = 0
xlist = [math.sin(i*math.pi) for i in range(1000000)]

from tqdm import tqdm
for i in tqdm(range(1000000)):
    x_sum += xlist[i]

print(x_sum)
#当我们对一个非常大的列表进行长时间计算时，估计大概需要的计算时间非常重要；

#使用 tqdm 库，可以显示计算进程


#In[21]使用 numba.jit 加速
'''
python 的原始循环体比较慢，有两种方式加速，
    numpy 的 数组操作 模式
    numba 的 jit （just in time compilation 即时编译)
'''

from numba import jit

@jit
#@符号的作用还没太搞明白
def jit_sum():
    x_sum = 0
    for i in range(10000000):
        x_sum += 1.0E-5
    return x_sum

jit_sum()

#In[22] 字典类型
studentx = {'id':3300, 'score':99, 'gender':'female'}

studentx['id']
3300
studentx['score'] 
99
for key, value in studentx.items():
    print(key, value)

#In[27]函数-lorentz_gamma
# 狭义相对论
import math
import numpy as np
def lorentz_gamma(v):
    '''
    args:
        v: velocity over speed of the light, in [0, 1)
    return: lorentz gamma factor 1/sqrt(1-v*v)
    '''
    assert(math.fabs(v)<1.0)#类似if v的绝对值小于1
    return 1/np.sqrt(1 - v*v)

lorentz_gamma(0.9999)
help(lorentz_gamma)
'''
Help on function lorentz_gamma in module __main__:

lorentz_gamma(v)
    args:
        v: velocity over speed of the light, in [0, 1)
    return: lorentz gamma factor 1/sqrt(1-v*v)

#############################################################
根据狭义相对论

$ E = m \gamma = \frac{m}{\sqrt{1 - v^2}}$

我们来定义一个函数，计算高能核碰撞在不同能量下，原子核的飞行速度 v
'''
# Python 函数的参数可以提供默认数值，比如此处默认 sqrtsnn=200

def velocity_of_nucleus(sqrtsnn=200):
    '''compute the velocity of nucleus given the sqrt{s_{NN}} per pair of nucleons
    args:
        sqrtsnn: the center of mass frame energy of one pair of nucleons.
        e.g., the Au+Au 200 GeV collision, each nucleon has energy 100 GeV
    return: 
        the velocity of the nucleon
    '''
    energy_ = 0.5 * sqrtsnn
    nucleon_mass = 0.938
    gamma = energy_ / nucleon_mass
    velocity = math.sqrt(1 - 1/(gamma**2))
    return velocity
# 如果函数参数有默认值，可直接调用

velocity_of_nucleus()
#Out 0.9999560068323006
# 也可显式赋值调用

velocity_of_nucleus(sqrtsnn=200)
#Out 0.9999560068323006
# LHC 能量 sqrtsnn = 2760 GeV 碰撞
vlhc = velocity_of_nucleus(sqrtsnn=2760)
vlhc
#Out 0.9999997689970328
# 在 LHC 能量下（$\sqrt{s_{NN}}=2760$ GeV）, 原子核被加速到了百分之 99.99998 的光速！

# 原子核沿束流方向的厚度被压缩了 1471 倍，collision of pancakes!

lorentz_gamma(vlhc)

#Out 1471.2153520044649
#In[25] 递归函数 勒让德多项式
'''
已知 n = 1 时结果
知道 n 到 n+1 的递推公式
例子：勒让德多项式

$$P_0(x) = 1, \quad\; P_1(x) = x,\quad\; P_{n+1}(x) = \left[ (2n+1) x P_n(x) - n P_{n-1} (x)\right]/(n+1) $$
https://baike.baidu.com/item/%E5%8B%92%E8%AE%A9%E5%BE%B7%E5%A4%9A%E9%A1%B9%E5%BC%8F/5335504?fr=aladdin
'''
import numpy as np
import math
import matplotlib.pyplot as plt
def Pn(x, n):
    '''此处，Pn 是递归函数，需要调用自己计算 Pn(n-1) 与 Pn(n-2)'''
    if n == 0: 
        return np.ones_like(x)
    elif n == 1: 
        return x
    else:
        return ((2*n-1)*x*Pn(x, n-1) - (n-1)*Pn(x, n-2))/n
x = np.linspace(0, 1, 100)

for n in range(5):
    legi = Pn(x, n)
    plt.plot(x, legi, label="%s"%n)
    plt.xlabel("x")
    plt.ylabel(r"$P_n(x)$")
    plt.legend(loc="best")


#In[44]读写文件
############################################
# 最常用的文件格式：txt, csv, hdf5

# csv 是 txt 类型数据格式 （交互性较好）
# hdf5 是二进制类型数据格式 （数据载入速度比较快）
# 少量数据用 txt，大量数据用 hdf5
# 下面介绍几种文件读写方法。

#############################################
#In[44] 1. 使用 python 系统 io 进行 txt 文件读写
'''
with open("test.txt", "w") as fout:
    fout.write("hello world")
'''
#这条命令打开一个文件 test.txt, 向其中写入 "hello world", 并关闭文件。

#使用 with 语句可以保证在读写文件失败的时候，文件自动关闭，推荐使用。

############# 打开文件，向其中写 hello world###############
with open("test.txt", "w") as fout:
    fout.write("hello world")
    
# 此时可以检查，目录下多了 test.txt
# !cat 是命令行工具，可以输出文件内容
#!cat test.txt 
#hello world

###################  读文件，并输出#########################
with open("test.txt", "r") as fin:
    txt = fin.read()
    
print("Read from test.txt :", txt)
#Read from test.txt : hello world
##########################################################
#In[46] 2. 使用 numpy 库进行数据读写
'''
np.loadtxt, np.savetxt 分别可以读写数据文件

速度比 pandas.read_csv 函数慢，但不容易出错
'''
# 产生 5 行 4 列 随机数，范围 [0, 1)
rand_data = np.random.rand(5, 4)

rand_data
'''
array([[0.70806862, 0.36290251, 0.42432538, 0.08019838],
       [0.98111599, 0.87287279, 0.52940939, 0.05581787],
       [0.62925162, 0.41376343, 0.42454019, 0.29796559],
       [0.34702341, 0.5126459 , 0.03086713, 0.0926828 ],
       [0.79193308, 0.26338727, 0.95215944, 0.03741891]])'''
#########################保存数据到硬盘#########################

np.savetxt("rand_data.txt", rand_data)

#!cat rand_data.txt 

############# 从硬盘文件 rand_data.txt 读取数据#################
mydata = np.loadtxt("rand_data.txt")
mydata
'''
array([[0.70806862, 0.36290251, 0.42432538, 0.08019838],
       [0.98111599, 0.87287279, 0.52940939, 0.05581787],
       [0.62925162, 0.41376343, 0.42454019, 0.29796559],
       [0.34702341, 0.5126459 , 0.03086713, 0.0926828 ],
       [0.79193308, 0.26338727, 0.95215944, 0.03741891]])'''
###############################################################
#In[49] 3. 使用 pandas 读写文件
'''
pandas 可以读取 csv、excel、hdf5、json、xml 等文件格式

这里仅对 csv 格式文件进行示例。

这里需要先产生 DataFrame 类型数据，然后对其进行保存。
'''
import pandas as pd

df = pd.DataFrame(data=mydata, 
                  columns=['col1', 'col2', 'col3', 'col4'])

# pandas 的 DataFrame 多存储了每一列的名字
df.to_csv("pd_data.csv")

#!cat pd_data.csv
'''
,col1,col2,col3,col4
0,0.7080686218118419,0.36290251454428446,0.4243253816559156,0.08019837552752551
1,0.9811159855768012,0.8728727884847021,0.5294093870870228,0.055817872242783895
2,0.6292516238478628,0.41376343074291366,0.4245401871107133,0.29796558736270873
3,0.34702341270026316,0.5126458999597934,0.03086713413454656,0.09268280229837533
4,0.7919330820168982,0.26338726670589185,0.9521594379817641,0.0374189050779119'''

pd_data = pd.read_csv("pd_data.csv", index_col=0)

pd_data.head()
'''
col1	col2	col3	col4
0	0.708069	0.362903	0.424325	0.080198
1	0.981116	0.872873	0.529409	0.055818
2	0.629252	0.413763	0.424540	0.297966
3	0.347023	0.512646	0.030867	0.092683
4	0.791933	0.263387	0.952159	0.037419
'''
#########################################################
# In[51] 4. 使用 h5py 读写 hdf5 文件
'''
此处需要 h5py 库，可以在 Anaconda 中安装，或在命令行安装

#pip install --user h5py
'''
import h5py

# ##将数据写入文件，可以使用 create_dataset 创建多个 dataset 
with h5py.File("h5_file.h5", "w") as h5:
    h5.create_dataset("rand", data=mydata)

# 从 h5 文件中读取数据，h5["rand"][...] 将其表示为 numpy 数组
with h5py.File("h5_file.h5", "r") as h5:
    h5data = h5["rand"][...]

print(h5data)

'''
[[0.70806862 0.36290251 0.42432538 0.08019838]
 [0.98111599 0.87287279 0.52940939 0.05581787]
 [0.62925162 0.41376343 0.42454019 0.29796559]
 [0.34702341 0.5126459  0.03086713 0.0926828 ]
 [0.79193308 0.26338727 0.95215944 0.03741891]]'''
 
 