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

dfdx.subs(x, 1.)
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
import matplotlib.pyplot as plt
import numpy as np

# 这里作图看一下有限差分方法的误差
def comparison(dx):
    xcoord = np.linspace(0, np.pi, 20)
    # 解析微分的结果
    dfdx_ana = [dfdx.subs(x, xi) for xi in xcoord]
    # 有限差分的结果
    dfdx_num = [finite_difference(f, xi, dx) for xi in xcoord] 
    
    plt.plot(xcoord, dfdx_num, 'ko--', label="finite difference")
    plt.plot(xcoord, dfdx_ana, 'r-', label="sympy: analytic")
    
    plt.legend(loc='best')
    plt.xlabel(r"$x$")
    plt.ylabel(r"$df/dx$")
# dx 小的时候，有限差分比较准确
comparison(dx=0.001)