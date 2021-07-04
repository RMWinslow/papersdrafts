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

If $$Z$$ is a negbinom distribution with mean $$R_0$$ and dispersion $$k$$, then its $$r$$ parameter is $$k$$ and its $$q$$ parameter is $$R_0 \over k+R_0$$. $$p=(1+\frac{R_0}{k})^{-1}$$

The pdf for this negbinom dist is 

$$f_Z(x) = \binom{x+r-1}{x}(1-p)^rp^x$$

Schreiber says that if we get the NB this way, then pgf for offspring is

$$g(x) = (1+\frac{R_0}{k}(1-x))^{-1}$$

Compare with Newman, where pgf for offspring is $$G_1(x;T)$$ and  $$R_0$$ works out to be $$T\cdot G_1'(1)$$  or $$T\frac{E[k^2]-E[k]}{E[k]}$$.

We get the per-edge risk from $$\Psi=(U-1)T$$, and $$U=G_1(U;T)$$.
So this means combining the above we get

$$G_1(x;T) = g(x) = (1+\frac{R_0}{k}(1-x))^{-1} = (1+\frac{G_1'(1)}{k}T(1-x))^{-1}$$

And I think this means that because $$G_1(x;T)=G_1(1-T(1-x))$$, that

$$G_1(x) = (1+\frac{G_1'(1)}{k}(1-x))^{-1} = (1+\frac{1}{kT_c}(1-x))^{-1}$$

Note that this itself seems to be the pgf for a negbinom distribution with $$r=k$$ and mean $$1/T_c$$






$$U = G(U;T) = g(x) = (1+\frac{R_0}{k}(1-U))^{-1} \\
= (1-\frac{G_1'(1)}{k}T(U-1))^{-1} \\
= (1-\frac{1}{kT_c}\Psi)^{-1} $$

$$1+\Psi/T = \frac{\Psi+T}{T} =  \frac{1}{1-\frac{1}{kT_c}\Psi}$$

$$(\Psi+T)(1-\frac{1}{kT_c}\Psi) = T$$










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

