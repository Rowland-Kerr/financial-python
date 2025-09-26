import yfinance as yf
import pandas as pd
import os

folder = "index_data"
os.makedirs(folder, exist_ok=True)

tickers = {
    "SPY": "SPY",
    "S&P500": "^GSPC",
    "DJI": "^DJI",
    "NIKKEI225": "^N225",
    "AllOrdinaries": "^AORD",
    "CAC40": "^FCHI",
    "DAX": "^GDAXI",
    "HANGSENG": "^HSI",
    "NASDAQ": "^IXIC"
    }

for name, ticker in tickers.items():
    print(f"Fetching {name} ({ticker})...")
    data = yf.download(ticker, start='2017-01-01', end='2025-01-01', auto_adjust=True)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data.index.name = "Date"

    filepath = os.path.join(folder, f"{name}.csv")
    data.to_csv(filepath, index_label="Date")

    print(f"Saved {name} to {filepath}")
    
