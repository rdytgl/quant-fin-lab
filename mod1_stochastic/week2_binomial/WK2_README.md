# Weekly Summary
## 1. What did I model?
I created my first simulation for the one-step binomial tree model. Building from that code, I was able to build a two-step binomial tree model.

## 2. What is the key insight?
One key insight is that a risk-less portfolio must earn exactly the risk-free rate — no more, no less. If an option is mispriced, free money exists and arbitrageurs correct it immediately. This pins the option to exactly one fair price. Risk-neutral valuation then simplifies pricing further by replacing unknown real-world probabilities with risk-neutral probabilities, where everything earns the risk-free rate — giving us a known discount rate always.

## 3. What do/es the code/s do?
The [first code](one_step_bt_pricer.py) is the base code for the onestep binomial tree pricer. The [second code](two_step_bt_pricer.py) extends the one-step model to two steps, folding back from expiry to today twice using the same risk-neutral formula at each node.

## 4. What surprised me?
I finally understood what building a risk-less portfolio means in practice. By going long 0.25 shares and short one call option, the gains and losses offset each other perfectly regardless of where the stock goes. Any mispricing of the option breaks this balance and creates arbitrage — which is exactly why options have one specific fair price.