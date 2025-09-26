import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np
import warnings

warnings.filterwarnings('ignore')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 0)


indicepanel = pd.read_csv('index_data/indice_panel.csv', index_col=0)
#print(indicepanel.head())

Train = indicepanel.iloc[-2000:-1000,:]
Test = indicepanel.iloc[-1000:,:]

formula = 'spy~spy_lag1+sp500+nasdaq+dji+cac40+daxi+aord+hsi+nikkei'
lm = smf.ols(formula=formula, data=Train).fit()

Train['PredictedY']=lm.predict(Train)
Test['PredictedY']=lm.predict(Test)


#basic trading algo (train)

Train['Order'] = [1 if sig>0 else -1 for sig in Train['PredictedY']]
Train['Profit'] = Train['spy'] * Train['Order']

Train['Wealth'] = Train['Profit'].cumsum()
print("Total Profit made in Train: ", Train['Profit'].sum())

#train strategy comparison

plt.figure(figsize=(10,10))
plt.title("Perfomance of strategy in Train")
plt.plot(Train['Wealth'].values, color='green', label='Signal Based Strategy')
plt.plot(Train['spy'].cumsum().values, color='red', label='Buy and Hold Strategy')
plt.legend()
plt.show()

#basic trading algo (test)
Test['Order'] = [1 if sig>0 else -1 for sig in Test['PredictedY']]
Test['Profit'] = Test['spy'] * Test['Order']

Test['Wealth'] = Test['Profit'].cumsum()
print("Total Profit made in Test: ", Test['Profit'].sum())

#Test Strategy comparison

plt.figure(figsize=(10,10))
plt.title("Perfomance of strategy in Test")
plt.plot(Test['Wealth'].values, color='green', label='Signal Based Strategy')
plt.plot(Test['spy'].cumsum().values, color='red', label='Buy and Hold Strategy')
plt.legend()
plt.show()


#evaluation - Sharpe and Max Drawdown

Train['Wealth'] = Train['Wealth'] + Train.loc[Train.index[0], 'Price']
Test['Wealth'] = Test['Wealth'] + Test.loc[Test.index[0], 'Price']


Train['Return'] = np.log(Train['Wealth']) - np.log(Train['Wealth'].shift(1))
dailyr = Train['Return'].dropna()
print('Daily Sharpe Ratio in Train is ', dailyr.mean()/dailyr.std(ddof=1))
print('Yearly Sharpe Ratio in Train is ', (252**0.5)*dailyr.mean()/dailyr.std(ddof=1))

Test['Return'] = np.log(Test['Wealth']) - np.log(Test['Wealth'].shift(1))
dailyr = Test['Return'].dropna()
print('Daily Sharpe Ratio in Test is ', dailyr.mean()/dailyr.std(ddof=1))
print('Yearly Sharpe Ratio in Test is ', (252**0.5)*dailyr.mean()/dailyr.std(ddof=1))


Train['Peak']=Train['Wealth'].cummax()
Train['Drawdown']=(Train['Peak']-Train['Wealth'])/Train['Peak']
print("Maximum Drawdown in Train is: ", Train['Drawdown'].max())

Test['Peak'] = Test['Wealth'].cummax()
Test['Drawdown'] = (Test['Peak'] - Test['Wealth'])/Test['Peak']
print('Maximum Drawdown in Test is ', Test['Drawdown'].max())




