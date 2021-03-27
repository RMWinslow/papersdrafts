---
title: contagion notes march 2021
---

## Main influences

Kremer, M. (1996). **[Integrating behavioral choice into epidemiological models of AIDS.](https://www.nber.org/papers/w5428)** *The Quarterly Journal of Economics, 111(2)*, 549-573.
: Models and compares steady states of endemic disease. People have preferences over the number of partners they have, and are also concerned about the chance they become infected $p(i)$. Multiple equilibria are possible. Increased prevelance can somtimes increase activity among high-activity groups. I use the same basic concepts, but try to adapt them to looking at the final outcome of a transient epidemic rather than an endmic steady state. [Link](https://www.nber.org/papers/w5428).

Newman, M. E. (2002). **[Spread of epidemic disease on networks.](https://arxiv.org/abs/cond-mat/0205009)** *Physical review E, 66(1)*, 016128.
: Solves for the distribution of disease spread on networks. Uses probability generating functions. Views epidemic from timeless network perspective, looking at final outcomes of outbreak rather than timepath of outbreak. [Link](https://arxiv.org/abs/cond-mat/0205009). See also the application to modelling SARS outbreak in [this paper.](https://www.sciencedirect.com/science/article/abs/pii/S0022519304003510?via%3Dihub)


Lloyd-Smith, J. O., Schreiber, S. J., Kopp, P. E., & Getz, W. M. (2005). **[Superspreading and the effect of individual variation on disease emergence.](https://www.nature.com/articles/nature04153)** *Nature, 438(7066)*, 355-359.
: Argues distribution of $R_0$ is highly skewed.Defines and discussing superspreading. Has PGF with negative binomial (poisson gamma compound) offspeing distribution. 
    Argues that interventions which give the same $R_0$ but higher variance are more likely to supress outbreaks. 


---

## Continous version, single type, timeless

### Setup

- Each person chooses amount of social interaction $n$ to have during the epidemic.
- Outside of epidemic, they have preferences for social interaction $$u(n)$$
    - Diminishing returns to social interaction: $u'' < 0$, $u'$ decreasing.
- Chance they get infected over the course of the epidemic is a function of social interaction $p(n)$
- Disutility of becoming infected: $c$
- Maximize $$u(n)-cp(n)$$
    - For continuous $n$, happens when $u'=cp'$
    - Naively expect increase in $p'$ or $c$ to be associated with increase in $u'$, which means lower $n$.


### Infection Probability, discrete n

I interact with a specific neighbor. What is the chance they transmit to me if they are sick? 
[Newman 2002]

- Rate of disease-causing contacts $r$
- Duration of infectiousness $\tau$
- Chance no infection occurs during time fragment $\delta t$: $$1-r \delta t$$
- chance no infection during any of those time fragments: $$(1-r\delta t)^{\tau/\delta t}$$
- Limit as time becomes continuous gives chance no transmission from that neighbor: $$1-T \equiv \lim_{\delta t\to 0}(1-r\delta t)^{\tau/\delta t} = e^{-r/\tau}$$
- Chance transmission occurs: $T$
- Following Newman, just look at T, ignore dynamics of timing.


What is the chance I don't get sick from any neighbors during epidemic?
- Define $R$ as chance that a given neighbor gets sick during epidemic.
- Chance they don't transmit to me: $1-RT$
- Chance no neighbors transmit to me: $(1-RT)^n$
- Chance at least 1 does: $1-(1-RT)^n$



### Infection Probability, continuous n

- Rate of transmission per unit of contact $\equiv RT$
- Total portion 



















---


### Setup

- Each type of person $k$ chooses amount of social interaction $n_k$
- Outside of epidemic, they have preferences for social interaction $$u_k(n_k)$$



---
## Setup

### Variables and Concepts



## Homogenous Fully Mixed




## Two types of people










---

## Cost from contagion risk.

- If you get infected, you experience disutility $\delta$.
    - Multiple infectious exposures don't incur any additional disutility. 
    - Let $$I_{\delta x}=1$$ iff person x is exposed to the contagion at some point during the epidemic, and 0 otherwise. 
- The expected disutility from disease exposure is thus $Pr(I_{\delta x}=1)\cdot\delta$
- $T$ is transmissibility of the contagion. Assume $T$ the same for all connections.
- Let $R_{\infty}$ denote the portion of the population that is exposed to the disease throughout the entire course of the epidemic. 
    - Because people are assumed to not know the connectivity of their neighbors, each person expects that each of their neighbors will become infected with probability $R_{\infty}$.
- The chance that the contagion is transmitted along any particular social connection is $TR_{\infty}$.
- The chance that none of your neighbors transmits to you is $\left[1-TR_{\infty}\right]^{n}$.
- The chance that *at least* one neighbor transmits to you is $1-\left[1-TR_{\infty}\right]^{n}$.
- The expected disutility from disease exposure is thus $\delta - \left[1-TR_{\infty}\right]^{n}\delta$
    - negative, within $[0,\delta)$
    - increasing in $n$
    - marginal disutility from increasing n:
        - discrete change from increase in $n$ by 1: 
            - $\delta - \left[1-TR_{\infty}\right]^{n+1}\delta - \delta + \left[1-TR_{\infty}\right]^{n}\delta$
            - $=[1-TR_{\infty}]^{n}\delta-[1-TR_{\infty}]^{n+1}\delta$
            - $=[1-TR_{\infty}]^{n}TR_{\infty}\delta$
            - positive and decreasing in n
        - continuous: $-[1-TR_{\infty}]^{n} \ln [1-TR_{\infty}] \delta$













































