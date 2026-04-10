from scipy.stats import norm
from math import log, sqrt, exp
import numpy as np
import matplotlib.pyplot as plt

# Define inputs
s_0 = float(input("Enter initial price: "))
k = float(input("Enter strike price: "))
r = float(input("Enter risk-free rate (decimal): "))
T = float(input("Enter time of maturity (years): "))
sigma = float(input("Enter volatility (sigma): "))
option_type = input("Type of Option: [C]all or [P]ut: ").strip().lower()

# Generate 300 possible final stock price values ranging from 50% to 2.0x value of set initial price
stock_prices = np.linspace(0.50*s_0, 2*s_0, 300)

# Function for d1 and d2
def d_1(sigma, s_0, k, r, T):
    d_1 = (log(s_0/k)+(r+(sigma**2)/2)*T)/((sigma)*sqrt(T))
    return d_1

def d_2(sigma, s_0, k, r, T): 
    return d_1(sigma, s_0, k, r, T) - (sigma)*sqrt(T)

# Pricer (european put/call)
def bsm(sigma, s_0, k, r, T, option_type):
    if option_type == "c":
        d1 = d_1(sigma, s_0, k, r, T)
        d2 = d_2(sigma, s_0, k, r, T)
        opt_price = s_0 * norm.cdf(d1) - k * exp(-r * T) * norm.cdf(d2)
    elif option_type == "p":
        d1 = d_1(sigma, s_0, k, r, T)
        d2 = d_2(sigma, s_0, k, r, T)
        opt_price = k * exp(-r * T) * norm.cdf(-d2) - s_0 * norm.cdf(-d1)
    else:
        return "Acceptable option type input: C or P"
    return opt_price

# Compute for delta prices
def compute_delta(S):
    h = S * 0.005
    up = bsm(sigma, S + h, k, r, T, option_type)
    down = bsm(sigma, S - h, k, r, T, option_type)
    return (up - down)/(2 * h)

# Compute for gamma
def compute_gamma(S):
    h = S * 0.005
    price = bsm(sigma, S, k, r, T, option_type)
    up = bsm(sigma, S + h, k, r, T, option_type)
    down = bsm(sigma, S - h, k, r, T, option_type)
    return (up - 2 * price + down)/(h ** 2)

# Compute for theta
def compute_theta(S):
    h = min(1/365, T * 0.005)
    price = bsm(sigma, S, k, r, T, option_type)
    down = bsm(sigma, S, k, r, T - h, option_type)
    return (down - price)/h

# Compute for vega
def compute_vega(S):
    h = max(0.01, sigma * 0.005)
    up = bsm(sigma + h, S, k, r, T, option_type)
    down = bsm(sigma - h, S, k, r, T, option_type)
    return (up - down)/(2 * h)

# Compute plot points
prices = [bsm(sigma, S, k, r, T, option_type) for S in stock_prices]

# Compute tangent line
S0 = s_0
h = S0 * 0.005
V0 = bsm(sigma, S0, k, r, T, option_type)
d0 = compute_delta(S0)
tangent = [V0 + d0 * (S - S0) for S in stock_prices]

# Compute greeks
deltas =[compute_delta(S) for S in stock_prices]
gammas = [compute_gamma(S) for S in stock_prices]
thetas = [compute_theta(S) for S in stock_prices]
vegas = [compute_vega(S) for S in stock_prices]

# Plot the price curve
plt.figure()
plt.plot(stock_prices, prices, label="Price")

# Tangent line
plt.plot(stock_prices, tangent, linestyle='--', label="Tangent (Delta)")

# Highlight point
plt.scatter([S0], [V0])

# Strike line
plt.axvline(x=k, linestyle='--', label='Strike')

plt.title("Price Curve with Delta Tangent")
plt.xlabel("Stock Price")
plt.ylabel("Option Price")
plt.legend()

# Plot the greek values
fig, axes = plt.subplots(2, 2, figsize=(12,8))

axes[0, 0].plot(stock_prices, deltas)
axes[0, 0].set_title("Delta")
axes[0, 0].set_xlabel("Stock Price")
axes[0, 0].axvline(x=k, color='red', linestyle='--', label='Strike')
axes[0, 0].legend()

axes[0, 1].plot(stock_prices, gammas)
axes[0, 1].set_title("Gamma")
axes[0, 1].set_xlabel("Stock Price")
axes[0, 1].axvline(x=k, color='red', linestyle='--', label='Strike')
axes[0, 1].legend()

axes[1, 0].plot(stock_prices, thetas)
axes[1, 0].set_title("Theta")
axes[1, 0].set_xlabel("Stock Price")
axes[1, 0].axvline(x=k, color='red', linestyle='--', label='Strike')
axes[1, 0].legend()

axes[1, 1].plot(stock_prices, vegas)
axes[1, 1].set_title("Vega")
axes[1, 1].set_xlabel("Stock Price")
axes[1, 1].axvline(x=k, color='red', linestyle='--', label='Strike')
axes[1, 1].legend()

plt.tight_layout()

# Visualise gamma vs theta graphs
fig, ax1 = plt.subplots()

ax1.plot(stock_prices, gammas, label="Gamma")
ax1.set_xlabel("Stock Price")
ax1.set_ylabel("Gamma")
ax1.axvline(x=k, color='red', linestyle='--', label='Strike')

ax2 = ax1.twinx()

ax2.plot(stock_prices, thetas, label="Theta")
ax2.set_ylabel("Theta")

plt.title('Gamma v.s. Theta')
plt.show()