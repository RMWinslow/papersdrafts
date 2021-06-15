---
title: contagion notes march 2021
---

## Main influences

Kremer, M. (1996). **[Integrating behavioral choice into epidemiological models of AIDS.](https://www.nber.org/papers/w5428)** *The Quarterly Journal of Economics, 111(2)*, 549-573.
: Models and compares steady states of endemic disease. People have preferences over the number of partners they have, and are also concerned about the chance they become infected $$p(i)$$. Multiple equilibria are possible. Increased prevelance can somtimes increase activity among high-activity groups. I use the same basic concepts, but try to adapt them to looking at the final outcome of a transient epidemic rather than an endmic steady state. [Link](https://www.nber.org/papers/w5428).

Newman, M. E. (2002). **[Spread of epidemic disease on networks.](https://arxiv.org/abs/cond-mat/0205009)** *Physical review E, 66(1)*, 016128.
: Solves for the distribution of disease spread on networks. Uses probability generating functions. Views epidemic from timeless network perspective, looking at final outcomes of outbreak rather than timepath of outbreak. [Link](https://arxiv.org/abs/cond-mat/0205009). See also the application to modelling SARS outbreak in [this paper.](https://www.sciencedirect.com/science/article/abs/pii/S0022519304003510?via%3Dihub)


Lloyd-Smith, J. O., Schreiber, S. J., Kopp, P. E., & Getz, W. M. (2005). **[Superspreading and the effect of individual variation on disease emergence.](https://www.nature.com/articles/nature04153)** *Nature, 438(7066)*, 355-359.
: Argues distribution of $$R_0$$ is highly skewed.Defines and discussing superspreading. Has PGF with negative binomial (poisson gamma compound) offspeing distribution. 
    Argues that interventions which give the same $$R_0$$ but higher variance are more likely to supress outbreaks. 


---

## Continous version, single type, timeless

### Setup

- Each person chooses amount of social interaction $$n$$ to have during the epidemic.
- Outside of epidemic, they have preferences for social interaction $$u(n)$$
    - Diminishing returns to social interaction: $$u'' < 0$$, $$u'$$ decreasing.
- Chance they get infected over the course of the epidemic is a function of social interaction $$p(n)$$
- Disutility of becoming infected: $$c$$
- Maximize $$u(n)-cp(n)$$
    - For continuous $$n$$, happens when $$u'=cp'$$
    - Naively expect increase in $$p'$$ or $$c$$ to be associated with increase in $$u'$$, which means lower $$n$$.


### Infection Probability, discrete n

I interact with a specific neighbor. What is the chance they transmit to me if they are sick? 
[Newman 2002]

- Rate of disease-causing contacts $$r$$
- Duration of infectiousness $$\tau$$
- Chance no infection occurs during time fragment $$\delta t$$: $$1-r \delta t$$
- chance no infection during any of those time fragments: $$(1-r\delta t)^{\tau/\delta t}$$
- Limit as time becomes continuous gives chance no transmission from that neighbor: $$1-T \equiv \lim_{\delta t\to 0}(1-r\delta t)^{\tau/\delta t} = e^{-r/\tau}$$
- Chance transmission occurs: $$T$$
- Following Newman, just look at T, ignore dynamics of timing.


What is the chance I don't get sick from any neighbors during epidemic?
- Define $$R$$ as chance that a given neighbor gets sick during epidemic.
- Chance they don't transmit to me: $$1-RT$$
- Chance no neighbors transmit to me: $$(1-RT)^n$$
- Chance at least 1 does: $$1-(1-RT)^n$$

$$p(n) = 1-(1-RT)^n$$

$$\frac{dp}{dn} = -(1-RT)^n \ln (1-RT)$$

Always positive; but n is discrete so maybe doesn't work.

$$\delta p \equiv p(n+1)-p(n) \\
=  (1-RT)^n -(1-RT)^{n+1} \\
= (1-RT)^n (1 - (1-RT)) \\
= RT(1-RT)^n $$

$$\frac{d}{dR} [p(n+1)-p(n)]
=  \left[1-RT-RTn\right]T(1-RT)^{n-1}
$$

This is positive iff $$n < \frac{1}{RT} - 1$$
For $$n > RT - 1$$, a more common disease actually makes a person more likely to prefer increasing social activity. After all, if they're garunteed to get sick anyways, no point in worrying about it. (Similar to Kremer's result)
This transistion happens at different $$p(n)$$ depending on RT, but is never higher than $$p(n) = 1/e$$. So if you have enough connections to have a greater than $$1/e$$ chance of getting sick, then a more contagious or common epidemic would make you less worried about the risk of +1 connections.

eg For an epidemic which will eventually infect 60% of the population and has a 20% of transmitting along a given connection, then increasing your connections from 9 to 10 increases infection chance from $$p(9) \approx 0.684$$ to $$p(10) \approx .721$$ for an increase of $$0.038$$.
Make the disease more transmissive to T=30%, and $$p(9) \approx 0.832$$ to $$p(10) \approx .863$$ for an increase of $$0.030$$.
So a more dangerous disease *decreases* expected cost of 10th connection.

But this is a homogenous population without variation, so the chance that any particular individual gets infected must be the same as the portion of the population that gets infected.

$$p(n) = R = 1-(1-RT)^n$$

Note that for singular distribution $$p_n = 1$$, this matches the formula for $$S$$ from [Newman 2002].  
Or equivlently, since the generating function for the offspring distribution is just $$g(x)=(1-(1-x)T))^n$$, and chance of extinction $$u$$ is given by solution to $$u=g(u)$$, note that $$R=1-u=1-(1-(1-u)T))^n = 1-(1-RT))^n$$, following [Kremer]

Fixing $$n$$ and $$T$$, what values of R satisfy this?
- $$R=0$$ is always a solution, cooresponding to extinction of an outbreak.
- $$R=1$$ is only a solution if $$R=1=T$$
- Otherwise there is one solution in $$(0,1)$$ iff $$\frac{d}{dR} p(0) > 1$$, 
    - which happens iff $$nT > 1$$.
    - makes sense. If the transmisivity times number of connections are below 1, then average number of new cases per case falls below unit, so no epidemic possible, so only a finite portion of the infinite population gets infected as per Newman.
    - Sadly, I don't think there's a nice simple closed form for it. Easy to numerically solve though.

#### Equilibrium

So given exogenous transmission rate $$T$$, an equilbrium here consists of a pair $$R,n$$ such that

$$ n = \argmax_n [u(n) - c[1-(1-RT)^n]]
\tag{preferences}$$

$$ R = 1-(1-RT)^n$$ (prevalence)


With $$u(n)=-1/n$$, it seems like the result is always 
"max connections that prevent epidemic"
or "unboundedly large umber of connections. Makes sense.

With $$u(n)=-1/n - n/200$$, and no contagion
Get n=14, R=0, U=-.141  
With  c=0.08, T=0.2, 
Get n=12, R=0.91, U=-.216  
With more virulent contagion c=0.08, T=0.25, 
Get n=13,R=0.97,u=-.220

And what of $$u(n)= 20*n - n^2$$?
No contagion and $$n=10,R=.872,U=100$$  
Contagion $$T=0.2,c=30$$:
$$n=9,R=.785,U=75.5$$  
Contagion $$T=0.3,c=30$$:
$$n=10,R=.968,U=70.1$$

max= 75.4502726176 ; argmax= 9 ; R= 0.7849906785780745
max= 70.9728444744 ; argmax= 10 ; R= 0.9675718247229487




### Infection Probability, continuous n

- Rate of transmission per unit of contact $$\equiv RT$$
- Total portion 









- I have contacts at rate






- Rate of disease-causing contacts $$r$$
- Duration of infectiousness $$\tau$$
- Chance no infection occurs during time fragment $$\delta t$$: $$1-r \delta t$$



- transmission happens at individual poisson rate $$\nu$$















---
---
---












---
---
---






---


- Continuous version just collapses to Clauset paper.
- multiple types
- some sort of distribution similar to clauset that lets me use the binomial thing
- maybe just give up and claim timeless perspecitve somehow makes sense?



---


### Setup

- Each type of person $$k$$ chooses amount of social interaction $$n_k$$
- Outside of epidemic, they have preferences for social interaction $$u_k(n_k)$$



---
## Setup

### Variables and Concepts



## Homogenous Fully Mixed




## Two types of people










---

## Cost from contagion risk.

- If you get infected, you experience disutility $$\delta$$.
    - Multiple infectious exposures don't incur any additional disutility. 
    - Let $$I_{\delta x}=1$$ iff person x is exposed to the contagion at some point during the epidemic, and 0 otherwise. 
- The expected disutility from disease exposure is thus $$Pr(I_{\delta x}=1)\cdot\delta$$
- Var $$T$$ is transmissibility of the contagion. Assume $$T$$ the same for all connections.
- Let $$R_{\infty}$$ denote the portion of the population that is exposed to the disease throughout the entire course of the epidemic. 
    - Because people are assumed to not know the connectivity of their neighbors, each person expects that each of their neighbors will become infected with probability $$R_{\infty}$$.
- The chance that the contagion is transmitted along any particular social connection is $$TR_{\infty}$$.
- The chance that none of your neighbors transmits to you is $$\left[1-TR_{\infty}\right]^{n}$$.
- The chance that *at least* one neighbor transmits to you is $$1-\left[1-TR_{\infty}\right]^{n}$$.
- The expected disutility from disease exposure is thus $$\delta - \left[1-TR_{\infty}\right]^{n}\delta$$
    - negative, within $$[0,\delta)$$
    - increasing in $$n$$
    - marginal disutility from increasing n:
        - discrete change from increase in $$n$$ by 1: 
            - $$\delta - \left[1-TR_{\infty}\right]^{n+1}\delta - \delta + \left[1-TR_{\infty}\right]^{n}\delta$$
            - $$=[1-TR_{\infty}]^{n}\delta-[1-TR_{\infty}]^{n+1}\delta$$
            - $$=[1-TR_{\infty}]^{n}TR_{\infty}\delta$$
            - positive and decreasing in n
        - continuous: $$-[1-TR_{\infty}]^{n} \ln [1-TR_{\infty}] \delta$$









































Make an intuition about stability of equilibrium.
If you think R-0.5, then more likely
If everyone sick, you still might not be.

Critical portion of extraverts that keep the beaches open?

Hopping on a plane raises R to 1.

- heterogeneity
- extra layers on decision process.

Someone like aldo or Jan

- Joe pikcens unions



