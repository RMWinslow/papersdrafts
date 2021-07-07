# -*- coding: utf-8 -*-
"""
This plots figures for the poisson+Newman model of disease spread, 
where the Nis themselves are gamma distributed.

EXOGENOUS:
    
    T is the apriori chance that transmission can occur along a given contact.
    Ai are the portion of population which is type i. should sum to 1.
    utility functions for individuals.
ENDOGENOUS:
    Ni are the target contact number of type i
    W is risk that a contact gets ill at some point during the epidemic
Calculates:
    approximation of V, given T,A_i,N_i
    given V, the optimal N_i
    
    
This particular version assumes people choose the desired number of contacts N_i
But their actual number of contacts is generated from a Poisson process with rate N_i
And then after that, disease spread follows Newman.
"""

"""
Note to self for later: When you try out the Poisson thing, it might be handy
to iterate first via Ts and cache the polynomials.
"""

from numpy.polynomial import Polynomial as poly
import numpy as np
#https://numpy.org/doc/stable/reference/routines.polynomials.classes.html
#from fractions import Fraction as frac

from scipy import optimize

import timeit

import sympy as sym
#NOTE: Sympy is neat, but its symbolic solver seems slower than the polynomial 
#   root approach I've been using with numpy's polynomial solver.
#sym.init_printing(use_latex=False)

def pp(p):
    print(f"{p:unicode}")
    
Ɛ = np.finfo(float).eps

#%% functions to aproximate the value of V, given {A_i,N_i},T

def calc_p(Ni,V):
    "Calculates individual risk of infection, taking V for granted."
    return 1 - np.exp( Ni*(V-1) )


#%% functions to approximate Ψ
# Basically equivalent to the above, but I want to see if numpy arrays speed things up.

'''def approx_Ψ(T,mu,k):
    Tc = k/((1+k)*mu)
    if T <= Tc:
        return 0
    else:
        Ψfunc = lambda Ψ: T- T*(1+mu*Ψ/k)**(-k-1) - Ψ
        return optimize.newton(Ψfunc,T)
 '''   
    
def approx_Ψ(T,mu,α):
    Tc = 1/((1+α)*mu)
    if T <= Tc:
        return 0
    else:
        Ψfunc = lambda Ψ: T- T*(1+mu*Ψ*α)**(-1/α-1) - Ψ
        return optimize.newton(Ψfunc,T)
    
def evaluate_Ψfunc(Ψ,T,mu,k):
    return T- T*(1+mu*Ψ/k)**(-k-1) - Ψ

#%% Simple nonutility response where people just respond proportionately

def proportionalmeanresponse(Ψ,responsetoΨ0,responsetoΨ1):
    return responsetoΨ0*(1-Ψ) + responsetoΨ1*Ψ

def propmean_expondecay(Ψ, responseΨ0,portionleftatΨtenth):
    "Here, an increase in psi exponential decays mean"
    return responseΨ0*np.exp(np.log(portionleftatΨtenth)*10*Ψ)


    

#%% Utility functions for contact target

def u_Nlogtaper(N,Nsansrisk,weight):
    #vsansrisk is a parameter representing the optimum choice when rtauW=0
    return weight*(np.log(N) - N**2 / (2*Nsansrisk**2))

φH = 25
φL = 10

def u_Nlogtaper_H(N):
    return u_Nlogtaper(N,φH,0.5)
    
def u_Nlogtaper_L(N):
    return u_Nlogtaper(N,φL,0.5)


def u_kremertest(x):
    return 0.2*x - 0.004*x*x
def u_kremertest2(x):
    return 0.15*x - 0.004*x*x
def u_kremertest3(x):
    return 0.1*x - 0.004*x*x
    

#%% Find the best response N_i* to parameters V 

def approx_bestNi(V,utilfunc):
    #need to look at -U because scipy has minimization functions.
    #only goes to 10^-9 accuracy. And not bumping up against maxiter either. Weird.
    negU = lambda Ni: - utilfunc(Ni) + calc_p(Ni,V)
    return optimize.minimize_scalar(negU, bounds=(0, 1000), method='bounded',options={'xatol': Ɛ}).x
    





#%%Iterate {v_i} and W to get fixed points.

def iterate_V(V,T,Ai_list,utilfunc_list):
    "finds V(N(V))"
    Nistar_list = [approx_bestNi(V,utilfunc) for utilfunc in utilfunc_list]
    return approx_V(T,Ai_list,Nistar_list)

def iterate_Ψ(Ψ,T,Ai_list,utilfunc_list):
    return 1-iterate_V(1-Ψ,T,Ai_list,utilfunc_list)

def iterate_Ni_list(T,Ai_list,Ni_list,utilfunc_list):
    V = approx_V(T,Ai_list,Ni_list)
    return [approx_bestNi(V,utilfunc) for utilfunc in utilfunc_list]

def SPP_v_singletype(V,utilfunc):
    #return the contact rate that gives the maximum utility with awareness of W
    negSPPU = lambda N: - utilfunc(N) + calc_p(N,V)
    return optimize.minimize_scalar(negSPPU,bounds=(0, 1000), method='bounded',options={'xatol': Ɛ}).x

#%% Use iteration function to get equilibrium V

def approx_equilibriumV(T,Ai_list,utilfunc_list):
    "Finds a point where V(N(V))=V. Doesn't check for multiple equilibria."
    equilbriumfunc = lambda V: iterate_V(V,T,Ai_list,utilfunc_list) - V
    return optimize.newton(equilbriumfunc,1-T)

    
        

