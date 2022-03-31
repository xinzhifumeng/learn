##########################################################
# Python 中的Sympy详细使用
#        遇到复杂计算找python绝对不让你失望，# sympy是一个Pyt
# hon的科学计算库，用一套强大的符号计算体系完成# 诸如多项式求值
# 、求极限、解方程、求积分、微分方程、级数展开、# 矩阵运算等等计
# 算问题。虽然Matlab的类似科学计算能力也很强大，# 但是Python以
# 其语法简单、易上手、异常丰富的三方库生态，个人认# 为可以更优雅
# 地解决日常遇到的各种计算问题。
###########################################################       

###########################################################  
# 1、表达式与表达式求值：

#In[]--------多项式求解--------
import sympy 

#定义变量
x=sympy.Symbol('x')
fx=5*x+4
#使用evalf函数传值
y1=fx.evalf(subs={x:6})
print(y1)
#34

#In[]多元表达式
x=sympy.Symbol('x')
y=sympy.Symbol('y')
fx=x*x+y*y
result=fx.evalf(subs={x:3,y:4})
print(result)
#25


###########################################################
# 2、函数方程求解：

#In[]解方程 有限解
#定义变量
x=sympy.Symbol('x')
y=sympy.Symbol('y')
fx=x*3+9
#可求解直接给出解向量
print(sympy.solve(fx,x))
#-3

#In[]解方程无穷多解
#定义变量
x=sympy.Symbol('x')
y=sympy.Symbol('y')
fx=x*3+y**2
#得到是x与y的关系式，
print(sympy.solve(fx,x,y))
 #[(-y**2/3, y)]

#In[]解方程组
#定义变量
x=sympy.Symbol('x')
y=sympy.Symbol('y')
f1=x+y-3
f2=x-y+5
sympy.solve([f1,f2],[x,y])
#{x: -1, y: 4}  

##################################################################
# 3、求和 
#In[]求和
import sympy
#定义变量
n=sympy.Symbol('n')
f=2*n
#前面参数放函数，后面放变量的变化范围
s=sympy.summation(f,(n,1,100))
print(s)

#In[] 解带有求和式的方程 ：
#sum_(i=1)^5 {i*x}+10*x=15
#解释一下，i可以看做是循环变量，就是x自己加五次
#先定义变量，再写出方程
x=sympy.Symbol('x')
i=sympy.Symbol('i')
f=sympy.summation(i*x,(i,1,5))+10*x-15
result=sympy.solve(f,x)
print(result)
         

##############################################################
#4、求极限
# 注意，math包中sin和很多数学函数会报错，要用sympy中的
# 无穷大用 sympy.oo 表示

#In[]求极限使用limit方法
#定义变量与函数
x=sympy.Symbol('x')
f1=sympy.sin(x)/x
f2=(1+x)**(1/x)
f3=(1+1/x)**x
#三个参数是 函数，变量，趋向值
lim1=sympy.limit(f1,x,0)
lim2=sympy.limit(f2,x,0)
lim3=sympy.limit(f3,x,sympy.oo)
print(lim1,lim2,lim3)


#############################################################
# 5、求导


#In[]求导使用diff方法
x=sympy.Symbol('x')
f1=2*x**2+3*x+6
#参数是函数与变量
f1_=sympy.diff(f1,x)
print(f1_)
#25
f2=sympy.sin(x)
f2_=sympy.diff(f2,x)
print(f2_)
 
#In[]求偏导
y=sympy.Symbol('y')
f3=2*x**2+3*y**4+2*y*x
#对x，y分别求导，即偏导
f3_x=sympy.diff(f3,x)
f3_y=sympy.diff(f3,y)
print(f3_x)
print(f3_y)


######################################################
# 6、求定积分


#In[]求定积分用 integrate方法
x=sympy.Symbol('x')
f=2*x
#参数传入 函数，积分变量和范围
result=sympy.integrate(f,(x,1,2))
print(result)


 #上面的求法有点烂，难的就罢工不干了，我丢，还是喜欢scipy，如下：
#http://liao.cpython.org/scipy18/  scipy 还能解决很多数值计算，包括多重积分。
from scipy import integrate
def f(x):
    return 2*x
v, err = integrate.quad(f, 1, 2)# err为误差
print(v)




####################################################
#In[]以下计算多重积分： 
#求多重积分，先求里面的积分，再求外面的
x,t=sympy.symbols('x t')
f1=2*t
f2=sympy.integrate(f1,(t,0,x))
result=sympy.integrate(f2,(x,0,3))
print(result)
        
####################################################
#7、求不定积分
         
#In[]求不定积分其实和定积分区别不大
x=sympy.Symbol('x')
f=(sympy.E**x+2*x)
f_=sympy.integrate(f,x)
print(f_)

#######################################################
#In[] 8、数学符合补充：
 
#数学符合
#虚数单位i
sympy.I
#自然对数低e
sympy.E
#无穷大
sympy.oo
#圆周率
sympy.pi
#求n次方根
sympy.root(8,3)
#求对数
sympy.log(1024,2)
#求阶乘
sympy.factorial(4)
#三角函数
sympy.sin(sympy.pi)
sympy.tan(sympy.pi/4)
sympy.cos(sympy.pi/2)

##########################################################
#In[] 9、公式展开与折叠
x=sympy.Symbol('x')
#公式展开用expand方法
f=(1+2*x)*x**2
ff=sympy.expand(f)
print(ff)
#公式折叠用factor方法
f=x**2+1+2*x
ff=sympy.factor(f)
print(ff)

############################################################
#In[] 10、公式分离与合并（分数的分离与合并）
x=sympy.Symbol('x')
y=sympy.Symbol('y')
#公式展开用apart方法,和expand区别不是很大，常用于分数进行分离
f=(x+2)/(x+1)
ff=sympy.apart(f)
print(ff)
#公式折叠用tegother方法
f=(1/x+1/y)
ff=sympy.together(f)
print(ff)


###########################################################
#In[]11、表达式简化
#simplify( )普通的化简
sympy.simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
#x−1
#trigsimp( )三角化简
sympy.trigsimp(sympy.sin(x)/sympy.cos(x))
#tan(x)
#powsimp( )指数化简
sympy.powsimp(x**2*x**3)
#x**5
# %%
