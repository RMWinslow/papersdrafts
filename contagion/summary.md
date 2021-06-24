---
title: Contagion Summary
---

I'm playing around with combining 
the graph-theory-based description of epidemics 
from [Newman 2002](https://journals.aps.org/pre/pdf/10.1103/PhysRevE.66.016128)
with a simple behavioral equilibrium, 
as in [Kremer 1996](https://academic.oup.com/qje/article-pdf/111/2/549/5460782/111-2-549.pdf).

Given parameters for a contagion, individual people choose some measure of connectivity with other people. The parameters for contagion and individual choice together are in equilibrium if the following two conditions are met:

- **The behavioral condition**: Taking the contagion parameters as given, and acting as if their behavior has no effect on aggregate patterns of disease spread, each person chooses the connectivity that makes them individually best off.
- **The epidemiological condition**: The contagion parameters are consistent with the decisions that people are making.



## Notes so far:

### [Singular degree distributions](notes_newman_singular)

Here, I'm assuming that there are only one type of people, and each type of person chooses a specific number of connections to have.

Most of the notes on the page are just following Newman through a simple example. 
But there are some interesting graphs. 
Depending on how much people care about social connections and how contagious the disease is, you can end up in situations where:

- Everyone would be better off if everyone chose to have fewer connections, but each individual is happiest with more connections, and so the epidemic happens anyways.
- People individually reduce connections for a mildly transmissible epidemic but not a highly transmissible one.
    - And this behavior can be either societally optimal or suboptimal depending on the severity of the disease.
- It is individually optimal to reduce connections if and only iff everyone else does, leading to multiple equilibria.
- It is individually optimal to reduce connections if and only iff nobody else does, leading to a lack of equilibria (just a consequence of everyone being identical)


### [Two types of people, each with singular degree](notes_newman_twotype)

This is the same as the above, except that there are two types of people, each of which has different preferences over connections and thus chooses a different amount of connections.


### [Multiple types of people who imperfectly choose their degree](notes_newman_poisson)

Here, each type $$i$$ chooses the number of connections $$N_i$$ they want, but the actual number of connections they make is determined by a Poisson process with mean $$N_i$$. The averages work out to be the same as in the previous case, but this smooths things out and hopefully removes the ugly discontinuities when I go to graph it.
