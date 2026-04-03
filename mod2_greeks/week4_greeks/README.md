# Weekly Summary

## 1. What did I model?
Built a Black-Scholes-Merton (BSM) pricer for European call and put options, and an implied volatility solver using Newton's method.

## 2. What is the key insight?
// clean these:
1. delta: how much the option price changes for every small change in stock price; measures instantaneous changes only
    a. very important here: delta of options can range between 1 to -1; usually 0 to 1 is for call options and -1 to 0 for put; but we are aiming for delta-zero or delta neutral for the stock position
    b. long vs short: long is holding that option; short is selling that contract to someone else. long trades mean you own the convexity (in gamma), and short trades mean you owe it. simply, long trades mean you benefit from the movement of the option, and shorts is the other side of it
    c. the cost difference between BSM and using a delta hedge: the ideal is continuous trade--> but that trade can reach infinity quickly (esp when done instantaneously and continuously). since it is like holding long positions, the stocks can go in different directions, hence affecting the total option cost. 

## 3. What do the codes do?

The [BSM pricer](bsm_sim.py) takes S₀, K, r, σ, T as inputs and outputs fair call and put prices. Put-call parity (C - P = S - Ke^{-rT}) is used as a verification check — if the relationship holds, the pricer is correct.

The [implied vol solver](implied_vol.py) inverts the BSM formula — given a market option price, it recovers the implied σ using Newton's method. The initial idea was to compute IV from both call and put prices and verify consistency via put-call parity. In practice, puts with low Vega caused Newton's method to diverge, so the solver uses call prices only. In production, one would either enforce parity by converting puts to synthetic calls, or use a more robust solver like bisection.

The [Python notebook](black_scholes_merton.ipynb) consolidates both of the codes above and added verifiers and additional information about BSM and its related concepts.

## 4. What surprised me?

The BSM formula looks intimidating but translates to roughly 35 lines of clean Python — the reading was harder than the coding, which was the opposite of Weeks 1 and 2. The put implied vol divergence was also unexpected — it showed that numerical methods have real limitations even when the math is theoretically sound.