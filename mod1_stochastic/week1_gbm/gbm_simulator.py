# Define libraries
import numpy as np
import matplotlib.pyplot as plt

# Set initial parameters
s_0 = 100 
mu_values = [0.05, 0.10, 0.15, 0.20]
sigma_values = [0.10, 0.20, 0.30, 0.40]
T = 1 # time period
N = 252 # number of steps
dt = T / N # time step/delta t
num_paths = 1000 # number of simulations 

# Generating all random draws
Z = np.random.standard_normal((num_paths, N))

fig, axes = plt.subplots(4, 4, figsize=(16, 12))
for i, mu in enumerate(mu_values):
    for j, sigma in enumerate(sigma_values):
        #  Building price paths
        prices = np.zeros ((num_paths, N+1))
        prices[:, 0] = s_0 
        for t in range(1, N+1):
            prices[:, t] = prices[:, t-1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z[:, t-1])
        # Plotting paths
        axes[i, j].plot(prices.T, alpha=0.1, color='blue')
        axes[i,j].set_title(f'mu={mu:.2f}, sigma={sigma:.2f}')

plt.plot(prices.T, alpha=0.1, color='blue')
plt.suptitle('gbm sim - 1000 paths @ 16 scenarios')
plt.tight_layout()
plt.show()
