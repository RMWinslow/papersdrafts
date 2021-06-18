# Newman-style disease network, discrete choice over number of neighbors.

## Contagion spread, singular degree distribution

Suppose every agent is identical and chooses $$n$$ connections. The degree distribution is described by $$p_n=1$$.

- Var $$T$$ is transmissibility of the contagion. 
    - Assume $$T$$ is the same for all connections.
    - It can be interpreted as the apriori chance that the disease potentially transmits along an edge (meaning the edge is "open"; transmission won't actually occur if neither person involved gets sick.)
    - Don't worry about the timing involved. (percolation theory)

Following Newman, look at the the probability generating functions for the spread of this disease.

- PGF for number of neighbors: $$G_0(x)=\sum_k p_k x^k = x^n$$
- PGF for excess degree of random neighbor: $$G_1(x)=\frac{G'_0(x)}{\mu}=x^{n-1}$$
- PGF for number of transmissible connections: $$G_0(x;T)=G_0(1-(1-x)T)=(1-[1-x]T)^n$$
- PGF for number of neighbor's transmissible excess edges: $$G_1(x;T)=G_1(1-(1-x)T)=(1-[1-x]T)^{n-1}$$
- Critical Transmissibility threshold $$T_c = 1/G'_1(1) = \frac{1}{n-1}$$
- (Meyers Newman et al 2004) $$R_0 = T(\frac{E[k^2]}{E[k]}-1) = T(n-1)$$
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
        - Also, in this case $$U = \sqrt{\frac{1-R}{T} + \left(\frac{1-T}{2T}\right)} - \frac{1-T}{2T}$$, but that doesn't have any intuitively obvious interpretation. Nice to know for later that it's uniquely determined by aggregate facts about the disease.
- In this case, infected and uninfected people won't differ in degree distribution (duh)
<!--    - Probability that person has degree $$k$$ given that they don't get sick: $$p_k (1-T+TU)^k / \sum_j p_j (1-T+TU)^j = 1$$
    - PGF for degree of uninfected people: $$x \mapsto G_0([1-T+TU]x)/G_0(1-T+TU)$$
    - Mean degree of uninfected: $$[1-T+TU]G'_0([1-T+TU]) \over G_0([1-T+TU])$$ = n.
    - PGF for infected degree distribution: $$\frac{G_0(x)-G_0([1-T+TU]x}{q-G_0(1-T+TU)}$$-->


<!--March 21 notes are different because I ignored the excess degree construction from Newman. If every vertex has degree three, then critical T_c is 1/2 because one of those edges is how people *get sick* in the first place. The chance that a random outbreak causes a pandemic (equal to size of pandemic) is the chance that at least one of those *3* initial neighbors -->,

## Contagion Risk

The previous section covers the spread of contagion through population. 
This section covers the spread to an individual

- Var $$T$$ is transmissibility of the contagion. Assume $$T$$ the same for all connections.
- Assume you personally are not patient 0 of a spontaneous outbreak.
- What is the chance that a *particular* neighbor gets sick?
    - The chance they get sick at all is $$R_\infty$$
        - But that includes the chance of getting sick *from you*, in which case they can't pass it to you.
    - Var $$U$$ is the chance that absent your connection with them, that neighbor would not get sick.
        - Thus $$1-U$$ is the chance that they have the possibility of passing it on to you.
- The chance that the contagion is transmitted to you from any particular neighbor is $$(1-U)T$$.
    -  Var $$\Psi \equiv (1-U)T$$ 
- The chance that none of your neighbors transmits to you is $$\left[1-\Psi\right]^{n}$$.
- The chance that *at least* one neighbor transmits to you is $$p(n) = 1-\left[1-\Psi \right]^{n}$$.
    - In this setup, $$p(n)=R_\infty$$, though with variation in degree, this wouldn't necessarily hold.     
    - Range of $$[0,1)$$ if $$T\in(0,1)$$

Now suppose the individual takes $$U$$ for granted, and wants to go about myopically choosing $$n$$.

- For convinence, suppose that the person cares directly about disease risk $$p(n)$$
- The risk of getting sick is increasing in $$n$$, and the marginal increase in disease risk in going from $$n-1$$ connections to $$n$$ connections is 
        
    $$p(n) - p(n-1) = \left(1 - \left[1-\Psi\right]^{n}\right) - \left(1 - \left[1-\Psi\right]^{n-1}\right) \\
    = [1-\Psi]^{n-1} - [1-\Psi]^{n} \\
    =[1-\Psi]^{n-1}\Psi > 0$$

- For any given $$n$$, as $$\Psi$$ increases, (increasing transmissibility or final prevalence), the marginal disease risk can either increase *or* decrease.
  
    $$\frac{d}{d\Psi}[p(n) - p(n-1)]  
    = -(n-1)[1-\Psi]^{n-2} + n[1-\Psi]^{n-1} \\
    = [1-\Psi]^{n-2}[-(n-1) + n[1-\Psi]] \\
    = [1-\Psi]^{n-2}[1-n\Psi]$$

- iff $$n > 1/\Psi$$, then the marginal disease risk from your $$nth$$ connection actually *decreases* as each individual contact becomes more dangerous. 

![](graph_newman_singular_pdiffexperiment2.svg)

- This threshold occurs at different values of $$p(n)$$ depending on the the value of $$\Psi$$, but is bounded above by $$p(\frac{1}{\Psi}) < \frac{1}{e} \approx 37\%$$.
    - That is, if you are already more than 37% likely to get sick, a more hazardous disease might actually make you worry less about the marginal connection.
    - **Fatalism** ala Kremer 


<!--continuous version d/dn d/d\Psi) has threshold -1/lnV)-->

![Graph showing 6 depictions on the disease prevalence imposed by exogenous T and n.](graph_newman_singular.svg)

## Individual decision about contacts

- Var $$\delta$$ is the cost incurred by illness
- Aside from contagion, person recieves some utility $$u(n)$$ from contacts.
- Preferences are represented by $$U(n)=u(n)-\delta p(n)$$
- Myopic individual, taking $$\Psi$$ as given, chooses $$n\in\Z_+$$ to solve

    $$\max_n [u(n)-\delta p(n)] = \max_n [u(n) - \delta (1-[1-\Psi]^n)]$$

<!--maximimum connection number a la Kremer?-->    

## Equilibrium with singular distribution

Given $$T$$, a regular contagion equilbrium consists of a degree $$n\in \Z_+$$ and an edge unprevalence $$U$$ such that 
- Taking $$U$$ as given, $$n$$ solves 

    $$n = \argmax_n [u(n) - \delta + \delta (1-T+TU)^n ] \tag{preferences}$$

- This choice of $$n$$ causes the ultimate edge unprevalence to be $$U$$ satisfying:

    $$U = (1-T+UT)^{n-1} \tag{unprevalence}$$

Alternatively, in terms of the threat each neighbor poses for you, $$\Psi$$: 

$$n = \argmax_n [u(n) - \delta + \delta (1-\Psi)^n ] \tag{preferences}$$
$$\Psi = (1-[1-\Psi]^{n-1})T \tag{contact risk}$$

Alternatively, in terms of $$V$$, the chance that a particular neighbor doesn't transmit to you:

$$n = \argmax_n [u(n) - (1-V^n)\delta ] \tag{preferences}$$
$$1-V = (1-V^{n-1})T \tag{contact risk}$$




# TODO Tomorrow
- [ ] Graph somehow showing U,n equilibrium?
    - [x] Contour plot for U(n,t), also p and R? Psi?
    - [ ] Optimum n, given utility?
        - Graph u(n) and p(n) as function of n
        - Find some spiffy way to numerically solve
    - [ ] Is equilibrium efficient? What about directly choosing n* to get a good outcome?
    - [ ] Do that for a few different u functions.
- [ ] Version with two types. The *fatalism* is the interesting part!
- [ ] Combine Poisson and Discrete nieghbors:
    - Start with discrete results
    - Set that number of neighbors as the mean in a poisson distribution
    - Integrate the discrete results over that poisson distribution.
    - Will it collapse to be the same as poisson or will it turn into something more interesting?
    - (target connections can thus be continuous!
- [ ] Improve understanding of threshold? Maybe just move on?
- [ ] Figure out what I meant by "Continuous version just collapses to [Clauset](https://scholar.google.com/citations?user=e7VI_HcAAAAJ&hl=en&oi=sra) paper."
- Longer term ideas:
    - Make comparison to SIR predictions
    - Somehow shoehorn in the gamma / negbinom distributions to connect to Schreiber paper?
    - Come up with some sort of validation comparison
