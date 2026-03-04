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
            prices[:, t] = prices[:, t-1] * np.exp(mu * dt + sigma * np.sqrt(dt) * Z[:, t-1])
        
# Getting mean price for the 1000 paths
ave_prices = np.mean(prices, axis=0)

# Getting expected mean price at s_0=100
expected_ave_price = s_0 * np.exp(mu * np.arange(N+1) * dt)

# Plotting mean price paths & expected mean price
plt.figure(figsize=(16, 12))
plt.plot(ave_prices, color='blue', label='average price path')
plt.plot(expected_ave_price, color='red', label='expected average price path')
plt.title('average price path vs expected average price path')
plt.xlabel('days')
plt.ylabel('asset_price')
plt.legend()
plt.show()