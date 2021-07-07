# -*- coding: utf-8 -*-
"""
For simplicity, I'll probably always just set τ to 1. 
That way, all rates are in terms of 'infection durations'.
And I know that many paramaters will range in (0,1).

In individual's problem, r,tau,W are interchangable.
"""

import numsolve_newman_negbinom as nnn
import matplotlib.pyplot as plt
import numpy as np

#%%Helper functions and parameters
def labelSubplot(ax,title,xlabel,ylabel):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
CL_log10 = [1E-09,1E-08,1E-07,1E-06,1E-05,1E-04,1E-03,1E-02,1E-01,.99999999]
CL_percentile = np.arange(0,1.0001,0.01)
CL_logGraded = [.99999999999]

#%% Some grids
unit_grid = np.arange(0,1.00001,.001)
mu_grid = np.arange(0,30.000001,0.01)

#%% Plot Psi vs mu


fig,ax = plt.subplots(figsize=(8,5),constrained_layout=True)

for T in [0.05,0.1,0.3]:
    for α in [0.001,1,100]:
        ax.plot(mu_grid,[nnn.approx_Ψ(T,mu,α) for mu in mu_grid], label="T:"+str(T)+',α:'+str(α))
labelSubplot(ax, "newman_negbinom_muvsPsi", r'$\mu_N$', r'$\Psi$')
ax.grid()
ax.legend()
#plt.show()
plt.savefig('newman_negbinom_muvsPsi.png')

#%% PLot Psi vs Psi

fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
ax.plot(unit_grid,unit_grid,c='black',linestyle='dotted')
newMu_grid = [nnn.proportionalmeanresponse(Ψ,20,0) for Ψ in unit_grid]
for T in [0.05,0.1,0.3,.6]:
    for α in [0.001,1,1000]:
        newΨ_grid = [nnn.approx_Ψ(T,mu,α) for mu in newMu_grid]
        plt.plot(unit_grid,newΨ_grid,  label="T:"+str(T)+',α:'+str(α))
labelSubplot(ax, "newman_negbinom_Psi(mu(Psi))_proportionalresponse", r'$\Psi$', r'$\Psi(\mu(\Psi))$')

ax.grid()
ax.legend()

plt.savefig("newman_negbinom_Psi(mu(Psi))_proportionalresponse.png")


#%% PLot Psi vs Psi with different proportional response

fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
ax.plot(unit_grid,unit_grid,c='black',linestyle='dotted')
newMu_grid = [nnn.propmean_expondecay(Ψ,30,1/np.e) for Ψ in unit_grid]
for T in [0.05,0.1,0.3,.6]:
    for α in [0.0001,1,1000]:
        newΨ_grid = [nnn.approx_Ψ(T,mu,α) for mu in newMu_grid]
        plt.plot(unit_grid,newΨ_grid,  label="T:"+str(T)+',α:'+str(α))
labelSubplot(ax, "newman_negbinom_Psi(mu(Psi))_propresponse_expdecy", r'$\Psi$', r'$\Psi(\mu(\Psi))$')

ax.grid()
ax.legend()

plt.savefig("newman_negbinom_Psi(mu(Psi))_propresponse_expdecy.png")


#%% PLot Psi vs Psi when  everybody actually increases their connections in response to Psi

fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
ax.plot(unit_grid,unit_grid,c='black',linestyle='dotted')
newMu_grid = [nnn.proportionalmeanresponse(Ψ,0,30) for Ψ in unit_grid]
for T in [0.05,0.1,0.3,.6]:
    for α in [0.001,1,1000]:
        newΨ_grid = [nnn.approx_Ψ(T,mu,α) for mu in newMu_grid]
        plt.plot(unit_grid,newΨ_grid,  label="T:"+str(T)+',α:'+str(α))
labelSubplot(ax, "newman_negbinom_Psi(mu(Psi))_propresponse_increasing", r'$\Psi$', r'$\Psi(\mu(\Psi))$')

ax.grid()
ax.legend()

plt.savefig("newman_negbinom_Psi(mu(Psi))_propresponse_increasing.png")














#%% Plot contact risk T vs optimal Ni, for two types of people.


#parameters for choice of each type in absence of contagion
fig,ax = plt.subplots(figsize=(8,5),constrained_layout=True)
plt.plot(unit_grid,[nnp.approx_bestNi(1-Ψ, nnp.u_Nlogtaper_H) for Ψ in unit_grid])
plt.plot(unit_grid,[nnp.approx_bestNi(1-Ψ, nnp.u_Nlogtaper_L) for Ψ in unit_grid])
plt.plot(unit_grid,[1/Ψ for Ψ in unit_grid])
#plt.plot(unit_grid,[nnp.approx_bestNi(1-Ψ, lambda N: nnp.u_Nlogtaper(N,4,0.5)) for Ψ in unit_grid])
labelSubplot(ax, r'newman+poisson,$N_i^*(\Psi),logtaper$',r'$\Psi$',r'$N_i^*(\Psi)$')
ax.set_ylim([0,30])
ax.set_xlim([0,1])
ax.grid()
plt.savefig('graph_newman_poisson_Ni(Psi)_logtaper.png')



