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

# def bsm_put(sigma, s_0, k, r, T):
    # d1 = d_1(sigma, s_0, k, r, T)
    # d2 = d_2(sigma, s_0, k, r, T)
    # put_price = k * exp(-r * T) * norm.cdf(-d2) - s_0 * norm.cdf(-d1)
    # return put_price

def implied_vol_call(call_market_price, s_0, k, r, T):
    sigma = 0.20
    for i in range(100):
        # Iterate d1 computation
        d1 = d_1(sigma, s_0, k, r, T)

        # Calculate current price
        price = bsm_call(sigma, s_0, k, r, T)

        # Calculate vega
        vega = s_0 * sqrt(T) * norm.pdf(d1)
        if vega < 1e-8: # if vega is too small (almost 0), formula will be undefined
            break

        # Update sigma
        old_sigma = sigma
        sigma = sigma - 0.5 * (price - call_market_price)/vega
        sigma = max(1e-6, min(sigma, 5))
        
        # Break if np.isclose is True
        if abs(old_sigma - sigma) < 1e-6:
            return sigma
    return None

# def implied_vol_put(put_market_price, s_0, k, r, T):
#     sigma = 0.20
#     for i in range(100):
#         # Iterate d1 computation
#         d1 = d_1(sigma, s_0, k, r, T)

#         # Calculate current price
#         price = bsm_put(sigma, s_0, k, r, T)

#         # Calculate vega
#         vega = s_0 * sqrt(T) * norm.pdf(d1)
#         if vega < 1e-8: # if vega is too small (almost 0), formula will be undefined
#             break

#         # Update sigma
#         old_sigma = sigma
#         sigma = sigma - 0.5 * (price - put_market_price)/vega
#         sigma = max(1e-6, min(sigma, 5))

#         # Break if np.isclose is True
#         if abs(old_sigma - sigma) < 1e-6:
#             return sigma
#     return None

# Define inputs
s_0 = float(input("Enter initial price: "))
k = float(input("Enter strike price: "))
r = float(input("Enter risk-free rate (decimal): "))
T = float(input("Enter time of maturity (years): "))
call_market_price = float(input("Enter call market price: "))
# put_market_price = float(input("Enter put market price: "))

iv_call = implied_vol_call(call_market_price, s_0, k, r, T) 
print(f"The implied volatility is {iv_call:.3f}")

# Initial idea for the code was to check parity of the volatility using call and put prices.
# For simplicity, implied volatility was computed using call price.
# iv_put = implied_vol_put(put_market_price, s_0, k, r, T)

# if iv_call is None or iv_put is None:
#     print("Implied volatility did not converge.")
# elif abs(iv_call - iv_put) < 1e-3:
#     print(f"The implied volatility is {iv_call:.3f}")
# else:
#     print("Mismatch between call and put IV.")