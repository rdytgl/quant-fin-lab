# Define libraries
import numpy as np
import matplotlib.pyplot as plt

# Set initial parameters
s_0 = 100 
mu = 0.10
sigma = 0.60
T = 2 # time period
N = 252 * T # number of steps
dt = T / N # time step/delta t
num_paths = 1000 # number of simulations 

# Generating all random draws
Z = np.random.standard_normal((num_paths, N))


#  Building price paths
prices = np.zeros ((num_paths, N+1))
prices[:, 0] = s_0         
for t in range(1, N+1):
            prices[:, t] = prices[:, t-1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z[:, t-1])
        
# Getting final asset price for the 1000 paths
final_prices = prices[:, -1]
log_final_prices = np.log(final_prices)

# Computing arithmetic returns of a singular path
arithmetic_returns = (prices[0, 1:] - prices[0, :-1]) / prices[0, :-1]

# Computing log returns of a singular path
log_returns = np.log(prices[0, 1:] / prices[0, :-1])

# Plotting arithmetic returns & log returns, difference between arithmetic and log returns, 
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot 1 — Both returns overlaid
axes[0].plot(arithmetic_returns, color='blue', alpha=0.7, label='arithmetic')
axes[0].plot(log_returns, color='red', alpha=0.7, label='log')
axes[0].set_title('arithmetic-v-log-returns')
axes[0].set_xlabel('time steps')
axes[0].set_ylabel('returns')
axes[0].legend()

# Plot 2 — Distributions
axes[1].hist(arithmetic_returns, bins=50, color='blue', alpha=0.7, label='arithmetic')
axes[1].hist(log_returns, bins=50, color='red', alpha=0.7, label='log')
axes[1].set_title('return-distrib')
axes[1].set_xlabel('returns')
axes[1].set_ylabel('freq')
axes[1].legend()

# Plot 3 — Difference
axes[2].plot(arithmetic_returns - log_returns, color='purple', alpha=0.7)
axes[2].set_title('diff-between-arith-and-log-returns')
axes[2].set_xlabel('time-steps')
axes[2].set_ylabel('diff')

plt.tight_layout()
plt.show()

# Plotting paths & final prices
fig, ax = plt.subplots(1, 3, figsize=(16, 6))
ax[0].plot(prices.T, color='blue', alpha=0.1)
ax[0].set_title('gbm simulation - 1000 paths')
ax[0].set_xlabel('time_steps')
ax[0].set_ylabel('asset_price')

ax[1].hist(final_prices, bins=50, color='blue', alpha=0.7)
ax[1].set_title('final asset price dist')
ax[1].set_xlabel('final_asset_price')
ax[1].set_ylabel('freq')

ax[2].hist(log_final_prices, bins=50, color='blue', alpha=0.7)
ax[2].set_title('log of final asset price dist')
ax[2].set_xlabel('log_final_asset_price')
ax[2].set_ylabel('freq')

plt.tight_layout()
plt.show()