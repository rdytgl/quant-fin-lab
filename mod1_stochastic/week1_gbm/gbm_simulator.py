# Define libraries
import numpy as np
import matplotlib.pyplot as plt

# Set initial parameters
s_0 = 100 
mu = 0.10
sigma = 0.20
T = 1 # time period
N = 252 # number of steps
dt = T / N # time step/delta t
num_paths = 1000 # number of simulations 

# Generating all random draws
Z = np.random.standard_normal((num_paths, N))


#  Building price paths
prices = np.zeros ((num_paths, N+1))
prices[:, 0] = s_0         
for t in range(1, N+1):
            prices[:, t] = prices[:, t-1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z[:, t-1])
        
# Plotting paths        
plt.figure(figsize=(16, 12))
plt.plot(prices.T, alpha=0.1, color='blue')
plt.title('gbm sim - 1000 paths @ 16 scenarios')
plt.xlabel('days')
plt.ylabel('asset_price')
plt.show()
