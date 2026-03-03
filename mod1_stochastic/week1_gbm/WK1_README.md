# Weekly Summary
## 1. What did I model?
I created my first GBM simulation, first on Excel on a single path then 100 paths, then eventually translated into Python. Added a separate model that checks for different values of mu and sigma and how it changes the shape of the plot.

## 2. What is the key insight?
The sigma effect is much more dramatic than the mu effect. A high mu just shifts the cone upward slightly. A high sigma absolutely explodes the spread of outcomes, although not as evident in the plots, it does get a wider range of possibilities. With a 1.00 sigma, the prices could reach 2000, a 2000% increase to the initial price although only briefly

## 3. What do/es the code/s do?
The [first code](quant-fin-lab/mod1_stochastic/week1_gbm/gbm_simulator.py) simulates 1000 paths of an asset price starting at 100 with an annualised drift of 0.10 and annualised volatilty of 0.20.

Using the base code, the [second code](quant-fin-lab/mod1_stochastic/week1_gbm/gbm_simulator_scenarios.py) checks for how the different sigma and mu values affect the shape of the plot cone.

## 4. What surprised me?