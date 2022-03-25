from matplotlib.animation import FuncAnimation
from Schrodinger import *
from Potential import *
import numpy as np
import matplotlib.pyplot as plt
#动画代码
class UpdateDist:
    def __init__(self, ax, x):
        self.success = 0
        self.line, = ax.plot([], [], 'k-')
        
        self.x = x
        self.ax = ax
        # Set up plot parameters
        self.ax.set_xlim(-0.6, 0.6)
        self.ax.set_ylim(-0.02, 0.1)
        self.ax.grid(True)

    def __call__(self, i):
        test = Schrodinger(Potential.double_well) 
        time = i * 0.01
        psi = test.psit(t = time)
        density = np.real(np.conjugate(psi) * psi)     
        self.line.set_data(self.x, density)
        return self.line,

# 画缩放了的双势阱
test = Schrodinger(Potential.double_well) 
potential = Potential.double_well(test.x) * 1.0E-4
fig, ax = plt.subplots()
ax.plot(test.x, potential, ':')
ax.set_xlabel(r'$x$')
ud = UpdateDist(ax, test.x)
anim = FuncAnimation(fig, ud, frames=1000, interval=80, blit=True)
#anim.save('double_well_evolution.gif')

anim.save('double.gif', writer='pillow')
#plt.show()