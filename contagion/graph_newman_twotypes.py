# -*- coding: utf-8 -*-
"""
"""

from numsolve_newman_twotype import *
import matplotlib.pyplot as plt
import numpy as np

#%%Helper functions and parameters
def labelSubplot(ax,title,xlabel,ylabel):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
CL_log10 = [1E-09,1E-08,1E-07,1E-06,1E-05,1E-04,1E-03,1E-02,1E-01,.99999999]
CL_percentile = np.arange(0,1.0001,0.01)
CL_logGraded = [.99999999999]

#%% Grid creation. Input variables to iterate over.
n_grid = np.arange(0,31)
Ψ_grid = np.arange(0,1.00001,.001)
V_grid = np.arange(0,1.00001,.001)


#%% PLot a contour graph showing critical threshold given nH,nL
#   Trivial. Just a warmup really.

TcTc = [[calcTc(nH, nL) for nH in n_grid] for nL in n_grid]

fig,ax = plt.subplots(figsize=(5,5),constrained_layout=True)
CS = ax.contour(n_grid,n_grid,TcTc,CL_percentile,)
ax.clabel(CS,CS.levels,fmt='{:.2}'.format,inline=False,fontsize=8)
labelSubplot(ax, 'newman,twotype,Tc', r'$n_H$', r'$n_L$')
plt.savefig('graph_newman_twotype_Tc.svg')



#%% Graph Two Types of people, Plot n(V) for each type

#parameters for choice of each type in absence of contagion
fig,ax = plt.subplots(figsize=(8,5),constrained_layout=True)
plt.plot(Ψ_grid,[findMyopicBest_n(1-Ψ,u_nlogtaper_H) for Ψ in Ψ_grid])
plt.plot(Ψ_grid,[findMyopicBest_n(1-Ψ,u_nlogtaper_L) for Ψ in Ψ_grid])
plt.plot(Ψ_grid,[1/Ψ for Ψ in Ψ_grid])
labelSubplot(ax, r'newman,two types, $n_H(V)$,$n_L(V)$, and threshold $n > \frac{1}{\Psi}$', r'$\Psi = 1-V$', r'$n^*_i(V)$')
ax.set_ylim([0,30])
ax.set_xlim([0,1])
plt.savefig('graph_newman_twotype_n(V).svg')


#%% Contour Plot of V based on n_H and n_L
#   Based on a specific values of T (unless I figure out another way of visualizing)

fig, ((ax0,ax1,ax2),(ax3,ax4,ax5)) = plt.subplots(2,3, 
                      figsize=(15,10),constrained_layout=True)

def makesubplot_contour_V(ax,T,nH_grid,nL_grid,AH,AL):
    VV = VV = [[approxV(T,nH,nL,AH=AH,AL=AL) for nH in nH_grid] for nL in nL_grid]
    CS = ax.contour(nH_grid,nL_grid,VV,CL_percentile,)
    ax.clabel(CS,CS.levels,fmt='{:.2}'.format,inline=False,fontsize=8)
    labelSubplot(ax, '$V(n_H,n_L)$ contour for  $T=$'+str(T), r'$n_H$', r'$n_L$')
    
makesubplot_contour_V(ax0, 0.05, n_grid, n_grid, 0.5, 0.5)
makesubplot_contour_V(ax1, 0.1, n_grid, n_grid, 0.5, 0.5)
makesubplot_contour_V(ax2, 0.15, n_grid, n_grid, 0.5, 0.5)
makesubplot_contour_V(ax3, 0.2, n_grid, n_grid, 0.5, 0.5)
makesubplot_contour_V(ax4, 0.3, n_grid, n_grid, 0.5, 0.5)
makesubplot_contour_V(ax5, 0.5, n_grid, n_grid, 0.5, 0.5)

#plot the pairs of (n_H*,n_L*) as we trace through the value of V.
nHstars = [findMyopicBest_n(1-Ψ,u_nlogtaper_H) for Ψ in Ψ_grid]
nLstars = [findMyopicBest_n(1-Ψ,u_nlogtaper_L) for Ψ in Ψ_grid]
for ax in [ax0,ax1,ax2,ax3,ax4,ax5]: ax.scatter(nHstars,nLstars)
for ax in [ax0,ax1,ax2,ax3,ax4,ax5]: ax.scatter(nHstars[0],nLstars[0])

fig.suptitle('newman,twotype, $V(n_H,n_L)$ contours for different values of $T$')
plt.savefig('graph_newman_twotype_Vcontours.png')


#%% EVERYTHING BELOW THIS LINE IS OLD AND NEEDS TO BE DELETED LATER.






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


#%% Make the graphs

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

