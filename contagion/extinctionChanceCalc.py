# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:41:21 2020

@author: RobertWinslow
"""

import matplotlib.pyplot as plt
import numpy as np
#%%

R = 3
k = 0.2

def G(シ, R, k):
    return ((1-シ)*(R/k) + 1)**(-k)

def extinction_probability(R,k):
    previous_guess = 0
    error = 1
    while error > 0.0000000001:
        new_guess = G(previous_guess,R,k)
        #print(new_guess)
        error = abs(new_guess - previous_guess)
        previous_guess = new_guess
    return new_guess


#%%
    
krange = np.linspace(0,2, num=101)

ydata = [extinction_probability(3,k) for k in krange]

plt.plot(krange, ydata, color='tab:blue')
#plt.xlabel('$x$')
#plt.ylabel('$W_0(x)$')
plt.xlabel('$k$')
plt.ylabel('$R_\infty = 1+ R_0^{-1} \cdot W_0(-R_0 e^{-R_0})$')


