## Goal
- Want to find a utility function such that the optimal response to contagion risk in the Newman+Poisson case has a nice analytical solution
- Use this to force the distribution of connections to be distributed according to a gamma distribution so that the offspring distribution becomes Negative Binomial.
- Connect to the Schreiber Paper


## Gamma distribution facts

Gamma distribution parameters:
- dispersion $$k$$ (this is the big one)
- mean $$\mu=R_0=k\theta$$
- scale $$\theta=\mu/k$$
- rate $$\beta=1/\theta=k/\mu$$
- pdf 
   
    $$f(x)=\frac{k^k x^{k-1} e^{-kx/\mu}}{\mu^k\Gamma(k)}$$
- variance $$\sigma^2=k\theta^2=\mu^2/k$$
- cdf
  
    $$F(x;k,\mu) = {\gamma(k,\frac{k x}{\mu}) \over \Gamma(k)} = \frac{\int_0^{\frac{k x}{\mu}} t^{k-1} e^{-t} \; dt}{\int_0^\infty t^{k-1} e^{-t} \; dt}$$







## Integrating over types instead of summing over types.

I need to stop using $$k$$ as subscript for a partiicular degree. How about little unidexed $$n$$?

The PGF for connections is PGF for connections: $$G_0(X)=\sum_{n=0}^\infty p_n x^n$$.

If there are multiple discrete types, with each type's connections being distributed according to iid Poisson process, then this PGF becomes: $$G_0(X)=\sum_{🍌=0}^\infty p_🍌 x^🍌 = \sum_i [A_i \sum_{🍌=0}^\infty \frac{N_i^🍌 e^{-N_i} x^🍌}{🍌!}] = \sum_i [ A_i e^{(x-1)N_i}]$$ because $$p_🍌 = \sum_i A_i Pr(n_i = 🍌 | N_i) = \sum_i A_i \frac{N_i^🍌 e^{-N_i}}{🍌!}$$.

If there are multiple discrete types, with each type's connections being distributed according to iid Poisson process, then this PGF becomes: $$G_0(X)=\sum_{n=0}^\infty p_n x^n = \sum_i [A_i \sum_{n=0}^\infty \frac{N_i^n e^{-N_i} x^n}{n!}] = \sum_i [ A_i e^{(x-1)N_i}]$$ because $$p_n = \sum_i A_i Pr(n_i = n | N_i) = \sum_i A_i \frac{N_i^n e^{-N_i}}{n!}$$.

Now instead we want to integrate across a continuum of types
- Instead of a discrete setof types like $$i\in\{H,L\}$$, we have a continuum $$i\in[0,1]$$
- Instead of $$A_i\equiv Pr(type=i)$$, now $$A_i \equiv f(i)$$, the pdf for type over the support $$(0,1)$$.

So now $$p_n = \int_i A_i Pr(n_i = n | N_i)$$....

# TODO JUNE 30: Finish the above!












## Potential Utility function

Simplifying a bit,
(utility and disutility left unspecified)
 the individual's problem becomes 

> Taking $$\Psi$$ as given, choose $$N$$ to solve $$N=\argmax_N [u(N) - p(N)]$$

Now make the following assumptions about the disutility incurred by disease risk $$p(N)$$:
- Diseasee risk disutility $$p(N)$$ is a strictly increasing function of $$N$$
- Marginal disutility from disease risk $$p'(N)$$ is a strictly decreasing function of $$N$$ (concave down) ($$p'' < 0$$)

And the following assumptions on regular utility from connections $$u(N)$$:
- Marginal connection utility is diminishing in number of connections. $$u'' < 0$$

Potential optimums occur where $$u' = p'$$


If I want to use FOCs to find the unique optimum to $$U(N)$$, then I need $$U$$ to be concave down on the entire domain of $$N\in [0,\infty)$$.
But the cost $$-p(N)$$ is concave up, so $$u$$ needs to not only be concave down, but, like really super duper concave down so that it overwhelms the concaveupness of the expected cost from disease exposure.



### What about a different exponential for u?

Suppose $$u(N) = -\frac{1}{\rho} e^{-\rho N}$$.
Then $$U(N) = -\frac{1}{\rho}e^{-\rho N} - 1 + e^{-\Psi N}$$,
and so $$U'(N) = e^{-\rho N} - \Psi e^{-\Psi N}$$.

Regardless of $$\rho$$, $$U'(0;0)=1$$. Hrm.

FOC is then: 

$$e^{-\rho N} = \Psi e^{-\Psi N}$$

$$-\rho N = \ln\Psi -\Psi N$$

$$N^* = \frac{\ln\Psi}{\Psi-\rho}$$

- Notice that $$\Psi\in[0,1]$$ so the top is negative, and $$N\geq 0$$, so this only has a valid solution if $$\rho > \Psi$$
- If $$\Psi=0$$, then the above FOC breaks. 
    - In this case $$U' > 0$$, so  $$N^*=+\infty$$
- If $$\Psi > \rho$$, then $$U' \geq e^{-\Psi N} - \Psi e^{-\Psi N} > 0$$, so again $$N^*=+\infty$$.
- the limit as $$\Psi\to 1$$ is 0, 
    - Note that $$U'(N;1)=e^{-\rho N} -  e^{- N} = e^{-N} [\frac{e^{-\rho N}}{e^{-\N}}  - 1] = e^{-N}[e^{-\rho N + N} - 1]$$ 
    - So if $$\rho > 1$$, then $$-\rho N+N \leq 0$$ so $$U'$$ is always nonpositive, 
    - And that means $$N^*=0$$ 
- Large $$\rho$$ leads to smaller optimal $$N$$, and it's tiny unless $$\Psi$$ is microscopic. It's only $$\approx 9$$ at $$\Psi=0.0001,\rho=1$$ 

Unfortunately, for this setup, the utility function very quickly shrinks from infinity to tiny numbers and then slows down but never reverses course. The condition that I'm missing is that:

- It must be that in the event of garunteed infection when you make contact with others, there is nonetheless incentive to make contact with others. 
- That is we need $$U'(0;1) > 0$$ to get fatalism?

Actually, looking at it some more, it seems like the interesting suff happens when $$\rho < 1$$:
- At $$\Psi = 0$$, $$N^*=+\infty$$
- When $$\Psi\in(=0,\rho)$$, the best response is finite, first plummetting and then rising again
- At $$\Psi \geq \rho$$, the best response again rises to $$+\infty$$

TODO?: Add a term for very very tiny non-contagion disaster risk?


#### What is the second derivative here?


#### What happens if we multiply $$u$$ by a constant?

Guess for later: equivalent to decreasing $$\rho$$.






# TODO for this page:
- [x] Copy over the properties of gamma distribution
- [ ] Find individual $$R_0$$ of a given type. (Mean number of spreads? Just NT, right?)
- [ ] Rewrite the PGFs for the case where types are a continuum instead of a discrete set.
    - Maybe look at the prelim solutions to help allieviate my confusion?
- [ ] Find utility function that makes this take on a nice form.
    - [ ] I think I have a text file somewhere with a note about the typical distribution of actual social connections. Find that and compare to the social connections induced in my model?
- [ ] Connect Schreiber model of Gamma Poisson spread to an indidivual's problem.

- [ ] Play around with the multiplicative $$U$$ some more. It looks like the threshold condition breaks down but maybe I flip a sign or something. (6-29 B)


