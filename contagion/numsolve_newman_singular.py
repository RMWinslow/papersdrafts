# -*- coding: utf-8 -*-
"""
Input:
    n is the number of connections each person has
    T is the transmissibility of the contagion (in 0,1)
Calculates:
    Polynomial expansion of (1-T+TU)^{n-1}
    Solutions to (1-T+TU)^{n-1} = U (specifically U\in (0,1))
    Portion of population infected from outbreak. R_\infty 
    
This particular version just assumes every person in graph has n neighbors.
I've put (*) comments next to lines that directly come from this singular degree distribution.
Also, of course any function with n as an input also only makes sense with this graph structure.
"""

from numpy.polynomial import Polynomial as poly
import numpy as np
#https://numpy.org/doc/stable/reference/routines.polynomials.classes.html
#from fractions import Fraction as frac

#test = poly([1,2,3,4,5,6,7,8,9,10,11,12,13])

def pp(p):
    print(f"{p:unicode}")

#%% Calculate V = 1-T+TU = 1-Psi
#   V is the chance that a particular neighbor does not transmit to you.
#   Rewrite of the below, but the math for solving for V should be simpler.
#   This is still dependent on the singular distribution assumption.

def createVpolynomial(n,T):
    #(1-T)  -V + T*V**(n-1)
    assert n>1, "n needs to be at least 2 if you're plugging it in here."
    coefficients = [0]*n
    coefficients[0] = (1-T)
    coefficients[1] = (-1)
    coefficients[-1] += T
    return poly(coefficients)

def approximateV(n,T):
    if (T*(n-1) <= 1):                                                         #(*)
        return 1
    Vpoly = createVpolynomial(n,T)
    Vroots = Vpoly.roots()
    for root in Vroots:
        if (0 < root.real < 1) and np.isreal(root):
            return root.real
    print("Hey, what are you doing here?", n, T)
    
#Note to self, weird floating point precision problems with doing it this way
# It is about twice as fast, so I've got that going for me.
# The direct root approximation is incredibly precise, more precise than floating point.

#print(approximateV(3, 2/3))

def calcUviaV(n,T,V=None):
    if not V:
        V = approximateV(n,T)
        assert V > 0
    return 1 - (1-V)/T

def calcRviaV(n,T,V=None):
    if not V:
        V = approximateV(n,T)
    return 1-V**n                                                                #(*)


#%% functions for individual decisions
max_n = 50


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


