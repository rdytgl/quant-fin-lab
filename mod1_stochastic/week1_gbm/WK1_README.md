# Weekly Summary
## 1. What did I model?
I created my first GBM simulation, first on Excel on a single path then 100 paths, then eventually translated into Python. Added a separate model that checks for different values of mu and sigma and how it changes the shape of the plot.

## 2. What is the key insight?
The sigma effect is much more dramatic than the mu effect. A high mu just shifts the cone upward slightly. A high sigma absolutely explodes the spread of outcomes, although not as evident in the plots, it does get a wider range of possibilities. With a 1.00 sigma, the prices could reach 2000, a 2000% increase to the initial price although only briefly.

Analysing the final asset prices, I also saw that the final price distribution of 1000 simulated paths show a right skew, but when taking the log of the final prices, it transforms the distribution into a normal one. I was actually able to observe this with an increased sigma (0.60 instead of 0.20) and by extending the time horizon to 2 years.

Eventually I will get to check Ito's Lemma but for now I wanted to see what it even does, and with the [third code](gbm_sim_no_itos_lemma.py), it shows that the mean asset price is shifting higher than the expected mean price using the $s_0 * e^(\mu T)$

## 3. What do/es the code/s do?
The [first code](gbm_simulator.py) simulates 1000 paths of an asset price starting at 100 with an annualised drift of 0.10 and annualised volatility of 0.20. I then edited this same code to analyse the final prices across the 1000 paths comparing raw price distribution against log-transformed prices.

Using the base code, the [second code](gbm_simulator_scenarios.py) checks for how the different sigma and mu values affect the shape of the plot cone.

## 4. What surprised me?
While exponential growth wasn’t a new concept to me, seeing the lognormal-to-normal transformation in my own simulation made it click differently. Asset prices can’t go negative but have theoretically infinite upside — the lognormal distribution captures exactly that asymmetry, and taking the log recovers the familiar normal distribution underneath.