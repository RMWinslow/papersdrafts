# -*- coding: utf-8 -*-
"""
This plots figures for the poisson model of disease spread.

EXOGENOUS:
    r is in (0,1) chance contact with ill transmits
    tau is the duration of infectiousness
    Ai are the portion of population which is type i. should sum to 1.
    utility function for individual.
ENDOGENOUS:
    vi are the contact rate of type i
    W is risk that a contact gets ill at some point during the epidemic
Calculates:
    approximation of W from self referential definition
    optimand for v given rtauW
    optimal risk which minimizes R_infty???
    
This particular version assumes people choose the poisson rate of contact
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

import sympy as sym
#NOTE: Sympy is neat, but its symbolic solver seems slower than the polynomial 
#   root approach I've been using with numpy's polynomial solver.
#sym.init_printing(use_latex=False)

def pp(p):
    print(f"{p:unicode}")

#%% functions to aproximate the value of W, given {A_i,v_i},r,tau


def calc_p(vi,r,tau,W):
    "Calculates individual risk of infection, taking W for granted."
    return 1 - np.exp(-vi*r*tau*W)

def evaluate_Wfunc(W,  r,tau,Ai_list,vi_list,mu):
    "The root of this function gives us the true value of W."
    #Ai_list and vi_list are list of population and contacts of each type.
    assert len(Ai_list) == len(vi_list)
    numerator = sum([Ai*vi*calc_p(vi,r,tau,W) for Ai,vi in zip(Ai_list,vi_list)])
    return (numerator/mu) - W
    
def approx_W(r,tau,Ai_list,vi_list):
    "This finds the non-zero solution to contact risk formula."
    assert np.sum(Ai_list) == 1
    mu = np.sum([Ai*vi for Ai,vi in zip(Ai_list,vi_list)], dtype='float64')
    # check for the case where 0 is the only solution
    if r*tau*np.sum([Ai*vi*vi for Ai,vi in zip(Ai_list,vi_list)], dtype='float64') <= mu:
        return 0
    #otherwise find the roots
    Wfunc = lambda W: evaluate_Wfunc(W,  r,tau,Ai_list,vi_list,mu)
    return optimize.brentq(Wfunc,np.finfo(float).eps,1)
    return optimize.newton(Wfunc,1)

def approx_W_newton(r,tau,Ai_list,vi_list):
    "This finds the non-zero solution to contact risk formula."
    assert np.sum(Ai_list) == 1
    mu = np.sum([Ai*vi for Ai,vi in zip(Ai_list,vi_list)], dtype='float64')
    # check for the case where 0 is the only solution
    if r*tau*np.sum([Ai*vi*vi for Ai,vi in zip(Ai_list,vi_list)], dtype='float64') <= mu:
        return 0
    #otherwise find the roots
    Wfunc = lambda W: evaluate_Wfunc(W,  r,tau,Ai_list,vi_list,mu)
    return optimize.newton(Wfunc,1)

def compare_solver_accuracy(vrtau):
    brenterror = evaluate_Wfunc(approx_W(1,vrtau,[1],[1]),1,vrtau,[1],[1],1)
    newtonerror = evaluate_Wfunc(approx_W_newton(1,vrtau,[1],[1]),1,vrtau,[1],[1],1)
    print("vrtau:",vrtau,"newton:",newtonerror,"brent:",brenterror)


#for vrtau in [1,2,3,1.01,1.00001]: compare_solver_accuracy(vrtau)
#brent seems more accurate. Sure, let's go with that.
#print(approx_W(1,1,[1],[2]))


#%% Utility functions for contact rate
# Basically same as for Newman stlye, but with u instead of V

def u_vlogtaper(n,vsansrisk,weight):
    #vsansrisk is a parameter representing the optimum choice when rtauW=0
    return weight*(np.log(n) - n**2 / (2*vsansrisk**2))

φH = 25
φL = 10

def u_vlogtaper_H(v):
    return u_vlogtaper(v,φH,0.5)
    
def u_vlogtaper_L(v):
    return u_vlogtaper(v,φL,0.5)


def u_kremertest(x):
    return 0.5*x - 0.025*x*x
    

#%% Find the best response V_i* to parameters rtauW 

def approx_bestvi(r,tau,W,utilfunc):
    #need to look at -U because scipy has minimization functions.
    #only goes to 10^-9 accuracy. And not bumping up against maxiter either. Weird.
    negU = lambda vi: - utilfunc(vi) + calc_p(vi,r,tau,W)
    return optimize.minimize_scalar(negU,options={'xtol': np.finfo(float).eps}).x
    


#%%Iterate {v_i} and W to get fixed points.

def iterate_W(W,r,tau,Ai_list,utilfunc_list):
    #returns W(v(W))
    vi_list = [approx_bestvi(r,tau,W,utilfunc) for utilfunc in utilfunc_list]
    return approx_W(r, tau, Ai_list, vi_list)

def iterate_vi_list(vi_list,r,tau,Ai_list,utilfunc_list):
    #v(W(v))
    W = approx_W(r, tau, Ai_list, vi_list)
    return [approx_bestvi(r,tau,W,utilfunc) for utilfunc in utilfunc_list]

def SPP_v_singletype(r,tau,utilfunc):
    #return the contact rate that gives the maximum utility with awareness of W
    negSPPU = lambda v: - utilfunc(v) + calc_p(v,r,tau,approx_W(r, tau, [1], [v]))
    return optimize.minimize_scalar(negSPPU,options={'xtol': np.finfo(float).eps}).x



    
        

