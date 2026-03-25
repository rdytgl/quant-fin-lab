# Weekly Summary
## 1. What did I model?
* bsm pricer
* implied volatility using newton's method

## 2. What is the key insight?
* The BSM differential equation is a master equation that can produce a family of pricing formulas depending on the boundary conditions applied. This week I implemented the European call and put formulas, as well as the american call (same as the european call)
* In the BSM formula, the drift (mu) disappears completely, confirming the learnings from [week 1](../week1_gbm/README.md) and [week 2](../week2_binomial/README.md) that only the risk-free rate matters, not the expected return of the stock
* in bsm, there are a few assumptions (constant volatility, constant checking, non-dividend paying, continuous trading). this makes the pricer created not the most robust but can introduce the idea of pricing using BSM
* N(d2) is the probability that the option "expires in the money" i.e.: the exercise of the option will earn money
* N(d1) is the "delta of the option" i.e.: how much the option moves for every $1 move in the stock

## 3. What do/es the code/s do?
The [first code](bsm_sim.py) allows input of the various variables to compute call and put prices.

## 4. What surprised me?
* the use of the put-call parity relationship as a verification tool
* this code was easier than the reading, which was the opposite from the previous weeks
* that N(d1) is just the delta
