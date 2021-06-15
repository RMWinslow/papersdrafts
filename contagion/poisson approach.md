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

So $$e^{R_\infty R_0}$$ is chance I don't get sick.

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
= u(v) + e^{-vr\tau R}$$

where $$u(v)$$ is the utility from social activity in the absence of a contagion

<!--TODO: What if u(v) and p(v) are not additively seperable?-->








## Multiple types

R_1, R_2

Risk Pol = $$R_1 N_1 \tau_1 + R_2 N_2 \tau_2$$









