
# Trying to find a convinient form for the utility function.

In the Newman+Poisson case, each individual takes $$\Psi\in[0,1]$$ for granted and chooses $$N\in\R_+$$ as their connection rate to maximize $$U(N;\Psi)=u(N)-p(N;\Psi)$$ where $$p(N;\Psi)=1-e^{-\Psi N}$$.

I would like to choose a utility function such that the following properties hold:
- **Nice form:** The best response $$N^*(\Psi)$$ takes a nice analytic form and can be easily adjusted based on some parameter.
- **FOC works:** U is concave down, so that I can use FOCs to find this best response.
    - This means that not only do we need diminishing marginal utility of connection, but it must be extreme enough to counterbalance the diminishing marginal cost of connection.
- **Bounded connections:** Even in the absence of a contagion, the best response is finite.
- **Gumption:** If $$\Psi=1$$ then the best response is nonetheless *not* $$N=0$$. Even at the most extreme, the agents (or at least some of them) don't want to just cut off all contact completely.
    - Ideally, they return right back to the same level of social connection as at $$\Psi=0$$
- **Elasticity:** I wan the response to increasing contact risk to be big enough to easiy see on a graph.




## Let utility be negative exponential

$$u(N) = -\frac{\theta}{\rho} e^{-\rho N}$$

$$U(N;\Psi,\delta) = -\frac{\theta}{\rho} e^{-\rho N} - \delta[1- e^{-\Psi N}]$$

- Paramater domains: $$\rho,\delta,\theta\in(0,\infty)$$, $$\Psi\in[0,1]$$, $$N_{BR} \in [0,\infty)$$
- Marginal utility: $$\frac{d}{dN}U = \theta e^{-\rho N} - \delta \Psi e^{-\Psi N}$$
    - Where FOC  is appropriate, it resolves to the single critical point $$N^* = \frac{\ln(\delta\Psi/\theta)}{\Psi-\rho}$$
        - At this point, probability of infection is $$1-e^{-\psi N^*} = 1-\left[{\delta\Psi\over\theta}\right]^{-\Psi/(\Psi-\rho)}$$
    - Because $$U'$$ is continuous, this point exists iff both $$\Psi\neq 0$$ and $$\Psi\neq\rho$$
    - Whenever it exists, it is the only critical point, and thus at least one of $$N^*,\infty,0$$ are the best response.
        - If it's a local maximixa, then $$N_{BR}=N^*$$
    - When it doesn't exist, or when its a local minima, the function is monotonic or constant and thus at least one of $$0,\infty$$ maximizes utility.
- Second derivative: $$\frac{d}{dN}\frac{d}{dN}U =  - \theta\rho e^{-\rho N} + \delta \Psi^2 e^{-\Psi N}$$
    - If the critical point $$N^*$$ exists, then $$U''(N^*) = [\Psi-\rho] \cdot (\delta\Psi)^{\frac{-\rho}{\Phi-\rho}}\theta^{\frac{\Psi}{\Phi-\rho}}$$.
    - Thus if $$\Psi > \rho$$, $$N^*$$ is a local minima, and the optimum is at the boundaries.
    - If $$\rho < \Psi$$, then the $$N^*$$ is a local maxima and thus the optimum.
- Cross derivative: $$\frac{d}{d\Psi}\frac{d}{dN}U = \delta e^{-\Psi N}[\Psi N -1]$$, 
    - giving us the standard $$N=\frac{1}{\Psi}$$, $$p(N;\Psi)=1-\frac{1}{e}$$ fatalism threshold when the FOC is valid.
    - For the critical point to be at this threshold, it must be that $$1-\frac{\rho}{\Psi}=\ln(\frac{d\Psi}{\rho})$$.

To reiterate conditions for optimum (See paper notes [6-30 D+] for flowchart):
- If $$\Psi = 0$$: then $$N_{BR}=+\infty$$
- If $$\Psi\in(0,\rho)$$: 
    - If $$\delta\Psi \geq \theta$$: then  $$N_{BR}=0$$
    - If $$\delta\Psi \leq \theta$$: then  $$N_{BR}=N^*=N^* = \frac{\ln(\delta\Psi/\theta)}{\Psi-\rho}$$
- If $$\Psi\geq\rho$$: 
    - If $$\delta < {\theta\over\rho}$$: then  $$N_{BR}=+\infty$$
    - If $$\delta = {\theta\over\rho}$$: then  there are multiple optima, includeing $$N=0$$ and $$N=+\infty$$.
    - If $$\delta > {\theta\over\rho}$$: then  $$N_{BR}=0$$

