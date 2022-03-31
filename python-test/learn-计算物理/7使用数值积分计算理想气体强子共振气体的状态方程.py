########################################################
####################### 学习内容 #######################
#什么是强子
#高能核碰撞末态强子的统计分布
#从粒子数据表 pdg data table 中读取各种强子的量子数
#计算所有强子对强子共振气体状态方程的贡献
#http://lgpang.gitee.io/mlcphysics/htmls/hrg_eos_with_integration.html
########################################################

#In[]
import numpy as np
import matplotlib.pyplot as plt

# quad 函数用来做数值积分
from scipy.integrate import quad
#公式环境

import seaborn as sns

#befor
sns.set_context("talk")




pion0 = {'mass': 0.135,    # unit: [GeV]
        '2*spin+1': 1,     # spin degeneracy
        'eta': -1,         # - for boson
        'baryon_num': 0,
        'strange_num': 0,
        'charge_num': 0}
def dist_f(k, T, hadron):
    '''the distribution function of hadron 
    :k: float or np.array(), momentum in units [GeV]
    :T: float, temperature, [GeV]
    :hadron: dict with {'mass', '2*spin+1', 'eta',
                        'baryon_num', 'strange_num', 'charge_num'}
             where eta: +1 for fermion, -1 for boson
             
    :return: (2s + 1) / (np.exp(np.sqrt(k**2 + m**2)/T) + eta)
    '''
    spin_dof = hadron['2*spin+1']
    m = hadron['mass']
    eta = hadron['eta']
    return  spin_dof / (np.exp(np.sqrt(k**2 + m**2)/T) + eta)
def density_n(T, hadron):
    '''calc density for given temperatures
    :T: float, temperature, [GeV]
    :hadron: dict with {'mass', '2*spin+1', 'eta',
                        'baryon_num', 'strange_num', 'charge_num'}
             where eta: +1 for fermion, -1 for boson
    :return: hadron density at T '''
    # 此处 intg_n 是 inline function
    intg_n = lambda k: k**2 * dist_f(k, T, hadron) / (2 * np.pi**2)
    
    kmax = 50 * T
    # 不要直接使用 quad(f, 0, 50*T), 给 50*T 命名为 kmax，程序可读性更好
    ndensity = quad(intg_n, 0, kmax)[0]
    
    return ndensity
# 高能核碰撞产生大量强子中，pion 介子占 80% 以上，可以从 pion/proton ratio 简单看出
proton = {'mass': 0.938,    # unit: [GeV]
        '2*spin+1': 2,
        'eta': +1,
        'baryon_num': 1,
        'strange_num': 0,
        'charge_num': 1}

T = 0.155
npi0 = density_n(T, pion0)
nproton = density_n(T, proton)

print("pion to proton ratio=", npi0 / nproton)
#pion to proton ratio= 16.10186328398944
def pressure_p(T, hadron):
    '''HRG presure for given temperatures
    :T: float or np.array(), temperature, [GeV]
    :hadron: dict with {'mass', '2*spin+1', 'eta',
                        'baryon_num', 'strange_num', 'charge_num'}
             where eta: +1 for fermion, -1 for boson
    :return: hadron presure at T  in unit [GeV]^4 '''
    spin_dof = hadron['2*spin+1']
    m = hadron['mass']
    eta = hadron['eta']
    intg_p = lambda k:  k**2 * np.log(1 + eta * np.exp(-(np.sqrt(k**2 + m**2))/T))    
    coef_p = eta * T * spin_dof / (2 * np.pi**2)

    kmax = 50 * T
    pressure = coef_p * quad(intg_p, 0, kmax)[0] 
    return pressure
def energy_density_e(T, hadron):
    '''HRG presure for given temperatures
    :T: float or np.array(), temperature, [GeV]
    :hadron: dict with {'mass', '2*spin+1', 'eta',
                        'baryon_num', 'strange_num', 'charge_num'}
             where eta: +1 for fermion, -1 for boson 
    :return: hadron energy density at T in unit [GeV]^4'''
    m = hadron['mass']

    intg_e = lambda k: k**2 * np.sqrt(k**2 + m**2) * dist_f(k, T, hadron) / (2 * np.pi**2)
    kmax = 50 * T
    edensity = quad(intg_e, 0, kmax)[0] 
    return edensity
def eos(T, mu, hadron):
    '''calc the pressure vs energy density
    :T: float, temperature, [GeV]
    :mu: (mu_B, mu_S, mu_Q)
    :hadron: dict with {'mass', '2*spin+1', 'eta',
                        'baryon_num', 'strange_num', 'charge_num'}
             where eta: +1 for fermion, -1 for boson
    return: pressure, energy density in unit [GeV]^4，particle density'''
    pressure = pressure_p(T, hadron)
    edensity = energy_density_e(T, hadron)
    ndensity = density_n(T, hadron)
    
    return pressure, edensity, ndensity

#In[]
######### 测试无质量理想气体的状态方程 P = e/3##################

