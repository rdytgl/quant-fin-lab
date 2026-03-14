import numpy as np

s_0 = 20
u = 1.1
d = 0.9
r = 0.04
T = 0.25
K = 21

# Step 1: Calculate the stock price at time T
s_u = s_0 * u  # Stock price if the stock goes up
s_d = s_0 * d  # Stock price if the stock goes down

p = (np.exp(r * T) - d) / (u - d)  # Risk-neutral probability of the stock going up

# Step 2: Calculate the payoff of the call option at time T
payoff_u = max(s_u - K, 0)  # Payoff if the stock goes up
payoff_d = max(s_d - K, 0)  # Payoff if the stock goes down

# Step 3: Calculate the expected payoff under the risk-neutral measure
expected_payoff = p * payoff_u + (1 - p) * payoff_d

# Step 4: Discount the expected payoff back to time 0
option_price = np.exp(-r * T) * expected_payoff
print(f"The price of the European call option is: {option_price:.2f}")