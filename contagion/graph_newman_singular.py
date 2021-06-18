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
n_grid = np.arange(0,31)
TT,nn = np.meshgrid(T_grid,n_grid)

#%% Calc third dimension
UU = [[calcUviaV(n, T) for T in T_grid] for n in n_grid]


#%% Make the graphs

fig, ax = plt.subplots()
CS = ax.contour(T_grid,n_grid,UU,[.0000001,.000001,.00001,.0001,.001,.01,.1,.99999999])
#CS = ax.contour(T_grid,n_grid,UU)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Newman,Singular,U(n,T)')
plt.grid()
plt.show()