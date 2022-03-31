#######################################
#计算机上的微分
# 计算库 Sympy 解析微分
# 数值微分：有限差分近似 （Finite Difference）
# 自动微分：科学计算与人工智能的交叉 (Auto Differentiation)
#######################################
#In[]sympy做解析函数微分
# Step1: 定义自变量符号
# Step2: 定义解析函数的形式
# Step3: 使用 sympy.diff 函数返回函数的微分结果
# 详细见5.1 sympy专题
import sympy 

# Step1: define the variable
x = sympy.symbols("x")
# Step2: define the function 
def f(x):
    return x * sympy.exp(- x**2)

f(x)
#$\displaystyle x e^{- x^{2}}$
# Step3: calc the differentiation

sympy.diff(f(x), x)

#$\displaystyle - 2 x^{2} e^{- x^{2}} + e^{- x^{2}}$

#################小技巧1###################################
# 写文章的时候打 Latex 公式很麻烦，可以将 sympy 的计算结果输出为 latex 代码。

dfdx = sympy.diff(f(x), x)

sympy.print_latex(dfdx)
#- 2 x^{2} e^{- x^{2}} + e^{- x^{2}}

#################小技巧2######################################
#使用 subs 函数可以临时将 dfdx 中的 x 替换为特定数值

dfdx.subs(x, 1)
#$\displaystyle -0.367879441171442$
dfdx.subs(x, 0)
#$\displaystyle 1$






##################################################################
#数值微分：有限差分近似
#$$ {df \over dx} = {\rm lim}_{\Delta x\rightarrow 0} {f(x+ \Delta x) - f(x) \over \Delta x } $$
#In[]
def finite_difference(func, x, dx=0.01):
    assert(dx != 0)
    return (func(x+dx) - func(x)) / dx

finite_difference(f, 0.0)
#$\displaystyle 0.999900004999833$
#$$ {df \over dx} = - 2 x^{2} e^{- x^{2}} + e^{- x^{2}}$$
#解析微分在 x=0 处精确值为 1
#有限差分法在 x=0 处得到近似的数值解： 0.999900004999833
#In[]
import matplotlib.pyplot as plt
import numpy as np

# 这里作图看一下有限差分方法的误差
def comparison(dx):
    xcoord = np.linspace(0, np.pi, 200)
    # 解析微分的结果——之前计算的有，带入了x的值
    dfdx_ana = [dfdx.subs(x, xi) for xi in xcoord]
    # 有限差分的结果，dx默认0.01，
    dfdx_num = [finite_difference(f, xi, dx) for xi in xcoord] 
    
    plt.plot(xcoord, dfdx_num, 'ko--', label="finite difference")
    plt.plot(xcoord, dfdx_ana, 'r-', label="sympy: analytic")
    
    plt.legend(loc='best')
    plt.xlabel(r"$x$")
    plt.ylabel(r"$df/dx$")
# dx 小的时候，有限差分比较准确
comparison(dx=0.001)
comparison(dx=1)

from ipywidgets import interact

# 移动滑钮看到 dx 大的时候，有限差分误差较大
interact(comparison, dx=(0.001, 1))

#In[]对比sqrt(x) 差分和解析的精度
def f(x):
    return sympy.sqrt(x)
dfdx = sympy.diff(f(x), x)
interact(comparison, dx=(0.001, 1))

# %%
#自动微分Auto-differentiation
'''
自动微分编程是一个最近很流行的研究方向。这种方法与传统的数值微分和解析微分都有所不同。

    数值微分：会引入数值误差
    解析微分：在函数复杂的时候，根据链式规则，展开项很多，计算速度慢
    
自动微分保留了数值微分速度快和解析微分结果精确的优点，正成为一种新的计算物理编程范式。

自动微分在人工智能时代开始流行，因为 Tensorflow, pytorch 等深度学习库封装了自动微分功能。

https://www.robots.ox.ac.uk/~tvg/publications/talks/autodiff.pdf

自动微分通过在计算机上实现一些基本算术操作的微分，加上链式规则，自动从用户编写的函数 f(x)，推导出它的微分 f'(x)。

自动微分广泛应用于，

    人工智能 $ \theta = \theta - \epsilon \partial L / \partial \theta$
    逆问题 $y = f(x) \rightarrow x = f^{-1}(y)$
    牛顿法寻根 $x_{n+1} = x_{n} - f(x_n) / f'(x_n)$
    Stiff 常微分方程 $df / dt = s$

方法：把所有的数加上一个对偶数 $x \rightarrow x + \dot{x} \mathbf{d}$

其中 $\mathbf{d}$ 是一个符号，像虚数的表示符号 $i$ 一样。不同的是，$i^2 = -1$, 此处 $\mathbf{d}^2 = 0$.

使用这种方法, 用户定义的函数会自动出现一个对偶的自动微分项, 以 $\mathbf{d}$ 标示.
'''
#In[]
import sympy
import numpy as np
# 简单举例  f(x) = x e^{-x^2}
def f1(x):
    w1 = x
    w2 = w1 * w1
    w3 = np.exp(- w2)
    w4 = w1 * w3
    return w4

