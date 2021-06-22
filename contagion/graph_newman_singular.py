# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:09:53 2021

@author: rober
"""

from numsolve_newman_singular import *
import matplotlib.pyplot as plt
import numpy as np

#%% Set up field of variables
T_grid = np.arange(0,1,0.01)
Psi_grid = T_grid
n_grid = np.arange(0,31)
TT,nn = np.meshgrid(T_grid,n_grid)

#%% Calc third dimension
# Could massively speed up by reusing Vs or Us, but :shrug:
VV = [[approximateV(n, T) for T in T_grid] for n in n_grid]
UU = [[approximateU(n, T) for T in T_grid] for n in n_grid]
RR = [[calcRviaV(n, T) for T in T_grid] for n in n_grid]
R0R0 = [[T*(n-1) for T in T_grid] for n in n_grid]
PsiPsi = [[1-approximateV(n, T) for T in T_grid] for n in n_grid]
pnpn = [[1-(1-Psi)**n for Psi in Psi_grid] for n in n_grid]


#%% Make the six graphs showing various forms of prevalence.

#formatting for contour of U(n,T)
def fmtcntrU(x):
    return '{:.0E}'.format(x)


fig, ((ax0,ax1,ax4),(ax2,ax3,ax5)) = plt.subplots(2,3, 
                      figsize=(15,10),constrained_layout=True)

ax0.set_title("V(n,T)")
CS = ax0.contour(T_grid,n_grid,VV,
                 [0.1*step-0.0001 for step in range(11)],colors='k')
ax0.clabel(CS, CS.levels, inline=False, fontsize=10)
ax0.set_xlabel("T")
ax0.set_ylabel("n")
ax0.grid()

ax1.set_title(r"$R_\infty(n,T)$")
CS = ax1.contour(T_grid,n_grid,pnpn,
                 [0,0.1,0.5,0.9,0.99,0.999,.9999,.99999],colors='k')
ax1.clabel(CS, CS.levels, inline=False, fontsize=10,fmt='{:.5}'.format)
ax1.set_xlabel("T")
ax1.set_ylabel("n")
ax1.grid()

ax2.set_title('U(n,T)')
CS = ax2.contour(T_grid,n_grid,UU,
                [1E-09,1E-08,1E-07,1E-06,1E-05,1E-04,1E-03,1E-02,1E-01,.99999999]
                ,colors='k')
ax2.clabel(CS, CS.levels, inline=False, fmt=fmtcntrU, fontsize=10)
ax2.set_xlabel("T")
ax2.set_ylabel("n")
ax2.grid()

ax3.set_title(r"$R_0(n,T) = (n-1) T$")
CS = ax3.contour(T_grid,n_grid,R0R0,
                 [0,1,2,4,8,16],colors='k')
ax3.clabel(CS, CS.levels, inline=True, fontsize=10)
ax3.set_xlabel(r"$T$")
ax3.set_ylabel("n")
zc = CS.collections[1]
plt.setp(zc, linewidth=6)
ax3.grid()


ax4.set_title(r"$\Psi=1-V$")
CS = ax4.contour(T_grid,n_grid,PsiPsi,10,colors='k')
ax4.clabel(CS, CS.levels, inline=True, fontsize=10,fmt='{:.1}'.format)
ax4.set_xlabel(r"$T$")
ax4.set_ylabel("n")
ax4.grid()


ax5.set_title(r"$p(n;\Psi)$")
CS = ax5.contour(Psi_grid,n_grid,pnpn,
                 [0,0.1,0.367879441171,0.5,0.9,0.99,0.999,.9999,.99999],colors='k')
ax5.clabel(CS, CS.levels, inline=True, fontsize=10,fmt='{:.5}'.format)
ax5.set_xlabel(r"$\Psi=1-V$")
ax5.set_ylabel("n")
plt.setp(CS.collections[2], linewidth=6)
ax5.grid()


fig.suptitle('Newman, Singular Degree Distribution, equilibrium whatsits')
plt.savefig('graph_newman_singular.svg')

#%% For each point in the grid,
#       Find V(n,T)
#       Find the n* that maximizes utility, taking V,T for granted.
#       If matches up with n, then add point to graph
#   Also, for each T, find the n that maximizes u(n)-p(n;V(n,T))

def plotEquilAndOptim(utilityfunc,filename,title):
    # loop to find equilibriums
    equilibriums = []
    for T in T_grid:
        for n in n_grid:
            V = approximateV(n,T)
            BRn = findMyopicBest_n(V,utilityfunc)
            #print(n,BRn)
            if n in BRn:
                equilibriums.append([n,T])
                
    n_equilibria = [equi[0] for equi in equilibriums]   
    T_equilibria = [equi[1] for equi in equilibriums]   
    
    # Plot equilibrium points and societal optimums 
    plt.scatter(T_equilibria,n_equilibria,marker='x',c='orange')
    plt.scatter(T_grid,[SPPu(T,utilityfunc)[0] for T in T_grid], marker='.',c='blue')
    
    
    plt.grid()
    plt.ylim(0,30)
    plt.title(title)
    plt.xlabel('T')
    plt.ylabel('n')
    plt.savefig(filename)
    
    
plotEquilAndOptim(neginverse_u, 'graph_newman_singular_equilibria_neginverse.png',r"newman,singular,equilibria(x) and SPP(.),$U=2-\frac{1}{n}-p(n)$")
#plotEquilAndOptim(big_neginverse_u, 'graph_newman_singular_equilibria_bigneginverse.png',r"newman,singular,equilibria(x) and SPP(.),$U=2-\frac{5}{n}-p(n)$")
#plotEquilAndOptim(u_kremertest, 'graph_newman_singular_equilibria_kremertest.png',r"newman,singular,equilibria(x) and SPP(.),$U=\frac{1}{2}n-\frac{1}{40}n^2-p(n)$")
#plotEquilAndOptim(u_neginv_withtaper, 'graph_newman_singular_equilibria_neginvtaper.png',r"newman,singular,equilibria(x) and SPP(.),$U=\frac{-5}{n}-\frac{1}{1000}n^2-p(n)$")
#plotEquilAndOptim(u_smol_neginv_withtaper, 'graph_newman_singular_equilibria_neginvtaper(small).png',r"newman,singular,equilibria(x) and SPP(.),$U=\frac{-1}{n}-\frac{1}{5000}n^2-p(n)$")


#%% Plot V(n(V))
#   For several (or just one at the start) values of T:
#       Iterate through a grid of Vs:
#           Plot V(n^*(V))

def plot_VnV_iteration(utilfunc,filename,title):
    V_grid = np.arange(0,1.000001,0.001)
    fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
    ax.plot(V_grid,V_grid,c='black',linestyle='dotted')
    for T in [0.05,0.1,0.15,0.2,0.4,0.6,0.8]:
        VnV_grid = []
        for V in V_grid:
            best_n = findMyopicBest_n(V,utilfunc)
            #if len(best_n) > 1:
            #    print("Multiple n*(V) found for V="+str(V)+",T="+str(T))
            VnV_grid.append(approximateV(best_n[0],T)) 
        ax.scatter(V_grid,VnV_grid,label='T='+str(T),marker='.')
    ax.set_ylim([0,1])
    ax.set_xlim([0,1])
    ax.grid()
    ax.set_title(title)
    ax.set_xlabel(r'$V$')
    ax.set_ylabel(r'$V(n^*(V);T)$')
    ax.legend()
    plt.savefig(filename)
    
plot_VnV_iteration(neginverse_u, 'graph_newman_singular_VnV_neginverse.png',r"newman,singular,V(n(V)), $U=2-\frac{1}{n}-p(n)$")
plot_VnV_iteration(big_neginverse_u, 'graph_newman_singular_VnV_bigneginverse.png',r"newman,singular,V(n(V)), $U=2-\frac{5}{n}-p(n)$")
plot_VnV_iteration(u_kremertest, 'graph_newman_singular_VnV_kremertest.png',r"newman,singular,V(n(V)), $U=\frac{1}{2}n-\frac{1}{40}n^2-p(n)$")
plot_VnV_iteration(u_neginv_withtaper, 'graph_newman_singular_VnV_neginvtaper.png',r"newman,singular,V(n(V)), $U=\frac{-5}{n}-\frac{1}{1000}n^2-p(n)$")
plot_VnV_iteration(u_smol_neginv_withtaper, 'graph_newman_singular_VnV_neginvtaper(small).png',r"newman,singular,V(n(V)), $U=\frac{-1}{n}-\frac{1}{5000}n^2-p(n)$")




#%% Plot p(n;Psi)-p(n+1;Psi) 
#   roc in marginal infection risk as connection danger increases
#   This section is kinda janky TODO: clean it up

def riskchange(n,Psi):
    return (1-(1-Psi)**n)-(1-(1-Psi)**(n-1))

n_grid2 = np.arange(0,31)
margrisk = [[riskchange(n,Psi) for Psi in Psi_grid] for n in n_grid2]

fig, ax = plt.subplots(figsize=(15,10))
plt.grid()
ax.set_title('Newman, Singular Degree Distribution, p(n)-p(n-1)')
CS = ax.contourf(Psi_grid,n_grid2,margrisk,
                np.arange(-.1,.1,.001))
ax.clabel(CS,CS.levels,inline=True,fontsize=10,fmt='{:.5}'.format)
plt.savefig('graph_newman_singular_pdiffexperiment1.png')

#%% Plot d/d\Psi p(n;Psi)-p(n+1;Psi) 
#   roc in marginal infection risk as connection danger increases
#   This section is kinda janky TODO: clean it up

def ddPsi_riskchange(n,Psi):
    return (1-n*Psi)*(1-Psi)**(n-2)

n_grid2 = np.arange(1,11)
Psi_grid2 = np.arange(0,1.0001,0.001)
changemargrisk = [[ddPsi_riskchange(n,Psi) for Psi in Psi_grid2] for n in n_grid2]

fig, ax = plt.subplots(figsize=(15,10))
#plt.grid()
ax.set_title(r'Newman, Singular Degree Distribution, $\frac{d}{d\Psi} p(n)-p(n-1)$')
CS = ax.contour(Psi_grid2,n_grid2,changemargrisk,60,colors='k')

plt.plot([1/n for n in n_grid2],n_grid2)

#ax.clabel(CS,CS.levels,inline=True,fontsize=10,fmt='{:.5}'.format)
plt.savefig('graph_newman_singular_pdiffexperiment2.svg')



#%% 

