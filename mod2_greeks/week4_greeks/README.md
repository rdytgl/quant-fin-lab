# Weekly Summary
## 1. What did I model?
This week I modeled the four major options Greeks — delta, gamma, theta, and vega — and visualized how each behaves across a range of stock prices. I then built a delta hedging simulation table for call options, replicating Hull’s Table 19.2, to see how a trader dynamically rebalances a position week by week to maintain delta neutrality.

## 2. What is the key insight?
**Delta** measures how much the option price moves for every $1 change in the stock price. For calls it ranges from 0 to 1, and for puts from -1 to 0. The goal of delta hedging is to keep the total position delta at zero — meaning small stock moves don’t affect your net position. Being long an option means you own the convexity; being short means you owe it.

**Gamma** is the rate of change of delta. A high gamma means delta is shifting rapidly, which means your hedge needs frequent rebalancing. A low gamma means you can afford to rebalance less often. This is the most practical Greek for a delta hedger — it tells you how unstable your hedge is at any given moment.

**Theta** is time decay — the option loses value simply from time passing. Theta and gamma have an inverse relationship: when you are long gamma you are paying for it through theta bleed every day. You can’t have the upside of gamma without the daily cost of theta.

**Vega** measures sensitivity to implied volatility. A high vega means the option price moves significantly when volatility shifts — which connects directly back to the implied volatility work from Week 3.

One observation that only became clear from the plots: gamma, theta, and vega all peak at the money. ATM options are the most sensitive to everything — price moves, time, and volatility. Deep ITM or OTM options are relatively inert. Also, gamma and vega are identical for calls and puts with the same inputs — only delta and theta differ between the two, which is put-call parity showing up in the Greeks.

Continuous delta hedging costs exactly the BSM premium in total, regardless of which direction the stock moves. The delta hedging table demonstrates this — whether the option expires ITM or OTM, the cumulative hedging cost converges toward the BSM theoretical price. The remaining gap comes from hedging weekly rather than continuously, and from real transaction costs that BSM doesn’t account for.

## 3. What do the codes do?
The [Greeks Visualizer](greek_viz.py) plots delta, gamma, theta, and vega against a range of stock prices from 50% to 150% of the initial price, with the strike marked on each plot. The [Delta Hedging Table](delta_hedge.py) simulates a GBM stock path over n weeks, computes the delta hedge at each step using N(d₁), and tracks shares purchased, cost, cumulative cost, and interest — producing a full replication of Hull’s hedging cost table for both ITM and OTM scenarios.

## 4. What surprised me?
I accidentally proved BSM convergence before I even finished the table. I was trying random inputs to force a delta→1 scenario and one run produced a hedging cost almost identical to the BSM price — with completely different parameters and a stock that ended deep OTM. That was the moment Hull’s entire argument clicked, and the math proved the original premise of the readings from Hull.