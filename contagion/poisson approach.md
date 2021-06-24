## Single Type

- A person has individual contact rate $$v$$, fixed throughout course of epidemic.
- The chance a transmission can occur along a contact is $$r$$
    - Transmission only actually occurs if one person is infected and the other is susceptible.
- Pandemic lasts for $$T$$ units of time (this will cancel out later)
- An infected person is infectious for $$\tau$$ units of time.
- Let $$R$$ be shorthand for $$R_\infty$$, the portion of the population that gets infected over the course of the epidemic.
- If you a connection at random with another person during the pandemic, there is a $$\tau R \over T$$ chance that your partner is infectious at the time of the connection and an $$r {\tau R \over T}$$ chance that they transmit to you.
- Thus tranmission events where you can get infected happen at rate $$v r {\tau R \over T}$$.
- Rate of tranmission *per infection* is $$\nu\equiv vr\tau$$

### Risk of infection.

Given discrete units of time of length $$dt$$, the infection will last $$T \over dt$$ units of time, and the chance of infection during a discrete unit of time is $$r {\tau R \over T} dt$$.

The chance you **don't** get infected is thus 

$$\lim_{dt\to 0} (1 - v r {\tau R \over T} dt)^{T/dt} = 
\lim_{dt\to 0} (1 - v r R \tau (dt/T))^{T/dt}
= e^{-vrR\tau }$$

Note that this is invariant of the length of the epidemic, and depends instead on the total infectious person time $$R\tau$$. It's also worth noticing $$vr\tau$$, which is the number of potential transmission events per infection, ie $$R_0$$.

If everyone has the same contact and transmission rates $$v,r$$, then each person has $$R$$ chance of becoming infected, and consistency requires that 

$$R = 1 - e^{-vrR\tau}$$

