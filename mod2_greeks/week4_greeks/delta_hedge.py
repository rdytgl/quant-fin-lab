# This code generates a weekly delta hedging table for call options
from scipy.stats import norm
from math import log, sqrt, exp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Function for d1 and d2
def d_1(sigma, s_0, k, r, T):
    d_1 = (log(s_0/k)+(r+(sigma**2)/2)*T)/((sigma)*sqrt(T))
    return d_1

def d_2(sigma, s_0, k, r, T): 
    return d_1(sigma, s_0, k, r, T) - (sigma)*sqrt(T)

# Pricer (european put/call)
def bsm(sigma, s_0, k, r, T):
    d1 = d_1(sigma, s_0, k, r, T)
    d2 = d_2(sigma, s_0, k, r, T)
    opt_price = s_0 * norm.cdf(d1) - k * exp(-r * T) * norm.cdf(d2)
    return opt_price

def compute_delta_hedge(sigma, S, k, r, T_remaining):
    if T_remaining <= 0:
        return 1.0 if S > k else 0.0
    return norm.cdf(d_1(sigma, S, k, r, T_remaining))

s_0 = float(input("Enter initial price: "))
k = float(input("Enter strike price: "))
r = float(input("Enter risk-free rate (decimal): "))
sigma = float(input("Enter volatility (sigma): "))
mu = float(input("Enter drift (mu): "))
n_weeks = int(input("Enter time of maturity (weeks): "))
n_options = float(input("Enter number of options purchased: "))
dt = 1/52 # weekly hedge time

# Compute options cost with BSM:
bsm_price = bsm(sigma, s_0, k, r, n_weeks * dt) * n_options

# Generate random stock prices over the course of n-weeks
np.random.seed(0)
stock_prices = [s_0]
for t in range(n_weeks):
    dS = stock_prices[-1] * (mu * dt + sigma * np.random.normal() * sqrt(dt))
    stock_prices.append(stock_prices[-1] + dS)



# Compute delta based on weekly stock prices
T = n_weeks / 52
deltas = [compute_delta_hedge(sigma, S, k, r, T - t * dt) for t, S in enumerate(stock_prices)]

# Compute stocks purchased hedged against options bought
shares = [deltas[0] * n_options]
shares += [(deltas[t] - deltas[t-1]) * n_options for t in range(1, len(deltas))]

# Cost of shares purchased
cost = [shares[t] * S for t, S in enumerate(stock_prices)]

# Cumulative cost and interest computation
cum_cost = []
interest = []
for t in range (len(cost)):
    int_cost = cost[t] * r * dt if t < n_weeks else 0 # interest on week's spend
    if t == 0:
        cum_cost.append(cost[0] + int_cost)
    else:
        new_cum = cum_cost[t-1] + cost [t] + int_cost
        cum_cost.append(new_cum)
    interest.append(int_cost)

# Create the delta hedge table
rows = []
for week in range(n_weeks + 1):
    rows.append({
        "week": week,
        "stock_price": stock_prices[week],
        "delta": deltas[week],
        "shares_purchased": shares[week],
        "cost_shares_purchased_($000)": cost[week]/1000,
        "cumulative_cost_($000)": cum_cost[week]/1000,
        "interest_cost__($000)": interest[week]/1000
    })

pd.options.display.float_format = '{:.2f}'.format
df = pd.DataFrame(rows)

# Display output
print(df)
if stock_prices[-1] > k:
    delta_hedge = cum_cost[-1] - (k * n_options)
else:
    delta_hedge = cum_cost[-1]
scenario = "ITM (Exercised)" if stock_prices[-1] > k else "OTM (Expired Worthless)"
print(f"Scenario: {scenario}")
print(f"Cost of Hedging: {delta_hedge: .2f}")
print(f"Cost of options using BSM: {bsm_price: .2f}")
print(f"Hedging Error: {abs(delta_hedge - bsm_price):.2f}")
print(f"As % of BSM: {abs(delta_hedge - bsm_price)/bsm_price*100:.1f}%")

