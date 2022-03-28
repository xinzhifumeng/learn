


#In[60]预估任务难度
import numpy as np
import matplotlib.pyplot as plt

def plot_time(dt = 1.0E-9):
    N = np.logspace(1, 6)
    t = N**2 * dt
    plt.loglog(N, t)
    plt.xlabel("num of particles")
    plt.ylabel("cpu time (s)")

plot_time()


#In[37] 大数+小数困难的解决方案
#大数加小数遇到的困难
#float32 精度下，下面这两个数相加，结果是多少？

A = 3.1415927

B = 0.00000005

#如果 B 的值小于 A 的舍入误差，则 A+B 的计算与B无关。

# 小数被吃掉
np.float32(np.pi) + np.float32(5E-8)
#3.1415927
A = np.float32(1.0E2)

B = np.float32(1.0E-6)

A + B
#100.0

#举例：夸克胶子等离子体冷却超曲面上发射出的强子数计算使用 Cooper-Frye 公式，
#计算中将整个球面分割成几百万个小多边形，计算流过这些多边形的粒子数, 最后对几百万个小片求和。
#在将代码从 CPU （float64）到 GPU （float32） 上移植时，发现累积误差可以大到 5%!

# 大数加小数困难示例：小数连加

from tqdm import tqdm

loops = int(1E7)
res = np.float32(0.0)
dx = np.float32(1.0E-7)

for i in tqdm(range(loops)):
    res += dx

# 真实结果
ground_truth = loops*dx

print("theoretical results: %s"%(ground_truth))
print("accumulated sum：", res)
print("relative error = ", (res-ground_truth)/ground_truth)

#theoretical results: 1.0000000116860974
#accumulated sum： 1.0647675
#relative error =  0.06476746745356905

#################################################
#为了计算速度考虑，如果不想用 double（即 float64）数据类型，又希望大量数字的求和结果比较精确， 可以考虑使用如下两种方案：

#Kahan 求和公式（解决串行求和时大数吃小数的问题）
#将串行求和转化为并行求和
#http://lgpang.gitee.io/mlcphysics/htmls/numerical_traps.html
from tqdm import tqdm

def kahan_sum(arr):
    '''连加操作中解决大数吃小数的问题
    :arr: numpy array，存储 float 类型
    :return: arr 中所有元素的和'''
    sum_ = np.float32(0)
    correction = np.float32(0)
    for addend in tqdm(arr):
        addend += correction                  #  <--  
        temp_sum = sum_ + addend              #     \
        addend_high = temp_sum - sum_         #     \
        correction = addend - addend_high     #   --
        sum_ = temp_sum                       # update
        
    return sum_
#举例

arr = np.ones(int(1.0E6), dtype=np.float32) * 1.0E-6

sum_ = np.float32(0)
for x in tqdm(arr):
    sum_ += x 
    
print("sum(arr)=", res)
#100%|███████████████████████████████████████████████████████████████████| 1000000/1000000 [00:00<00:00, 2881855.25it/s]
#sum(arr)= 1.0090389
kahan_sum(arr)
#100%|███████████████████████████████████████████████████████████████████| 1000000/1000000 [00:00<00:00, 1620672.00it/s]



#In[20]避免两个浮点数的相等（==）比较
#因为计算机上浮点数有舍入误差，对浮点数做 == 比较有时会出现不可预测的错误。

#举例：

a = 3.14159268

b = 3.14159269

#判断 a==b 返回 True 还是 False?

#对于 float32 类型，最后的 8 和 9在舍入误差上，我们希望它返回 True

# 默认使用 float64 类型

a == b
False
# 比较好的做法是 np.isclose() 或 np.allclose() 函数
# 尤其是在对比数值解与解析解时
np.isclose(a, b)
True
# 使用 np.isclose(SHIFT + TAB), 在函数括弧处按 SHIFT+TAB 键看函数介绍
# 或 help(np.isclose)


