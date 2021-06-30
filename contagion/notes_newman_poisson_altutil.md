
# Trying to find a convinient form for the utility function.

In the Newman+Poisson case, each individual takes $$\Psi\in[0,1]$$ for granted and chooses $$N\in\R_+$$ as their connection rate to maximize $$U(N;\Psi)=u(N)-p(N;\Psi)$$ where $$p(N;\Psi)=1-e^{-\Psi N}$$.

I would like to choose a utility function such that the following properties hold:
- The best response $$N^*(\Psi)$$ takes a nice analytic form and can be easily adjusted based on some parameter.
- U is concave down, so that I can use FOCs to find this best response.
- In the absence of a contagion, the best response is finite.
- If $$\Psi=1$$ then the best response is nonetheless *not* $$N=0$$. Even at the most extreme, the agents (or at least some of them) don't want to just cut off all contact completely. 

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

$$\frac{d}{d\Psi} \frac{d}{dN} U(N) = \frac{d}{d\Psi}[e^{-\rho N} - \Psi e^{-\Psi N}] \\
= $$


#### What happens if we multiply $$u$$ by a constant?

Guess for later: equivalent to decreasing $$\rho$$.



