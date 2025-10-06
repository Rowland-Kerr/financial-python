# Linear Regression Signal Model and Backtest

This project investigates whether a simple linear regression model can extract predictive
signals from global equity indices to forecast returns and form a basic trading strategy.
It is intended as a learning exercise in quantitative finance, demonstrating model design,
evaluation, and critical reflection on performance limitations.


# Overview

- Objective: Identify linear relationships between nine equity indices and generate return forecasts.  
- Method: Ordinary Least Squares (OLS) regression using `statsmodels.formula.api.ols`.  
- Data: Daily closing prices of nine indices downloaded via `yfinance`, stored locally as CSVs.  
- Evaluation: Out-of-sample test performance (RMSE, Adjusted R²) and strategy robustness via Sharpe ratio and maximum drawdown.


# Project Structure

regression_project/
─ csv_load.py: Downloads data via yfinance and saves CSVs
─ test.py: Loads CSVs, builds combined DataFrame ('indicepanel'), cleans data, builds test and train set, and uses .predict() for ols
─ evaluation_fns.py: Contains evaluation functions (adjusted R², RMSE)
─ model_evaluation.py: Runs regression, makes predictions, evaluates and plots results
─ data/:  Contains downloaded CSV index data


## Methodology

1. **Data Preparation**
   - Uses `yfinance` and `os` to download and save daily closing prices for each index.
   - Constructs a combined returns panel (`indicepanel`), cleans missing values via `ffill()` and `dropna()`.
   - Splits dataset into 1,000 training days and 1,000 test days (chronological split).

2. **Exploratory Analysis**
   - Generates correlation matrix and scatter plots to visualise relationships and filter noisy features.

3. **Model Fitting**
   - Fits an OLS model on the training data using `statsmodels`.
   - Predicts returns for both training and testing datasets.

4. **Performance Evaluation**
   - Evaluates with RMSE and Adjusted R² via helper functions in `evaluation_fns.py`.
   - Constructs a summary table comparing in-sample and out-of-sample results.
   - Calculates Sharpe ratio and maximum drawdown to simulate naive trading performance.


## Key Results

- The model achieved moderate fit on training data but lower predictive power out-of-sample due to 2021 market regime changes.
- Demonstrates the limitations of static linear relationships in non-stationary financial series.
- Analysis highlights the need for regularisation, regime-switching, or nonlinear extensions in future work.


## Libraries Used

`pandas`, `numpy`, `statsmodels`, `matplotlib`, `yfinance`, `os`


## Takeaways

This project emphasises:
- The importance of critical evaluation in backtesting.
- Awareness of overfitting and the illusion of predictive power in linear models.
- Building transparent, modular, and reproducible code for quantitative experiments.
