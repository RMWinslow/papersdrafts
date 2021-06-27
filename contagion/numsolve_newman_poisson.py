# -*- coding: utf-8 -*-
"""
This plots figures for the poisson+Newman model of disease spread.

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

def calc_mu(Ai_list,Ni_list):
    "Returns dot product of two lists. Make sure Ai_list sums to 1, ya hear?"
    return sum([Ai*Ni for Ai,Ni in zip(Ai_list,Ni_list)])

def calc_Tc(Ai_list,Ni_list,mu):
    "Returns critical transmissibility threshold for a given social graph."
    #Only works for this Poisson thing. Not a general formula.
    EN2 = sum([Ai*Ni*Ni for Ai,Ni in zip(Ai_list,Ni_list)])
    return mu / EN2

def evaluate_Vfunc(V,T,Ai_list,Ni_list,mu):
    "The roots of this function gives us the true value of V."
    assert len(Ai_list) == len(Ni_list)
    numerator = sum([Ai*Ni*calc_p(Ni,V) for Ai,Ni in zip(Ai_list,Ni_list)])
    RHSfraction = (numerator/mu)
    return 1 - T*RHSfraction - V

def approx_V(T,Ai_list,Ni_list):
    "This finds the (non V=1) solution to contact unrisk formula."
    mu = calc_mu(Ai_list,Ni_list)
    Tc = calc_Tc(Ai_list,Ni_list,mu)
    if T <= Tc:
        return 1
    else:
        Vfunc = lambda V: evaluate_Vfunc(V,T,Ai_list,Ni_list,mu)
        return optimize.newton(Vfunc,1-T) #finds zero of Vfunc near (1-T)

#%% functions to approximate Ψ
# Basically equivalent to the above, but I want to see if numpy arrays speed things up.

def approx_Ψ(T,Ai_list,Ni_list):
    Ai_array = np.array(Ai_list)
    Ni_array = np.array(Ni_list)
    return approx_Ψ_using_arrays(T,Ai_array,Ni_array)

def approx_Ψ_using_arrays(T,Ai_array,Ni_array):
    "Approximates non-zero Ψ. Note that Ai_array and Ni_array must be numpy arrays."
    mu = np.sum(Ai_array*Ni_array)
    Tc = mu/np.sum(Ai_array*Ni_array*Ni_array)
    if T <= Tc:
        return 0
    else:
        Ψfunc = lambda Ψ: T-np.sum(Ai_array*Ni_array*np.exp(-Ψ*Ni_array))*T/mu - Ψ
        return optimize.newton(Ψfunc,T)
    
def evaluate_Ψfunc(Ψ,T,Ai_array,Ni_array,mu):
    return T-np.sum(Ai_array*Ni_array*np.exp(-Ψ*Ni_array))*T/mu - Ψ
    

#%% Test the comparitive speeds of numpy approximation vs the original one I made
def speedtest_VΨ(T,Ai_list,Ni_list,numbertrials):
    findV = lambda: approx_V(T, Ai_list, Ni_list)
    findΨ = lambda: 1-approx_Ψ(T, Ai_list, Ni_list)
    timeV = timeit.timeit(findV,number=numbertrials)
    timeΨ = timeit.timeit(findΨ,number=numbertrials)
    print("V="+str(findV())+",1-Ψ="+str(findΨ())+",diff="+str(findΨ()-findV()))
    print("Vtime:",timeV,"seconds")
    print("Ψtime:",timeΨ,"seconds")
    
#speedtest_VΨ(0.93, [1], [1.5], 10000)
#speedtest_VΨ(0.2, [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,], [5,10,15,20,12,4,3,19,8,20], 10000)
#speedtest_VΨ(0.2, [0.1]*100, [12]*100, 1000)
#speedtest_VΨ(0.2, [0.1]*100000, [12]*100000, 1)

#RESULTS:
#    Bad news: for a small number of types (like 1 or 2), the array version is slower.
#    Good news: for very large numbers of types, the array version works more quickly. 
#    So this might be useful if I want to approximate some distribution over types or something.


#%% Utility functions for contact target

def u_Nlogtaper(N,Nsansrisk,weight):
    #vsansrisk is a parameter representing the optimum choice when rtauW=0
    return weight*(np.log(N) - N**2 / (2*Nsansrisk**2))

φH = 20
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

    
        

