# -*- coding: utf-8 -*-
"""
"""

import numsolve_newman_twotype as nnt
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

TcTc = [[nnt.calcTc(nH, nL) for nH in n_grid] for nL in n_grid]

fig,ax = plt.subplots(figsize=(5,5),constrained_layout=True)
CS = ax.contour(n_grid,n_grid,TcTc,CL_percentile,)
ax.clabel(CS,CS.levels,fmt='{:.2}'.format,inline=False,fontsize=8)
labelSubplot(ax, 'newman,twotype,Tc', r'$n_H$', r'$n_L$')
plt.savefig('graph_newman_twotype_Tc.svg')



#%% Graph Two Types of people, Plot n(V) for each type

#parameters for choice of each type in absence of contagion
fig,ax = plt.subplots(figsize=(8,5),constrained_layout=True)
plt.plot(Ψ_grid,[nnt.findMyopicBest_n(1-Ψ,nnt.u_nlogtaper_H) for Ψ in Ψ_grid])
plt.plot(Ψ_grid,[nnt.findMyopicBest_n(1-Ψ,nnt.u_nlogtaper_L) for Ψ in Ψ_grid])
plt.plot(Ψ_grid,[1/Ψ for Ψ in Ψ_grid])
labelSubplot(ax, r'newman,two types, $n_H(V)$,$n_L(V)$, and threshold $n > \frac{1}{\Psi}$', r'$\Psi = 1-V$', r'$n^*_i(V)$')
ax.set_ylim([0,30])
ax.set_xlim([0,1])
plt.savefig('graph_newman_twotype_n(V).svg')


#%% Contour Plot of V based on n_H and n_L
#   Based on a specific values of T (unless I figure out another way of visualizing)

fig, ((ax0,ax1,ax2),(ax3,ax4,ax5)) = plt.subplots(2,3, 
                      figsize=(15,10),constrained_layout=True)

def makesubplot_contour_V(ax,T,nH_grid,nL_grid,AH=0.5,AL=0.5):
    VV = VV = [[nnt.approxV(T,nH,nL,AH=AH,AL=AL) for nH in nH_grid] for nL in nL_grid]
    CS = ax.contour(nH_grid,nL_grid,VV,CL_percentile,)
    ax.clabel(CS,CS.levels,fmt='{:.2}'.format,inline=False,fontsize=8,colors='k')
    labelSubplot(ax, '$V(n_H,n_L)$ contour for  $T=$'+str(T), r'$n_H$', r'$n_L$')
    ax.grid()
    
makesubplot_contour_V(ax0, 0.05, n_grid, n_grid,)
makesubplot_contour_V(ax1, 0.1, n_grid, n_grid,)
makesubplot_contour_V(ax2, 0.15, n_grid, n_grid,)
makesubplot_contour_V(ax3, 0.2, n_grid, n_grid,)
makesubplot_contour_V(ax4, 0.3, n_grid, n_grid,)
makesubplot_contour_V(ax5, 0.5, n_grid, n_grid,)

#plot the pairs of (n_H*,n_L*) as we trace through the value of V.
nHstars = [nnt.findMyopicBest_n(1-Ψ,nnt.u_nlogtaper_H) for Ψ in Ψ_grid]
nLstars = [nnt.findMyopicBest_n(1-Ψ,nnt.u_nlogtaper_L) for Ψ in Ψ_grid]
for ax in [ax0,ax1,ax2,ax3,ax4,ax5]: ax.scatter(nHstars,nLstars)
for ax in [ax0,ax1,ax2,ax3,ax4,ax5]: ax.scatter(nHstars[0],nLstars[0])


fig.suptitle('newman,twotype, $V(n_H,n_L)$ contours for different values of $T$')
plt.savefig('graph_newman_twotype_Vcontours_nlogtaper.png')
#fig.suptitle('newman,twotype, $V(n_H,n_L)$ contours for different values of $T$')
#plt.savefig('graph_newman_twotype_Vcontours.png')
#fig.suptitle('newman,twotype, $V(n_H,n_L)$ contours for different values of $T$, but $A_H=0.3$ and $A_L=0.7$')
#plt.savefig('graph_newman_twotype_Vcontours_populationtwist.png')


#%% Plot V(n(V)) to visualize equilibrium.
# I'm going to experiment with using Ψ=1-V this time.

def plot_ΨnΨ_iteration(utilfuncH,utilfuncL,speciallabel):
    fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
    ax.plot(Ψ_grid,Ψ_grid,c='black',linestyle='dotted')
    for T in [0.05,0.1,0.15,0.2,0.4,0.6,0.8]:
        ax.scatter(Ψ_grid,[1-nnt.iterateV(1-Ψ,T,utilfuncH,utilfuncL,AH=0.5,AL=0.5) for Ψ in Ψ_grid],
                   label='T='+str(T),marker='.')
    ax.set_ylim([0,1])
    ax.set_xlim([0,1])
    ax.grid()
    ax.legend()
    labelSubplot(ax, 'newman,twotype,Ψ(n(Ψ)),'+speciallabel, '$\Psi$', '$\Psi(n_H^*,n_L^*)$')
    plt.savefig('newman_twotype_PsinPsi_'+speciallabel+'.png')

plot_ΨnΨ_iteration(nnt.u_nlogtaper_H,nnt.u_nlogtaper_L,'nlogtaper-φH=25-φL=10')


#%% Plot n(V(n)) to visualize equilibrium.
# I'm going to experiment with using Ψ=1-V this time.

def plot_nVn_iteration(utilfuncH,utilfuncL,speciallabel,T):
    #Two outputs. One for mapping nVn, the other for highlighting fixed points.
    maxntoshow = 30
    mappedpoints = []
    equilibriapoints = []
    for nH in range(maxntoshow+1):
        for nL in range(maxntoshow+1):
            nVn = nnt.iterate_npair(nH, nL, T, utilfuncH, utilfuncL)
            mappedpoints.append(nVn)
            if nVn == (nH,nL):
                equilibriapoints.append(nVn)
                
    fig,ax = plt.subplots(figsize=(5,5),constrained_layout=True)
    ax.scatter(*zip(*mappedpoints))
    if equilibriapoints != []:
        ax.scatter(*zip(*equilibriapoints))
        
    ax.set_ylim([0,30])
    ax.set_xlim([0,30])
    ax.grid()
    labelSubplot(ax, 'newman,twotype,nVn,'+speciallabel, '$n_H$', '$n_L$')
    plt.savefig('newman_twotype_nVn_'+speciallabel+'.png')

plot_nVn_iteration(nnt.u_nlogtaper_H,nnt.u_nlogtaper_L,'nlogtaper-φH=25-φL=10-T=.2',0.2)
plot_nVn_iteration(nnt.u_nlogtaper_H,nnt.u_nlogtaper_L,'nlogtaper-φH=25-φL=10-T=.1',0.1)
plot_nVn_iteration(nnt.u_nlogtaper_H,nnt.u_nlogtaper_L,'nlogtaper-φH=25-φL=10-T=.15',0.15)

#Could I trun this into a gif maybe?




