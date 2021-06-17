# Newman-style disease network, discrete choice over number of neighbors.



## Contagion spread, singular degree distribution

Suppose every agent is identical and chooses $$n$$ connections. The degree distribution is described by $$p_n=1$$.

Following Newman, look at the the probability generating functions for the spread of this disease.

- PGF for number of neighbors: $$G_0(x)=\sum_k p_k x^k = x^n$$
- PGF for excess degree of random neighbor: $$G_1(x)=\frac{G'_0(x)}{\mu}=x^{n-1}$$
- PGF for number of transmissible connections: $$G_0(x;T)=G_0(1-(1-x)T)=(1-[1-x]T)^n$$
- PGF for number of neighbor's transmissible excess edges: $$G_1(x;T)=G_1(1-(1-x)T)=(1-[1-x]T)^{n-1}$$
- Critical Transmissibility threshold $$T_c = 1/G'_1(1) = \frac{1}{n-1}$$
- (Meyers Newman et al 2004) $$R_0 = T\frac{E[k^2]}{E[k]}-T = T(n-1)$$
- Chance that end of random edge remains uninfected determined implicitly by $$U=G_1(U;T) = (1-(1-U)T)^{n-1}$$
    - No disease $$U=1$$ is always a solution, 
        - and is the only solution if $$G'_1(1;T)=(n-1)T\geq 1$$ <!--because of concavity-->
    - Full infection $$U=0$$ is only a solution if $$T=1$$.
    - Otherwise if $$(n-1)T < 1$$, there exists a unique solution $$U\in(0,1)$$.
        - Unfortunately, can't be  solved in closed-form, but easy to approximate numerically
        - See [numerical-contagion-solver newman-singular.py](numerical-contagion-solver-newman-singular.py) for an example using numpy
- Chance that outbreak causes epidemic = fraction of population that gets infected = $$R_\infty = 1-G_0(U;T) =1-(1-T+TU)^n$$ (called S(T) in Newman)
    - Also must, in general, be numerically solved.
    - In this case, $$R=1-(1-T+TU)U=1-(1-T)U-TU^2$$, so holding T fixed, $$1-R$$ will be a weighted average of $$U$$ and $$U^2$$
        - That is, the chance that one of your neighbors stays healthy is at most the chance *nobody else* gets them sick, and at least that chance squared.
        - Higher transmission means $$1-R$$ closer to $$U$$, lower transmission means its farther away (holding U equal, allowing n to vary)
        - 

<!--March 21 notes are different because I ignored the excess degree construction from Newman. If every vertex has degree three, then critical T_c is 1/2 because one of those edges is how people *get sick* in the first place. The chance that a random outbreak causes a pandemic (equal to size of pandemic) is the chance that at least one of those *3* initial neighbors -->



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
- The chance that *at least* one neighbor transmits to you is $$p(n) = 1-\left[1-TR_{\infty}\right]^{n}$$.
    - negative, within $$[0,1)$$ for $$TR\in (0,1)$$
    - increasing in $$n$$ likewise
    - marginal risk of getting sick in going from $$n-1$$ to $$n$$ connections is positive and increasing in  $$n$$:
        
        $$\frac{dp(n)}{dn} = \left(1 - \left[1-TR_{\infty}\right]^{n}\right) - \left(1 - \left[1-TR_{\infty}\right]^{n-1}\right)$$
        $$=[1-TR_{\infty}]^{n-1}TR_{\infty}$$

        - for any given $$n$$, the marginal risk can be either increasing or decreasing:

        
        $$\frac{d}{dR}[1-TR_{\infty}]^{n-1}TR_{\infty} =
        -T^2(n-1) R (1-TR)^{n-2}+(1-TR)^{n-1} \\
        = [(1-TR)^{n-2}T][1-TR-TR(n-1)] \\
        = [''][1-TRn]$$


        - iff $$n > 1/(TR)$$, then the marginal expected disutility from your $$nth$$ connection actually decreases as epidemic becomes more severe.
        - This threshold occurs at different values of $$p(n)$$ depending on the the value of $$TR$$, but is bounded above by $$p(\frac{1}{TR}) < \frac{1}{e} \approx 37\%$$. 







# TODO Tomorrow
- [] Finish copying over discrete version (setup)(streamlined without fluff)
- [] Fix description of infection chance (R is the chance your neighbor gets sick, but (1-U) is the chance that they get sick in a way that potentially transmits to you.
- [] Combine Poisson and Discrete nieghbors:
    - Start with discrete results
    - Set that number of neighbors as the mean in a poisson distribution
    - Integrate the discrete results over that poisson distribution.
    - Will it collapse to be the same as poisson or will it turn into something more interesting?
- [] Figure out what I meant by "Continuous version just collapses to [Clauset](https://scholar.google.com/citations?user=e7VI_HcAAAAJ&hl=en&oi=sra) paper."












