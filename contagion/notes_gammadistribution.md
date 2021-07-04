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

    $$f(x)=\frac{x^{k-1} e^{-x/\theta}}{\theta^k\Gamma(k)}$$
- variance $$\sigma^2=k\theta^2=\mu^2/k$$
- cdf
  
    $$F(x;k,\mu) = {\gamma(k,\frac{k x}{\mu}) \over \Gamma(k)} = \frac{\int_0^{\frac{k x}{\mu}} t^{k-1} e^{-t} \; dt}{\int_0^\infty t^{k-1} e^{-t} \; dt}$$

Some additional helpful knowledge:

The pdf for gamma dist with $$k+1,\theta$$ is equal to the pdf for gamma dist with $$k,\theta$$ times $$\frac{x}{\theta k}$$

$$\sum_{k=0}^\infty \binom{k+(r-1)}{k} = \frac{1}{(1-px)^r}$$




























## Integrating over types instead of summing over types.

I need to stop using $$k$$ as subscript for a partiicular degree. How about little unidexed $$n$$?

The PGF for connections is PGF for connections: $$G_0(X)=\sum_{n=0}^\infty p_n x^n$$.

If there are multiple discrete types, with each type's connections being distributed according to iid Poisson process, then this PGF becomes: $$G_0(X)=\sum_{🍌=0}^\infty p_🍌 x^🍌 = \sum_i [A_i \sum_{🍌=0}^\infty \frac{N_i^🍌 e^{-N_i} x^🍌}{🍌!}] = \sum_i [ A_i e^{(x-1)N_i}]$$ because $$p_🍌 = \sum_i A_i Pr(n_i = 🍌 | N_i) = \sum_i A_i \frac{N_i^🍌 e^{-N_i}}{🍌!}$$.

If there are multiple discrete types, with each type's connections being distributed according to iid Poisson process, then this PGF becomes: $$G_0(X)=\sum_{n=0}^\infty p_n x^n = \sum_i [A_i \sum_{n=0}^\infty \frac{N_i^n e^{-N_i} x^n}{n!}] = \sum_i [ A_i e^{(x-1)N_i}]$$ because $$p_n = \sum_i A_i Pr(n_i = n | N_i) = \sum_i A_i \frac{N_i^n e^{-N_i}}{n!}$$.

Now instead we want to integrate across a continuum of types
- Instead of a discrete setof types like $$i\in\{H,L\}$$, we have a continuum $$i\in[0,1]$$
- Instead of $$A_i\equiv Pr(type=i)$$, now $$A_i \equiv f(i)$$, the pdf for type over the support $$(0,1)$$.

So now $$p_n = \int_i A_i Pr(n_i = n | N_i)$$....


From Schreiber. If each individual transmits poisson at individual rate $$v$$, and these $$v$$s are distributed with pdf $$f_v$$, then the PGF for offspring distribution is 

$$g(x)=\int_o^\infty e^{-v(1-x)}f_v(v)\ dv$$




## Here are the statistics facts I was confused about:

$$p_H(x)=\int p_F(x|\theta)p_G(\theta)\ d\theta$$

$$E[g(x)]=\int_x g(x)\ dF_x(x) = \int_x g(x) f_X(x)\ dx$$

If $$Y=g(X)$$ and $$X=h(Y)=g^{-1}(Y)$$, then 

