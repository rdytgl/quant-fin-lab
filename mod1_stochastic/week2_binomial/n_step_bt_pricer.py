# This code is to automate the binomial tree option pricing for n steps.
# Import libraries
import numpy as np

# Parameters
s_0 = 20 
u = 1.1
d = 0.9
r = 0.04
dt = 0.25
K = 21.5
n = 6 # Number of steps in the binomial tree

p = (np.exp(r * dt) - d) / (u - d)

# Step 1: Calculate the stock price at time T for all possible paths
stock_prices = np.zeros((n + 1, n + 1)) # Create a matrix to store stock prices at each node
for i in range(n + 1):
    for j in range(i + 1):
        stock_prices[i, j] = s_0 * (u ** j) * (d ** (i - j)) # Calculate stock price at each node

# Step 2: Loop through the tree to calculate the payoff at maturity for all paths
payoffs = np.zeros((n + 1, n + 1)) # Create a matrix to store payoffs at maturity
for j in range(n + 1):
    payoffs[n, j] = max(stock_prices[n, j] - K, 0) # Calculate payoff at maturity for each path

# Step 3: Loop backwards through the tree to calculate the expected payoff at each node and discount it back to time 0
for i in range (n-1, -1, -1):
    for j in range (i+1):
        payoffs[i, j] =  np.exp(-r*dt) * (p * payoffs[i+1, j+1] + (1-p) * payoffs[i+1, j])

print(stock_prices)
print(payoffs)
print(f"Option price: {payoffs[0, 0]:.4f}")