fake_hadron = {'mass': 0,  # unit: [GeV]
        '2*spin+1': 1,     # spin degeneracy
        'eta': -1,         # - for boson
        'baryon_num':  0,
        'strange_num': 0,
        'charge_num': 0}

Tarr = np.linspace(0.01, 0.2, 100)

ed = [energy_density_e(T, fake_hadron) for T in Tarr]

pr = [pressure_p(T, fake_hadron) for T in Tarr]

np.isclose(np.array(pr), np.array(ed)/3).all()
True
def plot_pr_vs_ed(ed, pr, label="EoS for massless ideal gas"):
    with plt.style.context(["science", "notebook", "no-latex"]):
        plt.plot(ed, pr, label=label)
        plt.xlabel(r"energy density ${\rm [GeV]^{-4}}$")
        plt.ylabel(r"pressure ${\rm [GeV]^{-4}}$")
        plt.legend(loc='best')

plot_pr_vs_ed(ed, pr)
#In[]
#######################$\pi$ 介子气体##########################
#$\pi^0$ 质量约为 0.135 GeV，自旋为 0，其压强与能量密度的关系是否满足 $P = {\varepsilon \over 3}$?

pion_ed = [energy_density_e(T, pion0) for T in Tarr]

pion_pr = [pressure_p(T, pion0) for T in Tarr]

np.isclose(np.array(pion_pr), np.array(pion_ed)/3).all()
False
with plt.style.context(["science", "notebook", "no-latex"]):
    plot_pr_vs_ed(pion_ed, pion_pr, label="pion0 gas")
    plt.plot(ed, np.array(ed)/3.0, 'r--', label="massless ideal gas")
    plt.legend(loc='best')

cs2_pion = np.gradient(pion_pr, pion_ed)

with plt.style.context(["science", "notebook", "no-latex"]):
    plt.plot(Tarr, np.ones_like(Tarr)/3, label="mass less ideal gas")
    plt.plot(Tarr, cs2_pion, label="pion0 gas")
    plt.legend(loc='best')
    plt.xlabel('T [GeV]')
    plt.ylabel(r'$c_s^2$')
#In[]
#######################Pion + Proton 气体#################
#如果系统不是单一的 pion 介子气体，而是介子与质子的混合气体呢？

# HRG with pion and proton only

def simple_hrg_eos():
    T = np.linspace(0.05, 0.350, 100)
    mu = 0  
    pressure = []
    edensity = []
    cs2 = []
    
    for Ti in T:
        pr_pion, ed_pion, n_pion = eos(Ti, mu, pion0)
        pr_proton, ed_proton, n_proton = eos(Ti, mu, proton)
        pr_ = pr_pion + pr_proton
        ed_ = ed_pion + ed_proton
        pressure.append(pr_)
        edensity.append(ed_)
    
    cs2 = np.gradient(pressure, edensity)
    
    return T, pressure, edensity, cs2

T, pre, ed, cs2 = simple_hrg_eos()
plt.plot(T, pre, label="p(T)")
plt.plot(T, ed, label="ed(T)")
plt.legend(loc='best')
plt.xlabel('T')
#Text(0.5, 0, 'T')

plt.plot(ed, pre, label="p(ed)")
plt.legend(loc='best')
plt.xlabel('ed')
#Text(0.5, 0, 'ed')

plt.plot(T, cs2, label="pion+proton")
plt.plot(Tarr, cs2_pion, label="pion0 gas")
plt.xlabel("Temperature [GeV]")
plt.ylabel(r"$c_s^2$")
plt.legend(loc='best')
#

#In[]数据处理
###################HRG EoS using PDG05 table###############
#PDG05 table 使用 05 年的 PDG 数据，数字化后保存了介子与重子（注意没有反重子）的量子数以及衰变分支信息。

pdg_ = []
name_ = []
mass_ = []
decay_width_ = []       # decay width
spin_degeneracy_ = []    # 2*s + 1
isbaryon_ = []
strange_num_ = []
charge_num_ = []
with open("data/pdg05.dat", "r") as pdg:
    lines = pdg.readlines()
    row = 0
    while row < len(lines):
        # 按空格将不同的数据分开
        particle = lines[row].split()
        # 最后一列存储了衰变通道个数
        decay_channels = int(particle[-1])
        row += decay_channels
        
        #print(particle[1], particle[10])
        pdg_.append(int(particle[0]))
        name_.append(particle[1])
        mass_.append(float(particle[2]))
        decay_width_.append(float(particle[3]))
        spin_degeneracy_.append(int(particle[4]))
        isbaryon_.append(int(particle[5]))
        strange_num_.append(int(particle[6]))
        charge_num_.append(int(particle[10]))
        
        row += 1
import pandas as pd

df = pd.DataFrame({"pdg":pdg_, 
                   "name":name_, 
                   "mass":mass_,
                   "decay_width":decay_width_,
                   "2*spin+1":spin_degeneracy_,
                   "isbaryon":isbaryon_,
                   "strange_num":strange_num_,
                   "charge_num":charge_num_})