Note $$R=0$$ is always a possibility, corresponding to the case where the outbreak goes extinct before it transitions into an epidemic.
Nonzero (epidemic) solutions only exist if $$vr\tau > 0$$.
Given that an epidemic does occur, the portion of population infected is increasing in $$vr\tau$$ and can be solved numerically.
An exact solution for $$R > 0$$ is given by $$(vr\tau+W(-e^{-vr\tau}vr\tau)) \over vr\tau$$, where $$W$$ is the principal branch of the [product logarithm](https://en.wikipedia.org/wiki/Lambert_W_function).
Unfortunately, this can't be expressed in terms of more elementary functions, so we'll have to be happy with this.

![R_infty_hires.png](R_infty.png)

<!--Holy canole. I already did all this back in november. Damn my memory is horrible. Something is really wrong with my mind.-->

### Chance an epidemic occurs

So $$e^{-R_\infty R_0}$$ is chance I don't get sick.

But assuming that I do, how many do I transmit to? What's the child distribution?

Expected number of of child infections is $$\nu=vr\tau=R_0$$, so assuming a poisson process for spreading the disease, generating function for offspring distribution is 

$$g(\maltese) = e^{-R_0 (1-\maltese)}$$

The chance you personally don't infect anyone is $$g(0)=e^{-\nu}$$

Ultimate extinction probability $$g_\infty(0)$$, the chance that an outbreak goes extinct in finite time is $$1-R = -W(- \nu /e^\nu)/\nu$$. This is a consequence of the static perspective.

Examples:

| $$R_0$$ | $$g(0)$$ | $$1-R$$
|---|---|---|
| 0.5 | 60% | 100% |
| 1 | 37% | 100% |
| 1.05 | 35% | 91% |
| 2 | 14% | 20% |
| 3 | 5% | 6% |

For any $$\nu \in (0,1)$$, the function $$W(\frac{-\nu}{e^\nu})$$ will just be $$-\nu$$, which will cancel out in the equation for $$R$$, giving $$R=0$$ without caveat or special case. Nice and clean... somehow.

### Marginal Risk of Infection.

Want to endogenize $$v$$ with incentives. To do that, need some preferences over contact rate given risk. Following Kremer(96), one simple option is to have disutility simply equal to probability of getting infected.

Our little agent treats $$R,r,\tau$$ as exogenous and chooses $$v$$ to maximize 

$$U(v) \equiv u(v) - \Pr (\text{infected} | v) 
= u(v) - (1-e^{-vr\tau R}) \\
= u(v) -1 + e^{-vr\tau R}$$

where $$u(v)$$ is the utility from social activity in the absence of a contagion. 

<!--TODO: What if u(v) and p(v) are not additively seperable?-->

Another way of interpreting: agent gets +1 util for healthiness, and this util exponentially decays as contact rate goes up. What is the half-life of expected health? $$\frac{-\ln (1/2)}{r\tau R} \approx \frac{0.69}{r\tau R}$$. This means when $$r\tau R\approx 0.69$$, +1 contact per period halves remaining expected utility from health. Likewise, when $$rR\approx 0.69$$, +1 contact per *infectious time* halves remaining expected utility from health. This could be when everyone is eventually gets sick, but tranmission only occurs along 69% of contacts, or the disease always transmits but only has an ultimate prevalence of 69%.

The marginal utility from additional social contact is

$$u'(v) - r\tau R e^{-vr\tau R}$$

- can be either positive or negative
- within range, right term always negative
- potential optimums wherever normal marginal utility equal to marginal disease disutility
- marginal disutility from disease risk is strictly decreasing. Most of the risk is front loaded on those first few connections.

Marginal disutility from disease risk specificially (=marginal chance of getting sick) is 

$$\frac{d}{dv} 1-e^{-vr\tau R} = r\tau Re^{-vr\tau R}$$

### Second derivatives

Then as $$R$$ increases, we get that 

$$\frac{d}{dR} r\tau Re^{-vr\tau R} = -vr\tau \cdot r\tau R e^{-vrR\tau} + r\tau e^{-vr\tau R} \\
= r \tau e^{-vr\tau R} \cdot [1-vr\tau R]$$

This means that increasing the prevalence of the disease actually decreases the marginal disutility from the disease when $$v > 1/r\tau R$$, meaning that the rate of contact exceeds the inverse of (the total disease time times the chance an infectious contact transmits ("total expected transmission time"?)). Or similarly, when $$v\tau > 1/rR$$ meaning that the number of contacts per disease-period exceeds the inverse of (final size of pandemic times chance an infectious contact transmits).

At this threshold of $$v=\frac{1}{r\tau W}$$, $$p(v;r,\tau,W)=1-e^{-1}=1-\frac{1}{e}\approx 0.63$$.
To repeat, **the fatalism threshold is when the probability of infection exceeds 1-1/e**,
as mentioned in one of Kremer's footnotes when the lifespan is of fixed length.

<!--For this setup, this threshold happens to be where the disutility and marginal disutility cross. $$1-e^{-vrR\tau}$$ equals $$rR\tau e^{-vrR\tau}$$ when DISREGARD I AM A DINGUS-->


## Equilibrium with one type

Given $$\tau, r$$, equilibrium consists of $$v, R$$ such that:

- Given $$\tau,r,R$$, $$v$$ solves

    $$\max_v [u(v) - (1-e^{v r \tau R})]$$

- The epidemic prevalence is consistent with the individual's choices:

    $$R = p(v;R,\tau,r) = 1-e^{-v \ r \tau R}$$




## Equilibrium with multiple types

Let $$W$$ be the weighted fully-mixed "pool-~~risk~~incidence". 
It's the chance that a randomly chosen *partner* 
gets infected at some point during the epidemic, 
noting that types with higher contact rates have higher chance of being partner:

$$W = \frac{\sum_i A_i v_i p(v_i;W,\tau,r)}{\sum_i A_i v_i }$$

And the chance an individual of type $$i$$ doesn't get infected is 

$$1 - p(n_i;W,\tau,r) = \lim_{dt \to 0}(1-vr\tau W (dt/T))^{T/dt} = e^{-v r \tau W}$$

Given $$\tau, r$$ and populations $$\{A_i\}$$, an equilibrium consists of $$\{v_i\},R, W$$ such that:

- For each $$i\in\{H,L\}$$, given $$\tau,r,R, W$$, $$v_i$$ solves

    $$\max_{v_i} [u(v_i) - (1-e^{- v_i r \tau W})]$$

- The epidemic prevalence is consistent with the individual's choices:

    $$W = \frac{\sum_i A_i v_i (1-e^{- v_i r \tau W})}{\sum_i A_i v_i } 
    = 1 - \frac{\sum_i A_i v_i (e^{- v_i r \tau W})}{\sum_i A_i v_i } $$

    $$R = \sum_i A_i (1-e^{-v_i \ r \tau W}) 
    = 1- \sum_i A_i e^{-v_i \ r \tau W}$$


The latter condition might be more easily conceptualized in terms of 

$$R_\infty = 1- \sum_i A_i e^{-R_{0i}W}$$

Unfortunately, this also must be solved numerically, 
and unlike the Lambert W up above or the polynomials in the discrete case, 
there isn't a snappy premade way of calculating it.
Would just have to find fixed points I suppose.

- Calculate detailed grid for $$v_i(W)$$ for each $$i$$.
- Iterating over W grid:
    - Plug in W to get $$v_i(R)$$ for each $$i$$
    - Use these to get $$1 - \frac{\sum_i A_i v_i (e^{- v_i r \tau W})}{\sum_i A_i v_i }$$
    - Call this quantity the "newW", and plot W vs newW
    - Phase diagram?
    - Somehow visualize $$R_\infty$$ as well. Plot W vs R?


### A few notes about solutions for W

- The solution $$W=0$$ always exists, regardless of parameters for $$v_i,r,\tau$$
- A solution $$W\in(0,1)$$ exists only if $$\frac{d}{dW}(1 - \frac{\sum_i A_i v_i (e^{- v_i r \tau W})}{\sum_i A_i v_i }) > 1$$ at $$W=0$$.
    - The above condition can be rearranged as "An epidemic occurs with non-zero probability iff $$r\tau E[v^2] > E[v]$$
    - If such a solution exists, it is unique because $$1 - \frac{\sum_i A_i v_i (e^{- v_i r \tau W})}{\sum_i A_i v_i }$$ is increasing and concave down over the domains for these parameters.



## Examples

<!--A note about Kremer's $$u(v)=\theta_i v_i - \phi v_i^2$$:
With my risk function, $$1-e^{-v_i \cdot r\tau W}$$, 
the marginal utility will be $$\theta_i - 2 \phi v_i  + r\tau W e^{-v_i \cdot r\tau W}$$.
This means that the marg utility is negative for all $$v$$ 
when $$\theta_i - 2 \phi v_i$$ is below a tangent line for $$r\tau W e^{-v_i \cdot r\tau W}$$.
The tangent lines go through the point $$(a,Ae^{-Aa})$$ where $$A\equiv Wr\tau$$
and have slope $$-A^2e^{-Aa}$$.
Put in slope intercept form, they become $$y=-A^2e^{-Aa}x + (Ae^{-Aa}+aA^2e^{-Aa})$$.
This means if $$\phi=A^2e^{-Aa}$$, 
then to get nonzero optimum, need $$\theta > (Ae^{-Aa}+aA^2e^{-Aa})$$.
At $$A=1$$, this means $$\phi=e^{-a}$$ needs $$\theta > (1+a)e^{-a} = (1+a)\phi$$,
and $$a=-\ln(\phi)$$, so needs $$\theta > (1-\ln(\phi))\phi$$.
More generally, it's $$\theta > \phi\cdot A\cdot (1-\ln(\phi / A^2))$$
So if $$A=1,\phi=0.002$$, need $$\theta > (1-\ln(0.002))0.002 \approx 0.014$$-->

### Example with taper log utility.

$$u(v) = \frac{1}{2} [\ln(v) - \frac{1}{2\phi^2}v^2]$$

for $$\psi = 25$$ and $$\psi = 10$$.


![](graph_poisson_v(rtauW)_logtaper.png)

*Just the orange and blue lines. The rest are a utility function of Kremer's that I used to debug.*

![](graph_poisson_W(v(W))_vlogtaper25,10.png)

*When the line is crammed against the bottom, that means the $$r\tau$$ is so low that the infection dies out even  if nobody social distances at all. When the line is crammed against the top, it means that $$r\tau$$ is so high that even the quarantine behavior of individuals isn't enough to appreciably reduce their chance of getting sick, or at least not among the types that dominate connections.*


# TODO tomorrow:
- [x] Second derivatives
- [x] Double check that this approach even makes sense.s
- [ ] what conditions needed on u to garuntee unique optimum in individual's prob
- [ ] Tie this back into the equilbrium setup
- [x] Extend equilibrium to multiple types?
- [ ] Calculate the Poisson contact equilibrium for a few different utility functions.
    - See notes right up above.
- [ ] Think about the following:

    What if vaccine arrives with poisson rate bleh?
    Then probability of infection becomes vrtauW/(vrtauW+bleh)?
    Doesn't seem quite the same, given that the W is also affected by vaccine arrival.





