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
n_grid = np.arange(0,41)
TT,nn = np.meshgrid(T_grid,n_grid)

#%% Calc thrid dimension
#UU = approximateU(nn, TT)
simpleline = [[n*T for T in T_grid] for n in n_grid]
UU = [[approximateU(n, T) for T in T_grid] for n in n_grid]


#%% Make the graphs

fig, ax = plt.subplots()
#CS = ax.contour(T_grid,n_grid,UU,[0,.1,.2,.3,.5,.6,.7,.8,.9,.99999999])
#CS = ax.contourf(T_grid,n_grid,UU,[0,.0001,.001,.01,.1,.99999999,1])
CS = ax.contour(T_grid,n_grid,UU,[0,.0001,.001,.01,.1,.99999999])
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Newman,Singular,U(n,T)')
plt.grid()
plt.show()