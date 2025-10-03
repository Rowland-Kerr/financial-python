import yfinance as yf
import numpy as np
import scipy.stats as si
import matplotlib.pyplot as plt
import mplfinance as mpf
import plotly.graph_objects as go
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

##  fetching real options data - download options data for major financial
#   institutions such as JPMC, GS, MS, BlackRock and Citigroup

def fetch_options_data(tick):
    ticker = yf.Ticker(tick)
    options_dates = ticker.options
    options_data = ticker.option_chain(options_dates[0])
    return options_data.calls, options_data.puts

#eg

jpm_calls, jpm_puts = fetch_options_data('JPM')

jpm_stock_data = yf.download('JPM',start='2023-01-01', end='2025-01-01')

#visualize historic stock price data for JPM

plt.figure(figsize=(10,5))
plt.plot(jpm_stock_data['Close'])
plt.title('JPM Historic Stock Price')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.grid(True)
plt.show()

#implementing black-scholes using OOP approach

class BlackScholesModel:
    def __init__(self, S, K, T, r, sigma):
        self.S = S #underlying price
        self.K = K #option strike price
        self.T = T #time to expiration (years)
        self.r = r #risk-free rate
        self.sigma = sigma #volatility of underlying

    def d1(self):

        return (np.log(self.S/self.K) + (self.r * 0.5 * self.sigma ** 2) * self.T)/ (self.sigma * np.sqrt(self.T))

    def d2(self):

        return self.d1() - self.sigma * np.sqrt(self.T)

    def call_option_price(self):

        return (self.S * si.norm.cdf(self.d1(), 0.0, 1.0) - self.K * np.exp(-self.r * self.T) * si.norm.cdf(self.d2(), 0.0, 1.0))

    def put_option_price(self):

        return (self.K * np.exp(-self.r * self.T) * si.norm.cdf(-self.d2(), 0.0, 1.0) - self.S * si.norm.cdf(-self.d1(), 0.0, 1.0))

#eg usage

bsm = BlackScholesModel(S=100, K=100, T=1, r=0.05, sigma = 0.2)
print(f'Call option price: {bsm.call_option_price()}')
print(f'Put option price: {bsm.put_option_price()}')

#now to estimate the volatility - will use annualized sd of returns

def Calculate_historic_volatility(stock_data, window=252):
    log_returns = np.log(stock_data['Close']/stock_data['Close'].shift(1))
    volatility = np.sqrt(window) * log_returns.std()
    return volatility

trading_days = jpm_stock_data.shape[0]
jpm_volatility = Calculate_historic_volatility(jpm_stock_data, trading_days)
print(f'JPM Historic Volatility: {jpm_volatility}')

#can now use this as an estimation for sigma in the BSM


#class to return the greeks

class BlackScholesGreeks(BlackScholesModel):

    def delta_call(self):

        return si.norm.cdf(self.d1(), 0.0, 1.0)

    def delta_put(self):

        return -si.norm.cdf(-self.d1(), 0.0, 1.0)

    def gamma(self):

        return si.norm.pdf(self.d1(), 0.0, 1.0) / (self.S * self.sigma * np.sqrt(self.T))

    def theta_call(self):

        return (-self.S * si.norm.pdf(self.d1(), 0.0, 1.0) * self.sigma / (2 * np.sqrt(self.T)) - self.r * self.K * np.exp(-self.r * self.T) * si.norm.cdf(self.d2(), 0.0, 1.0))

    def theta_put(self):

        return (-self.S * si.norm.pdf(self.d1(), 0.0, 1.0) * self.sigma / (2 * np.sqrt(self.T)) + self.r * self.K * np.exp(-self.r * self.T) * si.norm.cdf(-self.d2(), 0.0, 1.0))

    def vega(self):

        return self.S * si.norm.pdf(self.d1(), 0.0, 1.0) * np.sqrt(self.T)

    def rho_call(self):

        return self.K * self.T * np.exp(-self.r * self.T) * si.norm.cdf(self.d2(), 0.0, 1.0)

    def rho_put(self):

        return -self.K * self.T * np.exp(-self.r * self.T) * si.norm.cdf(-self.d2(), 0.0, 1.0)

#eg

bsg = BlackScholesGreeks(S=100, K=100, T=1, r=0.05, sigma=0.2)
print(f'Call Delta: {bsg.delta_call()}')
print(f'Put Delta: {bsg.delta_put()}')


#visualize the greeks by plotting them with underlying asset price

stock_prices = np.linspace(80,120,100)
deltas = [BlackScholesGreeks(S=price, K=100, T=1, r=0.05, sigma=0.2).delta_call() for price in stock_prices]

plt.figure(figsize=(10,5))
plt.plot(stock_prices, deltas)
plt.title('Delta of a Call Option as Underlying Price Changes')
plt.xlabel('Stock Prices')
plt.ylabel('Delta')
plt.grid(True)
plt.show()

#finally, analyzing the sensitivity of option prices to changes in rates and volatility

def plot_option_sensitivity(bsmodel, parameter, values, option_type='call'):
    prices = []
    for value in values:
        setattr(bsmodel, parameter, value)
        if option_type == 'call':
            prices.append(bsmodel.call_option_price())
        else:
            prices.append(bsmodel.put_option_price())

    plt.figure(figsize=(10,5))
    plt.plot(values, prices)
    plt.title(f'Option Price Sensitivity to {parameter.capitalize()}')
    plt.xlabel(parameter.capitalize())
    plt.ylabel('Option Price')
    plt.grid(True)
    plt.show()

#example use

volatilities = np.linspace(0.1, 0.3, 100)
plot_option_sensitivity(bsm, 'sigma', volatilities, 'call')

#can do the same for rates, and on put options