df.head(n=10)
'''
pdg	name	mass	decay_width	2*spin+1	isbaryon	strange_num	charge_num
0	211	Pion(+)	0.13957	0.0000	1	0	0	1
1	111	Pion(0)	0.13498	0.0000	1	0	0	0
2	-211	Pion(-)	0.13957	0.0000	1	0	0	-1
3	321	Kaon(+)	0.49368	0.0000	1	0	1	1
4	-321	Kaon(-)	0.49368	0.0000	1	0	-1	-1
5	311	Kaon(0)	0.49765	0.0000	1	0	1	0
6	-311	AntiKaon(0)	0.49765	0.0000	1	0	-1	0
7	221	eta	0.54775	0.0000	1	0	0	0
8	213	rho(+)	0.77580	0.1503	3	0	0	1
9	113	rho(0)	0.77580	0.1503	3	0	0	0
# 给 pandas 的 DataFrame 数据多添加一列，eta
'''
# for fermions (baryons)
df.loc[df["isbaryon"]==1, "eta"] = +1.0

# for bosons (mesons)
df.loc[df["isbaryon"]==0, "eta"] = -1.0
# pdg05.dat 中无反重子，手动添加
anti_baryon = df[df['isbaryon']==1].copy()
anti_baryon.loc[:, "pdg"] = - anti_baryon["pdg"]
anti_baryon.loc[:, "name"] = "anti" + anti_baryon["name"]
anti_baryon.loc[:, "charge_num"] = -anti_baryon["charge_num"]
anti_baryon.head()
'''
pdg	name	mass	decay_width	2*spin+1	isbaryon	strange_num	charge_num	eta
16	-2212	antip	0.93827	0.0	2	1	0	-1	1.0
17	-2112	antin	0.93957	0.0	2	1	0	0	1.0
24	-3122	antiLambda	1.11568	0.0	2	1	-1	0	1.0
26	-3222	antiSigma(+)	1.18937	0.0	2	1	-1	-1	1.0
27	-3212	antiSigma(0)	1.19264	0.0	2	1	-1	0	1.0
'''

df = df.append(anti_baryon, ignore_index=True)
df.tail()
'''
pdg	name	mass	decay_width	2*spin+1	isbaryon	strange_num	charge_num	eta
314	-12226	antiDelta1930(++)	1.960	0.360	6	1	0	-2	1.0
315	-12126	antiDelta1930(+)	1.960	0.360	6	1	0	-1	1.0
316	-11216	antiDelta1930(0)	1.960	0.360	6	1	0	0	1.0
317	-11116	antiDelta1930(-)	1.960	0.360	6	1	0	1	1.0
318	-13334	antiOmega2250	2.252	0.055	4	1	-3	1	1.0
'''
df.count()['pdg']
#319
#使用 PDG05 table，计算理想强子共振气体的状态方程
from tqdm import tqdm

# HRG with pion and proton only

def hrg_eos():
    T = np.linspace(0.1, 0.2, 20)
    mu = 0  
    pressure = []
    edensity = []
    ndensity = []
    cs2 = []
    
    for Ti in tqdm(T):
        pr = 0
        ed = 0
        nd = 0
        for i in range(len(df)):
            hadron = df.iloc[i, :]
            pr_, ed_, nd_ = eos(Ti, mu, hadron)
            pr += pr_
            ed += ed_
            nd += nd_
            
        pressure.append(pr)
        edensity.append(ed)
        ndensity.append(nd)
    
    cs2 = np.gradient(pressure, edensity)
    
    return T, np.array(pressure), np.array(edensity), np.array(ndensity), cs2
T, Pr, Ed, Nh, Cs2 = hrg_eos()
#100%|██████████| 20/20 [00:12<00:00,  1.56it/s]
plt.plot(T, Cs2)
plt.xlabel("T [GeV]")
plt.ylabel(r"$c_s^2$")
#Text(0, 0.5, '$c_s^2$')

plt.plot(Ed, Pr)
plt.xlabel(r"$\varepsilon\ [GeV]^4$")
plt.ylabel(r"$P\ [GeV]^4$")
#Text(0, 0.5, '$P\\ [GeV]^4$')

plt.plot(T, Ed/T**4)
plt.xlabel("T [GeV]")
plt.ylabel(r"$\varepsilon / T^4$")
#Text(0, 0.5, '$\\varepsilon / T^4$')

plt.plot(T, 3 * Pr/T**4)
plt.xlabel("T [GeV]")
plt.ylabel(r"$3 P / T^4$")
#Text(0, 0.5, '$3 P / T^4$')

to_fm_3 = (1/0.19732)**3
plt.plot(T, np.array(Nh) * to_fm_3)
plt.ylim(0, 1.4)
plt.xlabel("T [GeV]")
plt.ylabel(r"Hadron density $fm^{-3}$")
#Text(0, 0.5, 'Hadron density $fm^{-3}$')

# %%
