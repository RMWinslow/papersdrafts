# Newman-style disease network, discrete choice over number of neighbors.




## Cost from contagion risk.

- Var $$T$$ is transmissibility of the contagion. Assume $$T$$ the same for all connections.
- Var $$R \equiv R_{\infty}$$ denotes the portion of the population that is exposed to the disease throughout the entire course of the epidemic. 
    - Because people are assumed to not know the connectivity of their neighbors, each person expects that each of their neighbors will become infected with probability $$R_{\infty}$$.
- If you get infected, you experience disutility $$\delta$$.
    - Multiple infectious exposures don't incur any additional disutility. 
    - Let $$I_{\delta x}=1$$ iff person x catches contagion at some point during the epidemic, and 0 otherwise. 
    - The expected disutility from disease exposure is thus $$Pr(I_{\delta x}=1)\cdot\delta$$
- The chance that the contagion is transmitted along any particular social connection is $$TR_{\infty}$$.
- The chance that none of your neighbors transmits to you is $$\left[1-TR_{\infty}\right]^{n}$$.
- The chance that *at least* one neighbor transmits to you is $$1-\left[1-TR_{\infty}\right]^{n}$$.
- The expected disutility from disease exposure is thus   $$\delta - \left[1-TR_{\infty}\right]^{n}\delta$$
    - negative, within $$[0,\delta)$$
    - increasing in $$n$$
    - marginal expected disutility in going from $$n-1$$ to $$n$$ connections is positive and increasing in  $$n$$:
        
        $$\left(1 - \left[1-TR_{\infty}\right]^{n}\right)\delta - \left(1 - \left[1-TR_{\infty}\right]^{n-1}\right)\delta$$
        $$=[1-TR_{\infty}]^{n-1}TR_{\infty}\delta$$

        - for any given $$n$$, the marginal expected disutiltiy can be either increasing or decreasing:

        
        $$\frac{d}{dR}[1-TR_{\infty}]^{n-1}TR_{\infty}\delta =
        -T^2(n-1)\delta R (1-TR)^{n-2}+(1-TR)^{n-1} \\
        = [(1-TR)^{n-2}T\delta][1-TR-TR(n-1)] \\
        = [''][1-TRn]$$


        - iff $$n < 1/(TR)$$, then the marginal expected disutility from your $$nth$$ connection actually decreases.


    





# TODO Tomorrow
- [] Finish copying over discrete version (setup)(streamlined without fluff)
- [] Combine Poisson and Discrete nieghbors:
    - Start with discrete results
    - Set that number of neighbors as the mean in a poisson distribution
    - Integrate the discrete results over that poisson distribution.
    - Will it collapse to be the same as poisson or will it turn into something more interesting?
- [] Figure out what I meant by "Continuous version just collapses to [Clauset](https://scholar.google.com/citations?user=e7VI_HcAAAAJ&hl=en&oi=sra) paper."