f1(1.0)
#0.36787944117144233


## 自动微分版本
def f_ad(x):
    w1 = x
    dw1 = 1
    
    w2 = w1 * w1
    dw2 = 2 * w1 * dw1
    
    w3 = np.exp(-w2)
    dw3 = - np.exp(-w2) * dw2
    
    w4 = w1 * w3
    dw4 = w1 * dw3 + dw1 * w3
    
    return w4, dw4
f_ad(1.0)
#(0.36787944117144233, -0.36787944117144233)

# %%
#######################################################
'''
运算符重载的方法实现自动微分编程
举例：计算机如何做复数的加减乘除

\begin{align} z_1 &= x_1 + i y_1 \\ z_2 &= x_2 + i y_2 \end{align}
底层语言只实现了实数的加减乘除，但是使用复数库，可以直接计算

$z_1 + z_2$
$z_1 - z_2$
$z_1 * z_2$
$z_1 / z_2$
复数库对 +， -， *， / 符号做了重载
'''
#In[]
class DNumber:
    '''自动微分中的对偶数类，对 +， -， *， /，幂次符号做了重载'''
    def __init__(self, x, dx):
        self.val = x
        self.dval = dx
    
    def __repr__(self):
        '''使用 print(DNumber(1, 2)) 时输出：1 + 2 d'''
        return f'{self.val} + {self.dval} d'
        
    def __add__(self, other):
        '''overload a + b'''
        if isinstance(other, float) or isinstance(other, int):
            val = self.val + other
            dval = self.dval
        if isinstance(other, DNumber):
            val = self.val+other.val
            dval = self.dval + other.dval
            
        return DNumber(val, dval)
    
    def __iadd__(self, other):
        '''overload a += b'''
        self.val = self.val + other.val
        self.dval = self.dval + other.dval
        return self
    
    def __mul__(self, other):
        ''' overload x * y  or const * x
        (x + dx d)*(y + dy d) = x*y + (xdy + ydx) d'''
        if isinstance(other, float) or isinstance(other, int):
            val = other * self.val
            dval = other * self.dval
        
        if isinstance(other, DNumber):
            val = self.val * other.val
            dval = self.val * other.dval + other.val * self.dval
            
        return DNumber(val, dval)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __pow__(self, n):
        if isinstance(n, float) or isinstance(n, int):
            val = self.val**n
            dval = n * self.val**(n-1) * self.dval
        elif isinstance(n, DNumber) :
            raise(Exception("Pow(DNumber, DNumber) is not implemented yet"))
        return DNumber(val, dval)
    
    #缺少个转置的算法
    
s = DNumber(0.1, 1)
s + DNumber(0.2, 0)
#0.30000000000000004 + 1 d
s += DNumber(0.2, 0)
s
#0.30000000000000004 + 1 d
x = DNumber(0.1, 1)
x * x
#0.010000000000000002 + 0.2 d
x**3
#0.0010000000000000002 + 0.030000000000000006 d


#In[]
'''
多个变量的自动微分
上面例子中 f(x) 是 x 的单变量函数，$\dot{x}=1$.

如果是多变量函数 f(x, y), 要求对 x 求微分，则应取

$\dot{x}=1, \dot{y}=0$.

举例说明：

$f(x, y)= 3 x^2 y + x$

${\partial f \over \partial x} = 6 x y + 1$

在 (x, y) = (1, 1) 时，$f(x, y)=4.0$, $df/dx = 7.0$。
'''
def f2d(x, y):
    '''
    Args: 
    :x: DNumber
    :y: DNumber
    :return: f(x, y) = 3*x**2*y + x 
    and \partial f/\partial x '''
    return 3 * x**2 * y + x
# 求 (x,y)=(1,1) 时 f(x, y) 与 df/dx
x = DNumber(1.0, 1.0)
y = DNumber(1.0, 0.0)
print("x =", x)
print("y =", y)
print("3x^2 y + x = ", f2d(x, y))
#x = 1.0 + 1.0 d
#y = 1.0 + 0.0 d
#x^2 y + x =  4.0 + 7.0 d
#偏微分见5.1 
#复数的偏微分和转置都没有尝试

# %%
