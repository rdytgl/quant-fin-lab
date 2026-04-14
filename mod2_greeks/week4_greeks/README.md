# Weekly Summary

## 1. What did I model?

## 2. What is the key insight?
// clean these:
// insert formulas and explanations for the ipynb
1. delta: how much the option price changes for every small change in stock price; measures instantaneous changes only
    a. very important here: delta of options can range between 1 to -1; usually 0 to 1 is for call options and -1 to 0 for put; but we are aiming for delta-zero or delta neutral for the stock position
    b. long vs short: long is holding that option; short is selling that contract to someone else. long trades mean you own the convexity (in gamma), and short trades mean you owe it. simply, long trades mean you benefit from the movement of the option, and shorts is the other side of it
    c. continuous delta hedging to rebalance to delta neutrality costs exactly the BSM premium in total, regardless where the stock moves. but it also gets prohibitively expensive. hence it would be better to hedge often using delta if the stock is volatile, and less so when it isn't
2. theta: time decay of the portfolio; as time passes by the value of the portfolio decreases as time passes by
    a. it can also be a proxy for gamma
3. gamma: rate of change in delta
    a. helpful in understanding how frequent should delta hedging change; smaller gamma = infrequent changes needed, larger gamma = you are at risk of not hedging as often because the prices are changing dramatically
    b. usually when gamma is positive, theta is negative; portfolio value increases/decreases as the S changes
    c. when gamma is negative, theta is positive; portfolio value increases/decreases with minimal S changes
4. vega: rate of change of option price based on implied volatility

gamma theta and vega all peak at the money
gamma and vega are identical for calls and puts with the same inputs
put delta is just theh call s-curve just flipped-- put-call parity is also shown here
theta going positive for deep OTM puts (which makes sense because time will increase the strike value of that stock)
## 3. What do the codes do?
The [Greeks Visualiser](greeks_viz.py) creates the greek curves from 50% of the stock to 1.5x the price of stock. This is to simulate the different points in which the stock will reach a future price given a strike price.

## 4. What surprised me?