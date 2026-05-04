# Weekly Summary
## 1. What did I model?
An extended delta hedging simulation that runs across 1000 independent GBM paths, hedged at different rebalancing frequencies — biweekly, weekly, and daily.

## 2. What is the key insight?
**The hedge is fair on average**. Across 1000 paths, the mean P&L is near zero. This is the theoretical promise of BSM — the premium collected is the correct price for the hedge. The spread around zero is the hedging error introduced by discrete rebalancing.

**More frequent hedging tightens the distribution, not eliminates error**. Daily rehedging produces a narrower P&L distribution than weekly or biweekly. But in practice, every rebalance has transaction costs — continuous hedging is not free (also a learning from [Week 4](../week4_greeks/README.md)), and the optimal frequency is a tradeoff between hedging error and execution cost.

**Gamma predicts hedging difficulty, not hedging error perfectly**. Higher gamma paths tend to have larger absolute P&L errors — because gamma measures how fast delta changes, meaning weekly rebalances are always playing catch-up on high-gamma paths. But the scatter is wide because error also depends on the size and timing of moves along each path, not just average gamma.

## 3. What do the codes do?
1. Generates 1000 GBM paths (code from [GBM simulator](../mod1_stochastic/week1_gbm/gbm_simulator.py)) and runs a delta hedging simulation on each, tracking a single hedge account seeded with the BSM premium. At expiry, whatever remains in the account is the P&L for that path.
2. Plots the P&L distribution across all paths — centered near zero with a spread driven by discrete rebalancing error.
3. Reruns the simulation at three hedging frequencies and overlays the distributions — showing that daily hedging produces a tighter spread than weekly or biweekly.
4. Computes average gamma per path and scatterplots it against absolute P&L — showing a positive but noisy relationship.

## 4. What surprised me?
The hedge account framing was a cleaner mental model than tracking gross share costs. Seeding the account with the BSM premium and watching it fluctuate through rebalancing — then return near zero at expiry — made the whole mechanism click in a way the table alone did not.

The gamma-P&L scatter not being a clean line was also instructive. It is easy to assume one Greek explains everything, but the actual error depends on when big moves happen, not just how sensitive delta is on average. Greeks are local — they describe the current moment, not the full path.

The connection to Week 4 is now clearer too: delta tells me where to hedge, gamma tells me how hard it will be to stay hedged.