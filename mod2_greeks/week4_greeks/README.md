# Weekly Summary

## 1. What did I model?

## 2. What is the key insight?
// clean these:
// insert formulas and explanations for the ipynb
1. delta: how much the option price changes for every small change in stock price; measures instantaneous changes only
    a. very important here: delta of options can range between 1 to -1; usually 0 to 1 is for call options and -1 to 0 for put; but we are aiming for delta-zero or delta neutral for the stock position
    b. long vs short: long is holding that option; short is selling that contract to someone else. long trades mean you own the convexity (in gamma), and short trades mean you owe it. simply, long trades mean you benefit from the movement of the option, and shorts is the other side of it
    c. the cost difference between BSM and using a delta hedge: the ideal is continuous trade--> but that trade can reach infinity quickly (esp when done instantaneously and continuously). since it is like holding long positions, the stocks can go in different directions, hence affecting the total option cost. 
2. theta: time decay of the portfolio; as time passes by the value of the portfolio decreases as time passes by
    a. it can also be a proxy for gamma
3. gamma: rate of change in delta
    a. helpful in understanding how frequent should delta hedging change; smaller gamma = infrequent changes needed, larger gamma = you are at risk of not hedging as often because the prices are changing dramatically
    b. usually when gamma is positive, theta is negative; portfolio value increases/decreases as the S changes
    c. when gamma is negative, theta is positive; portfolio value increases/decreases with minimal S changes
4. vega: rate of change of option price based on implied volatility


## 3. What do the codes do?

## 4. What surprised me?