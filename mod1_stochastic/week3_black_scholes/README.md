# Weekly Summary

## 1. What did I model?
Built a Black-Scholes-Merton (BSM) pricer for European call and put options, and an implied volatility solver using Newton's method.

## 2. What is the key insight?

The BSM differential equation is a master equation — different boundary conditions produce different pricing formulas. This week I implemented the European call and put, which share the same structure but give opposite exposures: calls profit from upside, puts profit from downside.

The most important insight connecting back to [Weeks 1](../week1_gbm/README.md) and [2](../week2_binomial/README.md): **drift (μ) disappears entirely from BSM.** In the risk-neutral world, only the risk-free rate matters for pricing — not what the stock is expected to return. This held in the binomial tree and holds here in continuous time too.

Within the formula, N(d₂) is the probability the option expires in the money — i.e. the exercise will be profitable. N(d₁) is the option's delta — how much the option price moves per $1 move in the stock. This is the same delta from the Week 2 risk-less portfolio (0.25 shares), now expressed continuously.

BSM assumes constant volatility, continuous trading, and no dividends — simplifications that make the math tractable but break in the real world. Weeks 8-10 address what happens when these assumptions fail.

## 3. What do the codes do?

The [BSM pricer](bsm_sim.py) takes S₀, K, r, σ, T as inputs and outputs fair call and put prices. Put-call parity (C - P = S - Ke^{-rT}) is used as a verification check — if the relationship holds, the pricer is correct.

The [implied vol solver](implied_vol.py) inverts the BSM formula — given a market option price, it recovers the implied σ using Newton's method. The initial idea was to compute IV from both call and put prices and verify consistency via put-call parity. In practice, puts with low Vega caused Newton's method to diverge, so the solver uses call prices only. In production, one would either enforce parity by converting puts to synthetic calls, or use a more robust solver like bisection.

The [Python notebook](black_scholes_merton.ipynb) consolidates both of the codes above and added verifiers and additional information about BSM and its related concepts.

## 4. What surprised me?

The BSM formula looks intimidating but translates to roughly 35 lines of clean Python — the reading was harder than the coding, which was the opposite of Weeks 1 and 2. The put implied vol divergence was also unexpected — it showed that numerical methods have real limitations even when the math is theoretically sound.