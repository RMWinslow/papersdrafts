# -*- coding: utf-8 -*-
"""
For simplicity, I'll probably always just set τ to 1. 
That way, all rates are in terms of 'infection durations'.
And I know that many paramaters will range in (0,1).

In individual's problem, r,tau,W are interchangable.
"""

import numsolve_newman_poisson as nnp
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

#%% Some grids
unit_grid = np.arange(0,1.00001,.001)

#%% Plot contact risk T vs optimal Ni, for two types of people.

#parameters for choice of each type in absence of contagion
fig,ax = plt.subplots(figsize=(8,5),constrained_layout=True)
plt.plot(unit_grid,[nnp.approx_bestNi(1-Ψ, nnp.u_Nlogtaper_H) for Ψ in unit_grid])
plt.plot(unit_grid,[nnp.approx_bestNi(1-Ψ, nnp.u_Nlogtaper_L) for Ψ in unit_grid])
plt.plot(unit_grid,[1/Ψ for Ψ in unit_grid])
labelSubplot(ax, r'newman+poisson,$N_i^*(\Psi),logtaper$',r'$\Psi$',r'$N_i^*(\Psi)$')
ax.set_ylim([0,30])
ax.set_xlim([0,1])
plt.savefig('graph_newman_poisson_Ni(Psi)_logtaper.png')



#%% Plot Ψ vs Ψ(N(Ψ))

def plot_Ψiteration(Ai_list,utilfunc_list,speciallabel):
    fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
    ax.plot(unit_grid,unit_grid,c='black',linestyle='dotted')
    #for T in [0.01,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]:
    for T in [0.05,0.1,0.15,0.2,0.4,0.6,0.8]:
        newΨ_grid = [nnp.iterate_Ψ(Ψ, T, Ai_list, utilfunc_list) for Ψ in unit_grid]
        ax.scatter(unit_grid, newΨ_grid, label=r'$T=$'+str(T), marker='.')
    ax.set_ylim([0,1])
    ax.set_xlim([0,1])
    ax.grid()
    ax.legend()
    labelSubplot(ax, 'newman+poisson,Ψ(N(Ψ)),'+speciallabel, '$Ψ$', '$Ψ(\{N_i^*(Ψ)\})$')
    plt.savefig('graph_newman_poisson_Ψ(N(Ψ))_'+speciallabel+'.png')
    
plot_Ψiteration([0.5,0.5],[nnp.u_Nlogtaper_H,nnp.u_Nlogtaper_L],'vlogtaper2510')    
#plot_Witeration([0.5,0.5],[npm.u_kremertest2,npm.u_kremertest3],'kremertestmix')    



#%% Little test to try to find multiple equilibria.


def plot_Ψiteration_differencetest(Ai_list,utilfunc_list):
    xmn,xmx = 0.1,0.125
    ytol = 0.002
    smol_grid = np.arange(xmn,xmx,0.0001)
    fig,ax = plt.subplots(figsize=(4,4),constrained_layout=True)
    ax.plot(smol_grid,[0 for _ in smol_grid],c='black',linestyle='dotted')
    for T in [.15, .152, .1528, .15285, .153 ]:
        newΨdiff_grid = [nnp.iterate_Ψ(Ψ, T, Ai_list, utilfunc_list)-Ψ for Ψ in smol_grid]
        ax.scatter(smol_grid, newΨdiff_grid, label=r'$T=$'+str(T), marker='.')
    ax.set_ylim([-ytol,ytol])
    ax.set_xlim([xmn,xmx])
    ax.grid()
    ax.legend()
    plt.show()
    
#plot_Ψiteration_differencetest([0.5,0.5],[nnp.u_Nlogtaper_H,nnp.u_Nlogtaper_L])   

#%% Plot T vs equilibrium V.











