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
* learned some jargon like ATM/ITM/OTM
* in implied_vol, vega needs the value of the PDF as it is looking at the sensitivity of the probability of stock to small changes

Initial idea for the code was to compute implied volatility using both call and put prices and verify consistency via put-call parity: C - P = S - K * exp(-rT)
In theory, both call and put should yield the same implied volatility if prices are arbitrage-free.
However, in practice:
  - Small numerical inconsistencies (rounding, input errors) can break parity
  - Deep OTM/ITM options (especially puts) have very low Vega, making Newton method unstable
  - This can lead to unreliable or divergent implied volatility estimates for puts

For stability and simplicity, we compute [implied volatility](implied_vol.py) using the call price only.
In production settings, one would:
  - enforce parity (convert put → synthetic call), or
  - use a more robust solver (e.g., bisection with bounds)

## 3. What do/es the code/s do?
The [first code](bsm_sim.py) allows input of the various variables to compute call and put prices.

## 4. What surprised me?
