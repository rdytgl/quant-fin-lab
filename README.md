# 🧠 Quantitative Finance Lab
---
I’m a recent graduate with a background in coding and operations research, transitioning into quantitative finance. My strength is implementation — so this repo leans heavily on building first and deriving later. In the coming weeks, I intend to build simulations and learning not just financial concepts but also how quantitative methods come into play here as well.

Each week contains the following:
1. Python implementation
2. Jupyter notebook with plots and analysis
3. Personal notes on what clicked and what didn’t

---

![Status](https://img.shields.io/badge/Currently_On-Week_4_Greeks-blue)
![Progress](https://img.shields.io/badge/Progress-4%2F12_Weeks-green)

---

## 📦 MODULE 1 — Stochastic Foundations (Weeks 1–3)

Goal: Understand how markets are modeled before pricing anything.

---

## [Week 1 — Geometric Brownian Motion](mod1_stochastic/week1_gbm/)

### Concepts
- Random walks
- Wiener process
- Log returns vs arithmetic returns
- Drift vs volatility
- Lognormal distribution

### Build
- GBM simulator
- Distribution analysis
- Sensitivity to sigma
- Compare arithmetic vs log returns

---

## [Week 2 — No-Arbitrage & Risk-Neutral Pricing](mod1_stochastic/week2_binomial/)

### Concepts
- Arbitrage logic
- Replication
- Risk-neutral valuation
- Why drift disappears in pricing

### Build
- One-step binomial pricer
- Multi-step binomial tree
- Convergence to Black–Scholes

---

## [Week 3 — Black–Scholes Intuition](mod1_stochastic/week3_black_scholes/)

### Concepts
- Dynamic hedging
- Delta replication
- Risk-neutral world
- Implied volatility

### Build
- Black–Scholes pricer
- Implied volatility solver (Newton method)

---

## 📦 MODULE 2 — Risk & Greeks (Weeks 4–6)

Goal: Think like a risk manager.

---

## Week 4 — Greeks

### Concepts
- Delta
- Gamma
- Vega
- Theta
- Portfolio sensitivities

### Build
- Numerical Greeks (finite differences)
- Plot Greeks vs underlying price
- Portfolio Greeks calculator

---

## Week 5 — Dynamic Hedging Simulation

### Concepts
- Discrete hedging error
- Model vs reality
- P&L distribution

### Build
- Simulate delta hedging across GBM paths
- Plot hedging P&L distribution
- Study effect of hedging frequency

---

## Week 6 — Volatility Estimation

### Concepts
- Historical volatility
- EWMA
- GARCH (intuitive understanding)
- Realized vs implied volatility
### Build
- Estimate historical volatility from market data
- Compare historical vs implied volatility
- Implement simple EWMA model

---

## 📦 MODULE 3 — Advanced Simulation (Weeks 7–12)

Goal: Move from textbook models to computational depth.

---

## Week 7 — Monte Carlo Pricing

### Build
- Monte Carlo pricer
- Antithetic variates experiment
- Compare MC vs Black–Scholes

---

## Week 8 — Volatility Smile

### Build
- Extract implied vol across strikes
- Plot volatility smile

---

## Weeks 9–10 — Stochastic Volatility Intro

### Concepts
- Why constant volatility fails
- Volatility clustering
- Mean reversion

### Build
- Simulate simple stochastic volatility model
- Compare to GBM
- Observe volatility clustering

---

## Weeks 11–12 — Mini Project

**To be determined based on what interests me most by Week 10.**
