###########################################################
########################学习内容############################
#Sympy 解析积分
#最常用的数值积分方法
#数值积分原理介绍
#数值积分在强子共振气体状态方程计算中的应用
###########################################################


###########################################################
# 1 sympy解析积分
#In[]
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import seaborn as sns
'''
sns.set_style("whitegrid") 
#横坐标有标线，纵坐标没有标线，背景白色

sns.set_style("darkgrid") 
#默认，横纵坐标都有标线，组成一个一个格子，背景稍微深色

sns.set_style("dark")
#背景稍微深色，没有标线线

sns.set_style("white")
#背景白色，没有标线线

sns.set_style("ticks") 
#xy轴都有非常短的小刻度

sns.despine(offset=30,left=True) 
#去掉上边和右边的轴线，offset=30表示距离轴线（x轴）的距离,left=True表示左边的轴保留

'''

sns.set_context("talk")
 
x, l = sym.symbols('x, l')
psi = sym.sqrt(2/l) * sym.sin(sym.pi * x / l)
psi

from sympy.plotting import plot

# 可视化基态波函数
plot(psi.subs({l:1}), xlim=(0, 1))
plot((psi*psi).subs({l:1}), xlim=(0, 1))

## 位置的平均值：积分计算
avg_x = sym.integrate(psi*x*psi, (x, 0, l))

### 化简 simplify 得到平均位置
sym.simplify(avg_x)
#$\displaystyle \frac{l}{2}$

# 检查 sympy 里的虚数符号
sym.I * sym.I
#$\displaystyle -1$

# 检查 sympy 中的微分计算 d psi / dx
sym.diff(psi, x)
#$\displaystyle \frac{\sqrt{2} \pi \sqrt{\frac{1}{l}} \cos{\left(\frac{\pi x}{l} \right)}}{l}$

## ## 动量的平均值：微分算子 + 积分计算
hbar = sym.symbols("hbar")

p_rho = psi * (-sym.I * hbar) * sym.diff(psi, x)

avg_p = sym.integrate(p_rho, (x, 0, l))
#x取0-1

sym.simplify(avg_p)
####################################################################
#In[] 最常用的数值积分方法

from scipy.integrate import quad
# 1 维数值积分用 quad
# 2 维数值积分用 dblquad
# 3 维数值积分用 tplquad
# n 维数值积分用 nquad

## help(quad)
# 验证 sympy 不能给出椭圆周长的解析积分公式
'''
举例：可能很多人没意识到，椭圆的周长没有简单的解析公式，只能数值求解，

\begin{align} {x^2 \over a^2} + {y^2 \over b^2} = 1 \end{align}
设方位角为 $\theta$, 则椭圆上的任一点的坐标可以用 $\theta$ 表示为，

\begin{align} x &= a \cos \theta \\ y &= b \sin \theta \end{align}
此时椭圆周长的计算公式为， 
\begin{align} L & = \int dl = \int \sqrt{dx^2 + dy^2}\\ & = \int_0^{2\pi} \sqrt{({dx \over d\theta})^2 + ({dy \over d\theta})^2} d\theta \\ & = \int_0^{2\pi} \sqrt{a^2\sin^2\theta + b^2\cos^2\theta} d\theta \end{align}
'''
a, b, theta = sym.symbols('a b theta')

L = sym.integrate(sym.sqrt(a**2 * sym.sin(theta)**2 + b**2 * sym.cos(theta)**2), (theta, 0, 2*sym.pi))
sym.simplify(L)
#$\displaystyle \int\limits_{0}^{2 \pi} \sqrt{a^{2} \sin^{2}{\left(\theta \right)} + b^{2} \cos^{2}{\left(\theta \right)}}\, d\theta$
def ellipse_circumference(a = 4, b = 3):
    '''计算椭圆周长
    :a: 椭圆长轴长度
    :b: 椭圆短轴长度'''
    f = lambda t: np.sqrt(a**2 * np.sin(t)**2 + b**2 * np.cos(t)**2)
    circum, err = quad(f, 0, 2*np.pi)
    return circum, err

# 首先验证长轴等于短轴时，椭圆周长与圆周长公式相符
circ, err = ellipse_circumference(a=4, b=4)
np.isclose(circ, 2*np.pi * 4)#近似比较两个数大小
True

ellipse_circumference(a=4, b=3)
#(22.103492160709497, 2.2162729348778595e-08)
## 对比椭圆周长的低阶精度经验公式 L = 2 pi b + 4 (a - b)

def circ_approximate(a, b):
    if b > a: a, b = b, a
    return 2 * np.pi * b + 4 * (a - b)

circ_approximate(a=4, b=3)
#22.84955592153876


#######################################################
#In[]低维数值积分原理
#没看明白
#等 间距数值积分：牛顿科茨(梯形公式，辛普森积分）
# 不等间距积分：高斯 quadrature
#http://lgpang.gitee.io/mlcphysics/htmls/integration_on_computer.html#学习目标
#对于 n=2, 只有两个节点¶
#这两个节点等于积分上下限，$x_0=a$, $x_1=b$ \begin{align} f_2(x) & = f(x_0) {x - x_1 \over x_0 - x_1} + f(x_1) {x - x_0 \over x_1 - x_0}\\ & = f(a) {x - b \over a - b} + f(b) {x - a \over b - a} \end{align} 此时，得到系数 \begin{align} A_0 &= \int_a^b {x - b \over a - b} dx \\ A_1 & = \int_a^b {x - a \over b - a} dx \end{align}

a, b, x = sym.symbols("a b x")

A0 = sym.integrate((x - b)/(a - b), (x, a, b))

A1 = sym.integrate((x - a)/(b - a), (x, a, b))
sym.simplify(A0)
#$\displaystyle - \frac{a}{2} + \frac{b}{2}$
sym.simplify(A1)
#$\displaystyle - \frac{a}{2} + \frac{b}{2}$
#此时得到一阶 Newton-Cotes 积分公式 -- 梯形公式（上底加 下底，乘高除二等面积），

#\begin{align} F = {b - a \over 2 }\left[ f(a) + f(b) \right] \end{align}
# %%
