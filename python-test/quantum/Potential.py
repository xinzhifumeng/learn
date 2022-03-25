import numpy as np

#尝试对知乎中出现的势阱进行封装

class Potential:
    #def __init__(self, x, 
    #             R0=6.2, surface_thickness=0.5,
    #             xmin=-5, xmax=5, ninterval=1000):
    #    self.x = np.linspace(xmin, xmax, ninterval)    
        
    #############定义一个谐振子势###############
    # 定义谐振子势
    def harmonic_potential(x, k=100):
        print(0.5 * k * x**2)
        return 0.5 * k * x**2
    ###########################################
    ######执行可视化后需要执行
    #plt.show()

    ###### 创建谐振子势下的薛定谔方程
    #schro_harmonic = Schrodinger(harmonic_potential)

    ######对谐振子势能可视化
    #schro_harmonic.plot_potential()

    #schro_harmonic.check_eigen(n=1)
    ######再用上面这条命令检查一下薛定谔方程的解是否准确，具体来说就是本征方程 [公式] 是否满足。

    ######还可以看看粒子在谐振子势阱中的分布概率密度，
    ###### 这里随便选了一个能级 n = 9

    #schro_harmonic.plot_density(n=9)
    ######可以利用该命令画不同能级下的概率密度分布


    ############Woods Saxon 势能############
    #####在核物理领域，原子核中一大团核子所产生的势能接近于 Woods Saxon 函数形式。这里看看Woods Saxon 势阱中一个核子的能级分布。势阱函数形式为，
    def woods_saxon_potential(x, R0=6.2, surface_thickness=0.5):
        sigma = surface_thickness
        return  -1 / (1 + np.exp((np.abs(x) - R0)/sigma))

    ########################################

    ###################双势阱###############
    def double_well(x, xmax=5, N=100):
        w = xmax / N
        a = 3 * w
        return -100 * (np.heaviside(x + w - a, 0.5) - np.heaviside(x - w - a, 0.5)
                    +np.heaviside(x + w + a, 0.5) - np.heaviside(x - w + a, 0.5))

    #dw = lambda x: double_well(x, xmax=5, N=1000)
    #dw_shro = Schrodinger(double_well)
    ######双势阱中前几个能级下粒子的概率密度分布，

    #dw_shro.plot_density(n=0)
    #dw_shro.plot_density(n=1)
    #dw_shro.plot_density(n=2)
    #dw_shro.plot_density(n=4)
    
    ########################################