# -*- coding: utf-8 -*-
"""
This plots figures for the poisson model of disease spread.

Input:
    r is in (0,1) chance contact with ill transmits
    W is risk that a contact gets ill at some point during the epidemic
    tau is the duration of infectiousness
    vi are the contact rate of type i
    Ai are the portion of population which is type i. should sum to 1.
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



    
    


#%% Calculate U = (AH*nH*(1-T+TU)**(nH-1)+AL*nL*(1-T+TU)**(nL-1))/(AH*nH+AL*nL)
# Despite the imprecisions, I expect using V to be significantly faster now in the twotype case.

def createVpolynomial(T,nH,nL,AH=0.5,AL=0.5):
    assert (AH+AL)==1, "Population needs to be normalized."
    coefficients = [0]*max(nH,nL,2)
    μ = AH*nH+AL*nL
    coefficients[0] = μ*(1-T)
    coefficients[1] = μ*(-1)
    coefficients[nH-1] += T*AH*nH
    coefficients[nL-1] += T*AL*nL
    return poly(coefficients)

def calcTc(nH,nL,AH=0.5,AL=0.5):
    μ = AH*nH+AL*nL
    En2 = AH*nH*nH + AL*nL*nL #E[n^2]
    if En2 == μ: #check for zero in denominator. Happens when both n in [0,1].
        return np.inf
    else: 
        return  μ / (En2-μ)

def approxV(T,nH,nL,AH=0.5,AL=0.5):
    #check for critical threshold
    if (T <= calcTc(nH,nL,AH,AL)):                                                        
        return 1
    #if above Tc, calculate unique solution in (0,1)
    Vpoly = createVpolynomial(T,nH,nL,AH,AL)
    Vroots = Vpoly.roots()
    for root in Vroots:
        if ((1-T) <= root.real < 1) and np.isreal(root):
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

def u_nlogtaper(n,nsansV,weight):
    #nsansV is a parameter representing the optimum choice when V=1
    return weight*(np.log(n) - n**2 / (2*nsansV**2))

φH = 25
φL = 10

def u_nlogtaper_H(n):
    return u_nlogtaper(n,φH,0.5)
    
def u_nlogtaper_L(n):
    return u_nlogtaper(n,φL,0.5)
    




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
max_n = 100

def calcMyopicUgrid(V,utilfunc):
    util_grid = np.array([utilfunc(n)-calcMyopicRisk(n,V) for n in range(max_n)])
    return util_grid

def findMyopicBest_n(V,utilfunc):
    #only works on discrete n
    # in this function, n is myopic. not society wide n
    # uses numpy to speed things up. could be more clear. 
    #   it just finds index of max util
    util_grid = calcMyopicUgrid(V,utilfunc)
    best_outcomes = np.where(util_grid==max(util_grid))[0]
    return best_outcomes
   

''' #This one doesn't really make sense in the two-person case.
    #Needs a complete rewrite and reconceptualization even.
def SPPu(T,utilfunc):
    #This one is different. It finds the n that maximizes societal utility
    util_grid = np.array([utilfunc(n)-calcMyopicRisk(n,approximateV(n, T)) 
                          for n in range(max_n)])
    best_outcomes = np.where(util_grid==max(util_grid))[0]
    return best_outcomes
'''

def iterateV(V,T,utilfuncH,utilfuncL,AH=0.5,AL=0.5):
    #Given V in 0,1, find the optimum n_i(V) for each i, 
    #then plug these back into V({n_i},T)
    #Equilibrium where V=V(n(V))
    best_nH = findMyopicBest_n(V, utilfuncH)
    best_nL = findMyopicBest_n(V, utilfuncL)
    if len(best_nH) > 1 or len(best_nL) > 1:
        print("multiple optima at V="+str(V)+",T="+str(T))
        
    newV = approxV(T, best_nH[0], best_nL[0], AH=AH, AL=AL)
    if newV==V:
        print("equilibrium at V="+str(V)+",T="+str(T))
    
    return newV
        
        
        
        
def iterate_npair(nH,nL,T,utilfuncH,utilfuncL,AH=0.5,AL=0.5):
    V = approxV(T, nH, nL, AH=AH, AL=AL)
    #print(V)
    best_nH = findMyopicBest_n(V, utilfuncH)
    best_nL = findMyopicBest_n(V, utilfuncL)
    if len(best_nH) > 1 or len(best_nL) > 1:
        print("multiple optima at V="+str(V)+",T="+str(T))
    #print(best_nH,best_nL)
    return (best_nH[0],best_nL[0])
        
        
    
        

