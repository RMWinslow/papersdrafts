# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:52:44 2020

@author: RobertWinslow
"""

import matplotlib.pyplot as plt
import numpy as np

#%%

def nonzero_chance_poisson(rn):
    return 1-np.e**(-rn)




#%%

xrange = np.linspace(0,5, num=101)

def gen_graph(function,filename,xrange, xlabel,ylabel):
    ydata = [function(x) for x in xrange]

    plt.plot(xrange, ydata, color='tab:blue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.savefig(filename,dpi=150)



gen_graph(nonzero_chance_poisson, "riskPois",xrange,"$rn$","$I_{\delta x}$")