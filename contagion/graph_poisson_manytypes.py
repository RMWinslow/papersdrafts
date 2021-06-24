# -*- coding: utf-8 -*-
"""
For simplicity, I'll probably always just set τ to 1. 
That way, all rates are in terms of 'infection durations'.
And I know that many paramaters will range in (0,1).

In individual's problem, r,tau,W are interchangable.
"""

import numsolve_poisson_manytypes as npm
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

#%% Plot contact risk rτW vs optimal v, for two types of people.

#parameters for choice of each type in absence of contagion
fig,ax = plt.subplots(figsize=(8,5),constrained_layout=True)
plt.plot(unit_grid,[npm.approx_bestvi(1,1,rtauW,npm.u_vlogtaper_H) for rtauW in unit_grid])
plt.plot(unit_grid,[npm.approx_bestvi(1,1,rtauW,npm.u_vlogtaper_L) for rtauW in unit_grid])
plt.plot(unit_grid,[1/Ψ for Ψ in unit_grid])
plt.plot(unit_grid,[npm.approx_bestvi(1,1,rtauW,npm.u_kremertest) for rtauW in unit_grid])
plt.plot(unit_grid,[npm.approx_bestvi(1,1,rtauW,npm.u_kremertest2) for rtauW in unit_grid])
plt.plot(unit_grid,[npm.approx_bestvi(1,1,rtauW,npm.u_kremertest3) for rtauW in unit_grid])
labelSubplot(ax, r'poisson,optimal v for $u=\frac{1}{2}\ln(v)-\phi v^2$ and some kremer stuff',r'$\tau r W$',r'$v^*(\tau r W)$')
ax.set_ylim([0,30])
ax.set_xlim([0,1])
plt.savefig('graph_poisson_v(rtauW)_logtaper.png')



#%% Plot W vs W(v(W))

def plot_Witeration(Ai_list,utilfunc_list,speciallabel):
    fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
    ax.plot(unit_grid,unit_grid,c='black',linestyle='dotted')
    ##r and tau are interchangable in consumers problem and in W formula.
    for r in [0.01,0.03,0.04,0.05,0.09,0.1,0.12,0.15,0.1535,0.2,0.3,0.6,1]:
        newW_grid = [npm.iterate_W(W,r,1,Ai_list,utilfunc_list) for W in unit_grid]
        ax.scatter(unit_grid, newW_grid, label=r'$r\tau=$'+str(r), marker='.')
    ax.set_ylim([0,1])
    ax.set_xlim([0,1])
    ax.grid()
    ax.legend()
    labelSubplot(ax, 'poisson,W(v(W)),'+speciallabel, '$W$', '$W(\{v_i^*(W)\})$')
    plt.savefig('graph_poisson_W(v(W))_'+speciallabel+'.png')
    
plot_Witeration([0.5,0.5],[npm.u_vlogtaper_H,npm.u_vlogtaper_L],'vlogtaper25,10')    
    



#%% Plot two-type critical rτ threshold contour







