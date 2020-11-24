# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 07:07:14 2020

@author: RobertWinslow
"""

import scipy.special.lambertw as W
import numpy as np
import matplotlib.pyplot as plt


# Generate data
xrange = np.linspace(0.1,10, num=100)

def R_infty(R_0):
    return 1+(1/R_0)*W(-R_0*np.e**(-R_0))

#ydata = [W(x) for x in xrange]
ydata = [R_infty(x) for x in xrange]


# plot the data
plt.plot(xrange, ydata, color='tab:blue')
#plt.xlabel('$x$')
#plt.ylabel('$W_0(x)$')
plt.xlabel('$R_0$')
plt.ylabel('$R_\infty = 1+ R_0^{-1} \cdot W_0(-R_0 e^{-R_0})$')
plt.savefig("R_infty_hires.png",dpi=200)