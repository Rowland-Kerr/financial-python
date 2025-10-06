Black - Scholes Option Pricing and Sensitivity Analysis

This project implements the Black-Scholes model for pricing European call and put options,
and extends it to calculate key sensitivities (Greeks). It includes both analytical and
visual demonstrations of how option values respond to underlying parameters.

## Overview

Objective: Implement closed-form Black–Scholes pricing and calculate Greeks (Δ, Γ, Θ, ρ, ν).  
Outputs: Option prices, sensitivity plots, and a callable function returning Greeks.  

## Functionality

1. black_scholes_model(S, K, T, r, sigma, option_type)
   - Returns theoretical price for a European call or put.
   - Inputs:
     - `S`: Spot price
     - `K`: Strike price
     - `T`: Time to maturity (years)
     - `r`: Risk-free rate
     - `sigma`: Volatility
     - `option_type`: `'call'` or `'put'`

2. black_scholes_greeks(S, K, T, r, sigma, greek)
   - Returns value of chosen Greek:
     - `delta`, `gamma`, `theta`, `vega`, `rho`
   - Vectorised for arrays of prices or volatilities.

3. Plots
   - Price vs. strike price surface.
   - sensitivity plot for any of the greeks

---

 Example Visualisations

<img width="1000" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/2cd8b90b-e837-4182-a297-d492f0a17fc0" />

<img width="1000" height="500" alt="Figure_2" src="https://github.com/user-attachments/assets/6fb0b78f-05fa-48f7-b7f4-dd0108f7136f" />

---

## Libraries Used

`numpy`, `scipy.stats`, `matplotlib`, 

---

## Discussion

- Illustrates how option sensitivity (Greeks) varies with volatility, time, and moneyness.  
- Demonstrates the limits of Black–Scholes assumptions (log-normal returns, constant volatility).  
- Serves as a foundation for later Monte Carlo and stochastic volatility extensions.

---

## Future Work

- Compare analytical results to Monte Carlo simulation for validation.  
- Extend to American options (binomial tree or finite difference methods).  
- Stress-test model assumptions under fat-tailed or jump-diffusion distributions.

