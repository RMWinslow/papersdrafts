---
title: contagion notes march 2021
---

## Main influences

Kremer, M. (1996). **Integrating behavioral choice into epidemiological models of AIDS.** *The Quarterly Journal of Economics, 111(2)*, 549-573.
: Models and compares steady states of endemic disease. People have preferences over the number of partners they have, and are also concerned about the chance they become infected $p(i)$. Multiple equilibria are possible. Increased prevelance can somtimes increase activity among high-activity groups. I use the same basic concepts, but try to adapt them to looking at the final outcome of a transient epidemic rather than an endmic steady state. [Link](https://www.nber.org/papers/w5428).

Newman, M. E. (2002). **Spread of epidemic disease on networks.** *Physical review E, 66(1)*, 016128.
: Solves for the distribution of disease spread on networks. Uses probability generating functions. Views epidemic from timeless network perspective.  [Link](https://arxiv.org/abs/cond-mat/0205009).

---










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













































