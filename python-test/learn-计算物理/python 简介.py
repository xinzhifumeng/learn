
#In[19]
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


#In[21]
'''
使用 numba.jit 加速
python 的原始循环体比较慢，有两种方式加速，

numpy 的 数组操作 模式
numba 的 jit （just in time compilation 即时编译)
'''

from numba import jit

@jit
def jit_sum():
    x_sum = 0
    for i in range(10000000):
        x_sum += 1.0E-5
    return x_sum

jit_sum()

# %%
