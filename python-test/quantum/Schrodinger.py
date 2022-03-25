import numpy as np
import matplotlib.pyplot as plt 

'''
# np.linspace 将区间 [-2, 2] 离散化为 100 个坐标点
x = np.linspace(-2, 2, 100)
# 计算 100 个坐标点上的函数值 f
f = np.sin(x) / x
plt.plot(x, f)
plt.show()
#上面为画图的一个小测试
作者：hahakity
链接：https://zhuanlan.zhihu.com/p/264940250


'''
class Schrodinger:
    def __init__(self, potential_func, 
                 mass = 1, hbar=1,
                 xmin=-5, xmax=5, ninterval=1000):
        self.x = np.linspace(xmin, xmax, ninterval)    
        self.U = np.diag(potential_func(self.x), 0)        
        self.Lap = self.laplacian(ninterval)        
        self.H = - hbar**2 / (2*mass) * self.Lap + self.U       
        self.eigE, self.eigV = self.eig_solve()
            
        
    def laplacian(self, N):
        '''构造二阶微分算子：Laplacian'''
        dx = self.x[1] - self.x[0]
        return (-2 * np.diag(np.ones((N), np.float32), 0)
            + np.diag(np.ones((N-1), np.float32), 1)
            + np.diag(np.ones((N-1), np.float32), -1))/(dx**2)
    
    def eig_solve(self):
        '''解哈密顿矩阵的本征值，本征向量；并对本征向量排序'''
        w, v = np.linalg.eig(self.H)  
        idx_sorted = np.argsort(w)     
        return w[idx_sorted], v[:, idx_sorted]
    
    def wave_func(self, n=0):
        return self.eigV[:, n]

    def eigen_value(self, n=0):
        return self.eigE[n]
    
    def check_eigen(self, n=7):
        '''check wheter H|psi> = E |psi> '''
        with plt.style.context(['science', 'ieee']):
            HPsi = np.dot(self.H, self.eigV[:, n])
            EPsi = self.eigE[n] * self.eigV[:, n]
            plt.plot(self.x, HPsi, label=r'$H|\psi_{%s} \rangle$'%n)
            plt.plot(self.x, EPsi, '-.', label=r'$E |\psi_{%s} \rangle$'%n)
            plt.legend(loc='upper center')
            plt.xlabel(r'$x$')
            plt.ylim(EPsi.min(), EPsi.max() * 1.6)
            
    def plot_density(self, n=7):
        with plt.style.context(['science', 'ieee']):
            rho = self.eigV[:, n] * self.eigV[:, n]
            plt.plot(self.x, rho)
            plt.title(r'$E_{%s}=%.2f$'%(n, self.eigE[n]))
            plt.ylabel(r'$\rho_{%s}(x)=\psi_{%s}^*(x)\psi_{%s}(x)$'%(n, n, n))
            plt.xlabel(r'$x$')
            
    def plot_potential(self):
        with plt.style.context(['science', 'ieee']):
            plt.plot(self.x, np.diag(self.U))
            plt.ylabel(r'potential')
            plt.xlabel(r'$x$')
            
    #尝试将概率密度分布时间演化加到类里       
    def psit(self,t, hbar=1):
        #基态与第一激发态的叠加态波函数，随时演化
        psi0 = self.eigV[:, 0]
        psi1 = self.eigV[:, 1]
        E0 = self.eigE[0]
        E1 = self.eigE[1]
        return 1/np.sqrt(2) * (psi0 * np.exp(-1j * E0 * t/hbar)
                        +  psi1 * np.exp(-1j * E1 * t/hbar))