$$f_Y(y) = f_x(h(y))\cdot abs(h'(y))$$



## Examples:

### Proportional response

Say that $$N\sim\Gamma(k,\theta)$$. And $$M=N\cdot A$$, where A is some positive constant.
So $$N=M/A$$

Then 

$$f_M(m)=f_N(m/A)\cdot (1/A) = (1/A) \frac{(m/A)^{k-1} e^{-m/A\theta}}{\theta^k\Gamma(k)} 
= \frac{m^{k-1} e^{-m/(A\theta)}}{(A\theta)^k\Gamma(k)} 
\sim \Gamma(k,A\theta)$$



### Everyone reduces connections by same amount 

Say that $$N\sim\Gamma(k,\theta)$$. And $$M=N - A$$, where A is some positive constant.
So $$N=M+A$$

$$f_M(m)=f_N(m+A) = \frac{(m+A)^{k-1} e^{-(m+A)/\theta}}{\theta^k\Gamma(k)}$$


### That weird thing I found yesterday

Say that $$N\sim\Gamma(k,\theta)$$. And $$M=  \frac{\ln(\Psi/\Theta)}{\Psi-\rho} = \frac{\ln(\Psi/\Theta)}{\Psi-\frac{\ln\Theta}{N}-1}$$.

Then $$N=h(M)\equiv\frac{\ln\Theta}{\Psi-1-\ln(\Psi/\theta)/M}$$ and $$h'(M)=\frac{\ln\Theta\ln(\Psi/\Theta)}{(\Psi M - M - \ln(\Psi/\Theta))^2}$$

But plugging this in doesn't seem to lead to anything too useful.

$$f_M(m)
= \frac{1}{\theta^k\Gamma(k)} (\frac{\ln\Theta}{\Psi-1-\ln(\Psi/\theta)/M})^{k-1} \exp(\frac{\ln\Theta /\theta}{\Psi-1-\ln(\Psi/\theta)/M}) \left|\frac{\ln\Theta\ln(\Psi/\Theta)}{(\Psi M - M - \ln(\Psi/\Theta))^2}\right|
$$




## Negative Binomial Distribution

If $$Z$$ is a negbinom distribution with mean $$R_0$$ and dispersion $$k$$, then its $$r$$ parameter is $$k$$ and its $$p$$ parameter is  $$p=(1+\frac{R_0}{k})^{-1} = \frac{k}{k+R_0}$$. Then $$q\equiv 1-p = (1+\frac{k}{R_o})^{-1} = \frac{R_0}{k+R_0}$$

Confusingly, if you consult wikipedia, and compare the above to the formula for $$\mu$$, you'll find that the $$p$$ referred to in Schreiber is called $$q$$ on wikipedia and vice versa. 


The pdf for this negbinom dist (using Schreiber's notation is 

$$f_Z(x) = \binom{x+r-1}{x}p^r (1-p)^x$$

Schreiber says that if we get the NB this way, then pgf for offspring is

$$g(x) = (1+\frac{R_0}{k}(1-x))^{-k}$$

If we take the pgf from wikipedia, and swap the ps and qs, $$pgf = (\frac{p}{1-(1-p)x})^r$$, then this agrees after a bit of simplification.



### Compare to how Newman does it.

Working directly from Newman, suppose that the number of conncetions itself is $$\sim NB(\mu_n,k)$$. Then

- PGF for neighbors is $$G_0(x) = (1+\frac{\mu_n}{k}(1-x))^{-k}$$
    - Take derivative to get $$G_0'(x) = \mu(1+\frac{\mu_n}{k}(1-x))^{-k-1}$$
- PGF for excess degree is $$G_1(x) = \frac{G_0'(x)}{G_0'(1)} = (1+\frac{\mu_n}{k}(1-x))^{-k-1}$$
    - Take derivative to get $$G_1'(x) = \frac{(1+r)\mu_n}{r}(1+\frac{\mu_n}{k}(1-x))^{-k-2}$$
- The critical threshold is $$T_c = \frac{1}{G_1'(1)} = \frac{k}{(1+k)\mu_n}$$
    - And $$R_0$$ = $$T/T_c = T\cdot\frac{(1+k)\mu_n}{k}$$
- PGF for open excess degree is $$G_1(x;T) = G_1(1-(1-x)T) = (1+\frac{\mu_n}{k}T(1-x))^{-k-1}$$
    - This is the pgf for the contagion offspring distribution. 
    - Notice that $$(1+\frac{1}{k}\cdot\mu_n T(1-x))^{-k-1} = (1+\frac{1}{k+1}\cdot\frac{k+1}{k}\mu_n T(1-x))^{-k-1}$$, 
        - meaning that if the distribution of neighbors is $$NB(\mu_n,k)$$, the contagion offspring distribution will be $$\sim NB(\mu_c,k+1)$$, where  $$\mu_c = \frac{k+1}{k}T\mu_n = R_0$$. *(+1 to dispersion, mean slightly higher than $$T\mu_n$$)*.
        - Likewise, if the contagion offspring distribution is $$\sim NB(R_0,k+1)$$, then that tells us that the neighbor distribution may be $$\sim NB(\mu_n,k)$$, where $$\mu_n = \frac{k}{k+1}\frac{R_0}{T}$$.
- Unprevelance found from solution to $$U=G_1(U;T)=(1+\frac{\mu_n}{k}T(1-U))^{-k-1}$$.
- In terms of $$\Psi=T-TU$$, this becomes $$\Psi=T- T G_1(U;T)=T - T(1+\frac{\mu_n}{k}\Psi)^{-k-1}$$. Let's rearrange it to make it the roots of a polynomial:

$${T-\Psi \over T} = (1+\frac{\mu_n}{k}\Psi)^{-k-1}$$

$${T \over T-\Psi} = (1+\frac{\mu_n}{k}\Psi)^{k+1}$$

$$0 = (1+\frac{\mu_n}{k}\Psi)^{k+1}\cdot(T-\Psi) - T$$









## If individuals choose poisson N_i, but the poisson N_i is gamma distributed.







## TODO Tomorrow:

- [ ] Try just plugging the proportional response thing in and seeing how that turns out.
    - [ ] Reverse engineer a utility function that makes that happen?
    - [ ] Look at what happens in equilibrium. Might lead to counterintuitive consequences for relationship between $$T$$ and $$\Psi$$ and $$R_\infty$$??

















---

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






# TODO for this page:
- [x] Copy over the properties of gamma distribution
- [ ] Find individual $$R_0$$ of a given type. (Mean number of spreads? Just NT, right?)
- [ ] Find utility function that makes this take on a nice form.
    - [ ] I think I have a text file somewhere with a note about the typical distribution of actual social connections. Find that and compare to the social connections induced in my model?
- [ ] Connect Schreiber model of Gamma Poisson spread to an indidivual's problem.

- [ ] Play around with the multiplicative $$U$$ some more. It looks like the threshold condition breaks down but maybe I flip a sign or something. (6-29 B)


- [ ] Maybe just fix the dispersion as a function of the disease and let the rate vary as a consumer response?

