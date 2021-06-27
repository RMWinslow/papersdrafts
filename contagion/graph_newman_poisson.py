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
plt.plot(unit_grid,[nnp.approx_bestNi(1-Ψ, lambda N: nnp.u_Nlogtaper(N,4,0.5)) for Ψ in unit_grid])
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
    ax.legend()
    plt.show()
#plot_Ψiteration_differencetest([0.5,0.5],[nnp.u_Nlogtaper_H,nnp.u_Nlogtaper_L])   

#%% Plot T vs equilibrium V, along with prevalences?

def plot_equilibriumvsT(Ai_list,utilfunc_list,speciallabel):
    '''Iterate through T, find an equilibrium edge risk at each point. 
    Plug that in to get choices and prevalences. Plot  two graphs.'''
    #unit_grid = np.arange(0.15,0.155,0.00001)
    #Calculate the gridpoints: eqlb edge risk, eqlb connections, eqlb r_infty
    equilV_grid = [nnp.approx_equilibriumV(T, Ai_list, utilfunc_list) for T in unit_grid]
    equilΨ_grid = [1-V for V in equilV_grid]
    Ni_grids = [[nnp.approx_bestNi(V,utilfunc) for V in equilV_grid] for utilfunc in utilfunc_list]
    Rinfty_grids = [[nnp.calc_p(Ni, V) for Ni,V in zip(Ni_grid,equilV_grid)] for Ni_grid in Ni_grids]
    
    
    # First plot a graph of risk and prevalence.
    fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
    
    ax.plot(unit_grid,unit_grid,c='black',linestyle='dotted')#45degree line
    for i,Ri_grid in enumerate(Rinfty_grids):
        ax.plot(unit_grid, Ri_grid, label=r'$R_{\infty '+str(i)+r'}$', marker='.')
    ax.plot(unit_grid, equilΨ_grid, label=r'$Ψ_{eq}$', marker='.')
    
    ax.set_ylim([0,1])
    ax.set_xlim([0,1])
    ax.legend()
    ax.grid()
    labelSubplot(ax, 'newman+poisson, T vs equilibrium prevalence, '+speciallabel, '$T$', '')
    plt.savefig('graph_newman_poisson_equilibriumprev_'+speciallabel+'.png')
    
    
    #Then plot a graph of choices.
    fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
    
    
    for i,Ni_grid in enumerate(Ni_grids):
        ax.plot(unit_grid, Ni_grid, label='$N_'+str(i)+'$', marker='.')    
    plt.plot(unit_grid,[1/Ψ for Ψ in equilΨ_grid], label=r'$n=\frac{1}{\Psi}$')
    #plt.plot([0.153,0.153],[0,30])
    
    ax.set_ylim([0,30])
    ax.set_xlim([0,1])
    ax.legend()
    ax.grid()
    labelSubplot(ax, r'newman+poisson, T vs $N_i^*(V^*(T))$, '+speciallabel, '$T$', '')
    plt.savefig('graph_newman_poisson_equilibriumchoices_'+speciallabel+'.png')
    


plot_equilibriumvsT([0.5,0.5],[nnp.u_Nlogtaper_H,nnp.u_Nlogtaper_L],'vlogtaper2510')    