#%% Plot Ψ vs Ψ(N(Ψ))

def plot_Ψiteration(Ai_list,utilfunc_list,speciallabel):
    fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
    ax.plot(unit_grid,unit_grid,c='black',linestyle='dotted')
    #for T in [0.01,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]:
    #for T in [0.05,0.1,0.15,0.2,0.4,0.6,0.8]:
    #for T in [0.05,0.12769,0.2,0.4,0.6,0.8]:
    for T in [0.01,0.076,0.2,0.4,0.8]:
        newΨ_grid = [nnp.iterate_Ψ(Ψ, T, Ai_list, utilfunc_list) for Ψ in unit_grid]
        ax.scatter(unit_grid, newΨ_grid, label=r'$T=$'+str(T), marker='.')
    ax.set_ylim([0,1])
    ax.set_xlim([0,1])
    ax.legend()
    ax.grid()
    labelSubplot(ax, 'newman+poisson,Ψ(N(Ψ)),'+speciallabel, '$Ψ$', '$Ψ(\{N_i^*(Ψ)\})$')
    plt.savefig('graph_newman_poisson_Ψ(N(Ψ))_'+speciallabel+'.png')
    
#plot_Ψiteration([0.5,0.5],[nnp.u_Nlogtaper_H,nnp.u_Nlogtaper_L],'vlogtaper2510')    
#plot_Witeration([0.5,0.5],[npm.u_kremertest2,npm.u_kremertest3],'kremertestmix')    

#plot_Ψiteration([0.5,0.5],[lambda N: nnp.u_Nlogtaper(N,30,0.5),nnp.u_Nlogtaper_L],'vlogtaper3010')  
plot_Ψiteration([0.5,0.5],[lambda N: nnp.u_Nlogtaper(N,50,0.5),nnp.u_Nlogtaper_L],'vlogtaper5010')    


#%% Little test to try to find multiple equilibria.
def plot_Ψiteration_differencetest(Ai_list,utilfunc_list):
    xmn,xmx = 0,0.1
    ytol = .002
    smol_grid = np.arange(xmn,xmx,0.0001)
    fig,ax = plt.subplots(figsize=(5,5),constrained_layout=True)
    ax.plot(smol_grid,[0 for _ in smol_grid],c='black',linestyle='dotted')
    #for T in [.15, .152, .1528, .15285, .153 ]:
    for T in [ .07, .075, 0.076, 0.0761, 0.0762, 0.0763,  0.077, .08 ]:
        newΨdiff_grid = [nnp.iterate_Ψ(Ψ, T, Ai_list, utilfunc_list)-Ψ for Ψ in smol_grid]
        ax.scatter(smol_grid, newΨdiff_grid, label=r'$T=$'+str(T), marker='.')
    ax.set_ylim([-ytol,ytol])
    ax.set_xlim([xmn,xmx])
    ax.legend()
    ax.grid()
    plt.show()
#plot_Ψiteration_differencetest([0.5,0.5],[nnp.u_Nlogtaper_H,nnp.u_Nlogtaper_L])   
#plot_Ψiteration_differencetest([0.5,0.5],[lambda N: nnp.u_Nlogtaper(N,30,0.5), nnp.u_Nlogtaper_L]) 
plot_Ψiteration_differencetest([0.5,0.5],[lambda N: nnp.u_Nlogtaper(N,50,0.5), nnp.u_Nlogtaper_L])   

#%% Plot T vs equilibrium V, along with prevalences?

