

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
    - marginal disutility from infection risk:
        - discrete change from increase in $n$ by 1: 
            - $\delta - \left[1-TR_{\infty}\right]^{n+1}\delta - \delta + \left[1-TR_{\infty}\right]^{n}\delta$
            - $=[1-TR_{\infty}]^{n}\delta-[1-TR_{\infty}]^{n+1}\delta$
            - $=[1-TR_{\infty}]^{n}TR_{\infty}\delta$
            - positive and decreasing in n
        - continuous: $-n[1-TR_{\infty}]^{n-1} \delta$
        - second derivative $-n(n-1)[1-TR_{\infty}]^{n-2} \delta$
            - positive if $n\in (0,1)$
            - negative if $n > 1$













































