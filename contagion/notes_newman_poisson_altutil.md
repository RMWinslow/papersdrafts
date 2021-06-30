
# Trying to find a convinient form for the utility function.

In the Newman+Poisson case, each individual takes $$\Psi\in[0,1]$$ for granted and chooses $$N\in\R_+$$ as their connection rate to maximize $$U(N;\Psi)=u(N)-p(N;\Psi)$$ where $$p(N;\Psi)=1-e^{-\Psi N}$$.

I would like to choose a utility function such that the following properties hold:
- **Nice form:** The best response $$N^*(\Psi)$$ takes a nice analytic form and can be easily adjusted based on some parameter.
- **FOC works:** U is concave down, so that I can use FOCs to find this best response.
    - This means that not only do we need diminishing marginal utility of connection, but it must be extreme enough to counterbalance the diminishing marginal cost of connection.
- **Bounded connections:** Even in the absence of a contagion, the best response is finite.
- **Gumption:** If $$\Psi=1$$ then the best response is nonetheless *not* $$N=0$$. Even at the most extreme, the agents (or at least some of them) don't want to just cut off all contact completely.
    - Ideally, they return right back to the same level of social connection as at $$\Psi=0$$ 

## Let utility be negative exponential

$$u(N) = -\frac{\theta}{\rho} e^{-\rho N}$$

$$U(N;\Psi,\delta) = -\frac{\theta}{\rho} e^{-\rho N} - \delta[1- e^{-\Psi N}]$$

- Paramater domains: $$\rho,\delta,\theta\in(0,\infty)$$, $$\Psi\in[0,1]$$, $$N_{BR} \in [0,\infty)$$
- Marginal utility: $$\frac{d}{dN}U = \theta e^{-\rho N} - \delta \Psi e^{-\Psi N}$$
    - Where FOC  is appropriate, it resolves to the single critical point $$N^* = \frac{\ln(\delta\Psi/\theta)}{\Psi-\rho}$$
    - Because $$U'$$ is continuous, this point exists iff both $$\Psi\neq 0$$ and $$\Psi\neq\rho$$
    - Whenever it exists, it is the only critical point, and thus at least one of $$N^*,\infty,0$$ are the best response.
        - If it's a local maximixa, then $$N_{BR}=N^*$$
    - When it doesn't exist, or when its a local minima, the function is monotonic or constant and thus at least one of $$0,\infty$$ maximizes utility.
- Second derivative: $$\frac{d}{dN}\frac{d}{dN}U =  - \theta\rho e^{-\rho N} + \delta \Psi^2 e^{-\Psi N}$$
    - If the critical point $$N^*$$ exists, then $$U''(N^*) = [\Psi-\rho] \cdot (\delta\Psi)^{\frac{-\rho}{\Phi-\rho}}\theta^{\frac{\Psi}{\Phi-\rho}}$$.
    - Thus if $$\Psi > \rho$$, $$N^*$$ is a local minima, and the optimum is at the boundaries.
    - If $$
- Cross derivative: $$\frac{d}{d\Psi}\frac{d}{dN}U = \delta e^{-\Psi N}[\Psi N -1]$$, 
    - giving us the standard $$N=\frac{1}{\Psi}$$, $$p(N;\Psi)=1-\frac{1}{e}$$ fatalism threshold when the FOC is valid.

To reiterate conditions for optimum (See paper notes [6-30 D+] for flowchart):
- If $$\Psi = 0$$: then $$N_{BR}=+\infty$$
- If $$\Psi\in(0,\rho)$$: 
    - If $$\delta\Psi \geq \theta$$: then  $$N_{BR}=0$$
    - If $$\delta\Psi \leq \theta$$: then  $$N_{BR}=N^*=N^* = \frac{\ln(\delta\Psi/\theta)}{\Psi-\rho}$$
- If $$\Psi\geq\rho$$: 
    - If $$\delta < {\theta\over\rho}$$: then  $$N_{BR}=+\infty$$
    - If $$\delta = {\theta\over\rho}$$: then  there are multiple optima, includeing $$N=0$$ and $$N=+\infty$$.
    - If $$\delta > {\theta\over\rho}$$: then  $$N_{BR}=0$$



Now which of my desired properties does this utility have?
- [x] Nice Form
- [x] FOC Works
    - Kinda. The function isn't convex or concave, but it does have at most one critical point, which is all I actually need I think. As long as $$\Psi\in(0,\rho)$$ and $$\delta\Psi < \theta$$, the optimum is at that critical point.
- [ ] Bounded Connections
    - Alas, no
- [x] Gumption
    - Depends on parameters. But as long as $$\delta < \frac{\theta}{\rho}$$, the best response goes to infinity as $$\Psi\to1$$.


---

---

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



