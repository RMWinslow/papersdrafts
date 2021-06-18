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

#%% Calculate U, the chance that a random edge traversal leads to uninfected person

def pp(p):
    print(f"{p:unicode}")

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

def isUroughlycorrect(U):
    #need to select correct root
    #problem: 
        return None

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
    print(n,t)


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

def calcMyopicIllnessRisk(n,T,U):
    #Here, the n is the individual's choice of neighbors.
    return 1 - (1-T+T*U)**n

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


