# -*- coding: utf-8 -*-
"""
Input:
    nL is the number of connections each L-type person has.
    nH is the number of connections each H-type person has.
    AH and AN representing portions of the population of that type.
    T is the chance of potential transmission iid per connection (in 0,1)
Calculates:
    Polynomial solution of U
    Critical transmission threshold Tc
    Portion of population infected from outbreak. R_\infty 
    Solutions to individual optimization, equilibrium, SPP
    
This particular version assumes two types of people, each with discrete choice 
"""

"""
Note to self for later: When you try out the Poisson thing, it might be handy
to iterate first via Ts and cache the polynomials.
"""

from numpy.polynomial import Polynomial as poly
import numpy as np
#https://numpy.org/doc/stable/reference/routines.polynomials.classes.html
#from fractions import Fraction as frac

import sympy as sym
from sympy import init_printing
#NOTE: Sympy is neat, but its symbolic solver seems slower than the polynomial 
#   root approach I've been using with numpy's polynomial solver.
init_printing(use_latex=False)

def pp(p):
    print(f"{p:unicode}")

#%% Calculate U = (AH*nH*(1-T+TU)**(nH-1)+AL*nL*(1-T+TU)**(nL-1))/(AH*nH+AL*nL)
# Despite the imprecisions, I expect using V to be significantly faster now.

def createVpolynomial(T,nH,nL,AH=0.5,AL=0.5):
    assert nH>1, "nL needs to be at least 2 if you're plugging it in here."
    assert nL>1, "nH needs to be at least 2 if you're plugging it in here."
    assert (AH+AL)==1, "Population needs to be normalized."
    coefficients = [0]*max(nH,nL)
    μ = AH*nH+AL*nL
    coefficients[0] = μ*(1-T)
    coefficients[1] = μ*(-1)
    coefficients[nH-1] += T*AH*nH
    coefficients[nL-1] += T*AL*nL
    return poly(coefficients)

def calcTc(nH,nL,AH=0.5,AL=0.5):
    μ = AH*nH+AL*nL
    En2 = AH*nH*nH + AL*nL*nL #E[n^2]
    return  μ / (En2-μ)

def approxV(T,nH,nL,AH=0.5,AL=0.5):
    #check for critical threshold
    if (T <= calcTc(nH,nL,AH,AL)):                                                         
        return 1
    #if above Tc, calculate unique solution in (0,1)
    Vpoly = createVpolynomial(T,nH,nL,AH,AL)
    Vroots = Vpoly.roots()
    for root in Vroots:
        if (0 < root.real < 1) and np.isreal(root):
            return root.real
    print("Hey, what are you doing here?", T,nH,nL,AH,AL)
    
#Note to self, weird floating point precision problems with doing it this way
# It is about twice as fast, so I've got that going for me.
# The direct root approximation is incredibly precise, more precise than floating point.

#print(approximateV(3, 2/3))

def calcUviaV(T,nH,nL,AH=0.5,AL=0.5, V=None):
    if not V:
        V = approxV(T,nH,nL,AH,AL)
        assert V > 0
    return 1 - (1-V)/T

def calcRviaV(T,nH,nL,AH=0.5,AL=0.5, V=None):
    if not V:
        V = approxV(T,nH,nL,AH,AL)
        assert V > 0
    return 1 - AH*V**nH - AL*V**nL                             


#%% utility functions

def calcMyopicRisk(n,V):
    #Here, the n is the individual's choice of neighbors.
    return 1 - V**n

def neginverse_u(n):
    if 0 == n:
        return -1000
    return 2 - (1 / n)

def big_neginverse_u(n):
    if 0 == n:
        return -1000
    return 2 - (5 / n)

def u_kremertest(n):
    return 0.5*n - 0.025*n*n

def u_neginv_withtaper(n):
    if 0 == n:
        return -1000
    return 5*(1-(1/n)) - 0.001*n*n


def u_smol_neginv_withtaper(n):
    if 0 == n:
        return -1000
    return (1-(1/n)) - 0.0002*n*n

#%% Functions for calculating individual and SPP decisions
max_n = 50

def calcMyopicU(V,utilfunc):
    util_grid = np.array([utilfunc(n)-calcMyopicRisk(n,V) for n in range(max_n)])
    return util_grid

def findMyopicBest_n(V,utilfunc):
    #only works on discrete n
    # in this function, n is myopic. not society wide n
    # uses numpy to speed things up. could be more clear. 
    #   it just finds index of max util
    util_grid = calcMyopicU(V,utilfunc)
    best_outcomes = np.where(util_grid==max(util_grid))[0]
    return best_outcomes
    
def SPPu(T,utilfunc):
    #This one is different. It finds the n that maximizes societal utility
    util_grid = np.array([utilfunc(n)-calcMyopicRisk(n,approximateV(n, T)) 
                          for n in range(max_n)])
    best_outcomes = np.where(util_grid==max(util_grid))[0]
    return best_outcomes

#%% Calculate U, the chance that a random edge traversal leads to uninfected person

def G1xTpoly(n,T):
    basepoly = poly([1-T,T]) #(1-(1-x)T)
    #For singular distribution, simply raise to the power of (n-1)
    G1xT = basepoly**(n-1)                                                     #(*)
    return G1xT

def approximateUroots(n,T):
    #U is implicitly defined by U=G1(U;T)
    #Thus defined by roots of G1(U;T)-U
    G1xT = G1xTpoly(n, T)
    lonelyU = poly([0,1])
    implicitUpoly = G1xT - lonelyU
    return implicitUpoly.roots()

def approximateU(n,T):
    #assert 0 < T < 1, "T outside of (0,1)"
    #assert T*(n-1) > 1, "T not above critical threshold"                      #(*)
    if (T*(n-1) <= 1):                                                         #(*)
        return 1
    #given the roots to U=G1(x;T), select the unique real solution in (0,1)
    # (if it doesn't exist, then return None, but those should be caught by the assertions)
    # numpy approximates roots by approimating eigenvalues of companion matrix.
    for root in approximateUroots(n,T):
        if (0 < root.real < 1) and np.isreal(root):
            return root.real
    print(n,T)

def calcVfromU(n,T,U=None):
    if not U:
        U = approximateU(n, T)
    return (1-T+T*U)

#Note to self, using fractions seems to return error 
#    "ufunc 'isfinite' not supported for the input types"
#    unfortunate because the fraction printing is pretty.
#    Also, root solver return complex numbers when too close to critical threshold.

#test = approximateU(4,.99999)
#print(test)


#%% Given U, calculate R, called S(T) in Newman
#   which reprsents both chance and final prevalence of epidemic. 

def G0xTpoly(n,T):
    basepoly = poly([1-T,T]) #(1-(1-x)T)
    #For singular distribution, simply raise to the power of (n-1)
    G0xT = basepoly**(n)                                                       #(*)
    return G0xT
    

def calculateRinfty(n,T,U=None):
    if not U:
        U = approximateU(n,T)
    G0xT=G0xTpoly(n, T)
    return 1 - G0xT(U)



#%% Simple output to console using global variables
'''
n = 3
T = 2/3

U = approximateU(n,T)
R = calculateRinfty(n,T,U)    
    
print('R_\infty = ',R)
print('U = ',U)
'''

#%%


