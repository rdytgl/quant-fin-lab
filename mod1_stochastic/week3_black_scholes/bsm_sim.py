from scipy.stats import norm
from math import log, sqrt, exp
import numpy as np

# Define inputs
s_0 = float(input("Enter initial price: "))
k = float(input("Enter strike price: "))
r = float(input("Enter risk-free rate (decimal): "))
T = float(input("Enter time of maturity (years): "))
sigma = float(input("Enter volatility (sigma): "))

# Calculate d1
d_1 = (log(s_0/k)+(r+(sigma**2)/2)*T)/((sigma)*sqrt(T))

# Calculate d2
d_2 = d_1 - (sigma)*sqrt(T) 
# Calculate c
c = s_0*norm.cdf(d_1)-k*exp(-r*T)*norm.cdf(d_2)

# Calculate p
p = k*exp(-r*T)*norm.cdf(-d_2)-s_0*norm.cdf(-d_1)

# Verifying c and p prices
net_premium = c - p
returns = s_0-k*exp(-r*T)

if np.isclose(net_premium, returns):
    print("BSM Pricer is verified.")
else:
    print("BSM Pricer needs rework.")

# Print
print(f"Call Price: {c:.3f}")
print(f"Put Price: {p:.3f}")