def plot_equilibriumvsT(Ai_list,utilfunc_list,speciallabel, zoomparams=(0,1,0.001)):
    '''Iterate through T, find an equilibrium edge risk at each point. 
    Plug that in to get choices and prevalences. Plot  two graphs.'''
    #zoomparems are of the form (minx,maxx,step)
    local_grid = np.arange(zoomparams[0],zoomparams[1],zoomparams[2])
    xlimits=[zoomparams[0],zoomparams[1]]

    #Calculate the gridpoints: eqlb edge risk, eqlb connections, eqlb r_infty
    equilV_grid = [nnp.approx_equilibriumV(T, Ai_list, utilfunc_list) for T in local_grid]
    equilΨ_grid = [1-V for V in equilV_grid]
    Ni_grids = [[nnp.approx_bestNi(V,utilfunc) for V in equilV_grid] for utilfunc in utilfunc_list]
    #averages 
    Rinfty_grids = [[nnp.calc_p(Ni, V) for Ni,V in zip(Ni_grid,equilV_grid)] for Ni_grid in Ni_grids]
    weightedN_grid = sum([Ai*np.array(Ni_grid) for Ai,Ni_grid in zip(Ai_list,Ni_grids)])
    weightedN2_grid = sum([Ai*np.array(Ni_grid)**2 for Ai,Ni_grid in zip(Ai_list,Ni_grids)])
    edgeweightedN_grid = weightedN2_grid/weightedN_grid
    weightedR_grid = sum([Ai*np.array(Ri_grid) for Ai,Ri_grid in zip(Ai_list,Rinfty_grids)])
    edgesharetype0_grid = Ai_list[0]*np.array(Ni_grids[0])/weightedN_grid
    
    # First plot a graph of risk and prevalence.
    fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
    
    ax.plot(local_grid,local_grid,c='black',linestyle='dotted')#45degree line
    for i,Ri_grid in enumerate(Rinfty_grids):
        ax.plot(local_grid, Ri_grid, label=r'$p(N_'+str(i)+r')$', marker='.')
    ax.plot(local_grid, equilΨ_grid, label=r'$Ψ_{eq}$', marker='.')
    ax.plot(local_grid, weightedR_grid, label=r'$R_{\infty}$', marker='.')
    ax.plot(local_grid, edgesharetype0_grid, label='$edgshr_{0}$', marker='.')
    
    ax.set_ylim([0,1])
    ax.set_xlim(xlimits)
    ax.legend(loc='lower right')
    ax.grid()
    labelSubplot(ax, 'newman+poisson, T vs equilibrium prevalence, '+speciallabel, '$T$', '')
    plt.savefig('graph_newman_poisson_equilibriumprev_'+speciallabel+'.png')
    
    
    #Then plot a graph of choices.
    fig,ax = plt.subplots(figsize=(8,8),constrained_layout=True)
    
    for i,Ni_grid in enumerate(Ni_grids):
        ax.plot(local_grid, Ni_grid, label='$N_'+str(i)+'$', marker='.')    
    plt.plot(local_grid,[1/Ψ for Ψ in equilΨ_grid], label=r'$N=\frac{1}{\Psi}$')
    ax.plot(local_grid, weightedN_grid, label='avg N', marker='.')   
    ax.plot(local_grid, edgeweightedN_grid, label='EdgeWtd avg N', marker='.')   
    
    ax.set_ylim([0,30])
    ax.set_xlim(xlimits)
    ax.legend(loc='upper right')
    ax.grid()
    labelSubplot(ax, r'newman+poisson, T vs $N_i^*(V^*(T))$, '+speciallabel, '$T$', '')
    plt.savefig('graph_newman_poisson_equilibriumchoices_'+speciallabel+'.png')
    

#u_Nlogtaper_20 = lambda N: nnp.u_Nlogtaper(N, 20, 0.5)
#plot_equilibriumvsT([0.5,0.5],[u_Nlogtaper_20,nnp.u_Nlogtaper_L],'vlogtaper2010')    
#plot_equilibriumvsT([0.5,0.5],[u_Nlogtaper_20,nnp.u_Nlogtaper_L],'vlogtaper2010zoom',(0.16,0.21,0.0001))  

#plot_equilibriumvsT([0.5,0.5],[nnp.u_Nlogtaper_H,nnp.u_Nlogtaper_L],'vlogtaper2510')    
#plot_equilibriumvsT([0.5,0.5],[nnp.u_Nlogtaper_H,nnp.u_Nlogtaper_L],'vlogtaper2510zoom',(0.14,0.16,0.0001))    

#u_Nlogtaper_30 = lambda N: nnp.u_Nlogtaper(N, 30, 0.5)
#plot_equilibriumvsT([0.5,0.5],[u_Nlogtaper_30,nnp.u_Nlogtaper_L],'vlogtaper3010')    
#plot_equilibriumvsT([0.5,0.5],[u_Nlogtaper_30,nnp.u_Nlogtaper_L],'vlogtaper3010zoom',(0.125,0.13,0.00001))  
#plot_equilibriumvsT([0.5,0.5],[u_Nlogtaper_30,nnp.u_Nlogtaper_L],'vlogtaper3010zoom2',(0.127,0.128,0.00001)) 

#plot_equilibriumvsT([0.1,0.9],[nnp.u_Nlogtaper_H,nnp.u_Nlogtaper_L],'vlogtaper2510_H10pc') 
#plot_equilibriumvsT([0.9,0.1],[nnp.u_Nlogtaper_H,nnp.u_Nlogtaper_L],'vlogtaper2510_H90pc') 
#plot_equilibriumvsT([0.05,0.95],[nnp.u_Nlogtaper_H,nnp.u_Nlogtaper_L],'vlogtaper2510_H05pc')    


u_Nlogtaper_50 = lambda N: nnp.u_Nlogtaper(N, 50, 0.5)
plot_equilibriumvsT([0.5,0.5],[u_Nlogtaper_50,nnp.u_Nlogtaper_L],'vlogtaper5010')   
plot_equilibriumvsT([0.5,0.5],[u_Nlogtaper_50,nnp.u_Nlogtaper_L],'vlogtaper5010zoom',(0.07,.08,0.0001))    
