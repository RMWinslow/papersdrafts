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
n_grid = np.arange(0,20)
TT,nn = np.meshgrid(T_grid,n_grid)

#%% Calc thrid dimension
#UU = approximateU(nn, TT)
simpleline = [[n*T for T in T_grid] for n in n_grid]
UU = [[approximateU(n, T) for T in T_grid] for n in n_grid]


#%% Make the graphs
testplt = plt.contourf(T_grid,n_grid,UU)
plt.grid()
plt.show()