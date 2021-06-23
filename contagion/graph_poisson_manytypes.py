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
labelSubplot(ax, r'poisson,optimal v for $u=\frac{1}{2}\ln(v)-\phi v^2$',r'$\tau r W$',r'$v^*(\tau r W)$')
ax.set_ylim([0,30])
ax.set_xlim([0,1])
plt.savefig('graph_poisson_v(rtauW)_logtaper.png')



#%% Plot W vs W(v(W))



#%% Plot two-type critical rτ threshold contour







