## Goal
- Want to find a utility function such that the optimal response to contagion risk in the Newman+Poisson case has a nice analytical solution
- Use this to force the distribution of connections to be distributed according to a gamma distribution so that the offspring distribution becomes Negative Binomial.
- Connect to the Schreiber Paper


## Gamma distribution facts











## Integrating over types instead of summing over types.

I need to stop using $$k$$ as subscript for a partiicular degree. How about little unidexed $$n$$?

The PGF for connections is PGF for connections: $$G_0(X)=\sum_{n=0}^\infty p_n x^n$$.

If there are multiple discrete types, with each type's connections being distributed according to iid Poisson process, then this PGF becomes: $$G_0(X)=\sum_{🍌=0}^\infty p_🍌 x^🍌 = \sum_i [A_i \sum_{🍌=0}^\infty \frac{N_i^🍌 e^{-N_i} x^🍌}{🍌!}] = \sum_i [ A_i e^{(x-1)N_i}]$$ because $$p_🍌 = \sum_i A_i Pr(n_i = 🍌 | N_i) = \sum_i A_i \frac{N_i^🍌 e^{-N_i}}{🍌!}$$.

If there are multiple discrete types, with each type's connections being distributed according to iid Poisson process, then this PGF becomes: $$G_0(X)=\sum_{n=0}^\infty p_n x^n = \sum_i [A_i \sum_{n=0}^\infty \frac{N_i^n e^{-N_i} x^n}{n!}] = \sum_i [ A_i e^{(x-1)N_i}]$$ because $$p_n = \sum_i A_i Pr(n_i = n | N_i) = \sum_i A_i \frac{N_i^n e^{-N_i}}{n!}$$.

Now instead we want to integrate across a continuum of types
- Instead of a discrete setof types like $$i\in\{H,L\}$$, we have a continuum $$i\in[0,1]$$
- Instead of $$A_i\equiv Pr(type=i)$$, now $$A_i \equiv f(i)$$, the pdf for type over the support $$(0,1)$$.

So now $$p_n = \int_i A_i Pr(n_i = n | N_i)$$ 












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










# TODO for this page:
- [ ] Copy over the properties of gamma distribution
- [ ] Find individual $$R_0$$ of a given type. (Mean number of spreads? Just NT, right?)
- [ ] Find utility function that makes this take on a nice form.
    - [ ] I think I have a text file somewhere with a note about the typical distribution of actual social connections. Find that and compare to the social connections induced in my model?
- [ ] Connect Schreiber model of Gamma Poisson spread to an indidivual's problem.




