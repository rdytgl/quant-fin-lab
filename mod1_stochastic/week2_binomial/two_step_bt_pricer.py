import numpy as np

s_0 = 20
u = 1.1
d = 0.9
r = 0.04
dt = 0.25
K = 21

# Step 1: Calculate the stock price at time T
s_uu = s_0 * u * u  # Stock price if the stock goes up twice
s_ud = s_0 * u * d  # Stock price if the stock goes up then down/down then up
s_dd = s_0 * d * d  # Stock price if the stock goes down twice

p = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral probability of the stock going up

# Step 2: Calculate the payoff of the call option at time T
f_uu = max(s_uu - K, 0)  # Payoff if the stock goes up twice
f_ud = max(s_ud - K, 0)  # Payoff if the stock goes up then down
f_dd = max(s_dd - K, 0)  # Payoff if the stock goes down twice

# Step 3: Calculate the expected payoff under the risk-neutral measure
f_u = np.exp(-r * dt) * (p * f_uu + (1 - p) * f_ud)  # Expected payoff if the stock goes up at time 1
f_d = np.exp(-r * dt) * (p * f_ud + (1 - p) * f_dd)  # Expected payoff if the stock goes down at time 1
f = np.exp(-r * dt) * (p * f_u + (1 - p) * f_d)  # Expected payoff at time 0

print(f"The price of the European call option is: {f:.2f}")