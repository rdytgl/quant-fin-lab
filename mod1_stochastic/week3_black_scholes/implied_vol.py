from scipy.stats import norm
from math import log, sqrt, exp
import numpy as np

def d_1(sigma, s_0, k, r, T):
    d_1 = (log(s_0/k)+(r+(sigma**2)/2)*T)/((sigma)*sqrt(T))
    return d_1

def d_2(sigma, s_0, k, r, T): 
    return d_1(sigma, s_0, k, r, T) - (sigma)*sqrt(T)

def bsm_call(sigma, s_0, k, r, T):
    d1 = d_1(sigma, s_0, k, r, T)
    d2 = d_2(sigma, s_0, k, r, T)
    call_price = s_0 * norm.cdf(d1) - k * exp(-r * T) * norm.cdf(d2)
    return call_price

def bsm_put(sigma, s_0, k, r, T):
    d1 = d_1(sigma, s_0, k, r, T)
    d2 = d_2(sigma, s_0, k, r, T)
    put_price = k * exp(-r * T) * norm.cdf(-d2) - s_0 * norm.cdf(-d1)
    return put_price

def implied_vol_call(call_market_price, s_0, k, r, T):
    sigma = 0.20
    d1 = d_1(sigma, s_0, k, r, T)
    for i in range(100):
        # Calculate current price
        price = bsm_call(sigma, s_0, k, r, T)
        # Calculate vega
        vega = s_0 * sqrt(T) * norm.cdf(d1)
        # Update sigma
        new_sigma = (sigma - (sigma - market_price))/vega
        # Break if np.isclose is True
        if np.isclose(new_sigma, sigma):
            return new_sigma
    return None

def implied_vol_put(put_market_price, s_0, k, r, T):
    sigma = 0.20
    d1 = d_1(sigma, s_0, k, r, T)
    for i in range(100):
        # Calculate current price
        price = bsm_put(sigma, s_0, k, r, T)
        # Calculate vega
        vega = s_0 * sqrt(T) * norm.cdf(d1)
        # Update sigma
        new_sigma = (sigma - (sigma - market_price))/vega
        # Break if np.isclose is True
        if np.isclose(new_sigma, sigma):
            return new_sigma
    return None

# Define inputs
s_0 = float(input("Enter initial price: "))
k = float(input("Enter strike price: "))
r = float(input("Enter risk-free rate (decimal): "))
T = float(input("Enter time of maturity (years): "))
call_market_price = float(input("Enter call market price: "))
put_market_price = float(input("Enter put market price: "))
sigma = float(input("Enter volatility (sigma): "))

implied_vol_call = implied_vol_call(call_market_price, s_0, k, r, T) 
implied_vol_put = implied_vol_put(put_market_price, s_0, k, r, T)

if np.isclose(implied_vol_call, implied_vol_put):
    print(f"The implied volatility of the stock is {implied_vol_call:.3f}")
else:
    print("Implied volatility function is wrong.")