Sufficient conditions for $$N_{BR}=N^*$$: $$\Psi\neq0$$ and $$\delta < \theta$$.
- If $$\delta > \theta$$ and $$\rho < \frac{\theta}{\delta}$$,then the optimum will initially shrink and then pop back up to infinity asymptotically at $$\Psi\geq\rho$$
- If $$\delta > \theta$$ and $$\rho > \frac{\theta}{\delta}$$, then the optimum will initially shrink, but then get 'stuck' at $$N=0$$ when $$\Psi$$ goes to $$\theta\over\delta$$ 
- If $$\delta = \theta$$ and $$\rho < 1$$,then the optimum will initially shrink and then pop back up to infinity asymptotically at $$\Psi\geq\rho$$
- If $$\delta = \theta$$ and $$\rho \geq 1$$,then the optimum will initially shrink and then get stuck at $$N=0$$ as $$\Psi\to1$$.
- If $$\delta < \theta$$ and $$\rho \leq 1$$,then the optimum will initially shrink and then pop back up to infinity asymptotically at $$\Psi\geq\rho$$
- If $$\delta < \theta$$ and $$\rho > 1$$,then the optimum will be positive for all $$\Psi\in(0,1]$$, 
    - but will the person ever hit the fatalism threshold and start ramping up their connections? We can check by evaluating $$\frac{d}{d\Psi} N^* = \frac{1-\frac{\rho}{\Psi}-\ln(\frac{\delta\Psi}{\theta})}{(\Psi-\rho)^2}$$ at $$\Psi=1$$
    - The denom is always positive and the numer evaluates to $$1-p-\ln(\delta/\theta)$$, so 
    - If  $$\delta < \theta$$, $$\rho > 1$$, and $$(\rho-1) < \ln(\theta/\delta)$$, then the optimum dips down and then rises back up.
    - If  $$\delta < \theta$$, $$\rho > 1$$, and $$(\rho-1) > \ln(\theta/\delta)$$, then the optimum continually falls as $$\Psi$$ increases to 1.

Now which of my desired properties does this utility have?
- [x] Nice Form
- [x] FOC Works
    - Kinda. The function isn't convex or concave, but it does have at most one critical point, which is all I actually need I think. As long as $$\Psi\in(0,\rho)$$ and $$\delta\Psi < \theta$$, the optimum is at that critical point.
- [ ] Bounded Connections
    - Alas, no. Especially not at 0.
- [x] Gumption
    - Depends on parameters. But as long as $$\delta < \frac{\theta}{\rho}$$, the best response goes to infinity as $$\Psi\to1$$.
- [x] Elasticity

### Inducing specific values.

Sadly, $$N_{BR}=\infty$$ in the absence of a contagion.
But good news, I can easily choose parameters to make it such that the person choose a specific number of connections in the extreme case where $$\Psi=1$$:
- When $$\Psi=1$$, if $$\rho > 1$$, $$N_{BR}=N^*=\frac{\ln(\delta/\theta)}{1-p} = \frac{\ln(\theta/\delta)}{p-1}$$. 
- Solve for $$\theta/\delta$$ to get $$\frac{\theta}{\delta}=e^{(\rho-1)N^*}$$
- So to get parameters such that $$N^*(\Psi=1)=N_i$$:
    - pick any $$🍌 > 1$$, 
    - set $$\rho=\ln(🍌)+1$$ (Or choose $$🍌=e^{\rho-1}$$)
    - set $$\theta = \delta 🍌^{N_i}$$
        - For simplicity, you can normalize $$\delta=1$$. This degree of freedom was changing the utility but not the best response function.
- Then with these paramaters, the level of $$\Psi$$ point at which the person starts to become fatalistic is found by solving $$1-\frac{\rho}{\Psi}=\ln(\delta\Psi/\theta)$$ which becomes $$1-\frac{\ln(🍌)+1}{\Psi}=ln(\Psi/🍌^{N_i})$$
    - This becomes $$e^{1+\rho N - N} = \Psi e^{\rho/\Psi}$$
    - PLugging this into wolfram, with $$0 < \Psi < 1$$ and $$LHS > e^\rho$$ gets me the solution $$\Psi = \frac{-\rho}{W_{-1}(\frac{-\rho}{ee^{\rho N-N}})}$$, where $$W^{-1}$$ is a branch of the Lambert product log doohicky.
    - Sadly, I can't solve better than that. But I can say that as $$N_i$$ increases, the threshold $$\Psi$$  starts at 0, decays quickly, then continues to decay but more slowly.
- The condition for rising but finite optimum as $$\Psi\to1$$ becomes $$🍌>1$$ and $$\ln(🍌) > \ln (🍌^{N_i})$$, which implies $$N_i > 1$$. 





# TODO: 
- [] Add a term for very very tiny non-contagion disaster risk? Hopefully it lets me put $$\rho$$ below 1 without too much hassle?




