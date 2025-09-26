import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as smf
import warnings
warnings.filterwarnings("ignore")


spy = pd.read_csv('index_data/SPY.csv', index_col=0)
sp500 = pd.read_csv('index_data/S&P500.csv', index_col=0)
dji = pd.read_csv('index_data/DJI.csv', index_col=0)
nik = pd.read_csv('index_data/NIKKEI225.csv', index_col=0)
aord = pd.read_csv('index_data/AllOrdinaries.csv', index_col=0)
dax = pd.read_csv('index_data/DAX.csv', index_col=0)
hsi = pd.read_csv('index_data/HANGSENG.csv', index_col=0)
cac40 = pd.read_csv('index_data/CAC40.csv', index_col=0)
nasdaq = pd.read_csv('index_data/NASDAQ.csv', index_col=0)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 0)



indicepanel = pd.DataFrame(index=spy.index)

indicepanel['spy']=spy['Open'].shift(-1)-spy['Open']
indicepanel['spy_lag1']=indicepanel['spy'].shift(1)
indicepanel['sp500']=sp500['Open']-sp500['Open'].shift(1)
indicepanel['nasdaq']=nasdaq['Open']-nasdaq['Open'].shift(1)
indicepanel['dji']=dji['Open']-dji['Open'].shift(1)
indicepanel['cac40']=cac40['Open']-cac40['Open'].shift(1)
indicepanel['daxi']=dax['Open']-dax['Open'].shift(1)

indicepanel['aord']=aord['Close']-aord['Open']
indicepanel['hsi']=hsi['Close']-hsi['Open']
indicepanel['nikkei']=nik['Close']-nik['Open']
indicepanel['Price']=spy['Open']

#print(indicepanel.head())


indicepanel = indicepanel.fillna(method='ffill')
indicepanel = indicepanel.dropna()


path_save = 'index_data/indice_panel.csv'
indicepanel.to_csv(path_save)

#split data

Train = indicepanel.iloc[-2000:-1000,:]
Test = indicepanel.iloc[-1000:, :]
print(Train.shape, Test.shape)

from pandas.plotting import scatter_matrix
#sm = scatter_matrix(Train, figsize=(10,10))
#plt.show()

corr_array = Train.iloc[:,:-1].corr()['spy']
print(corr_array)

formula = 'spy~spy_lag1+sp500+nasdaq+dji+cac40+daxi+aord+hsi+nikkei'
lm = smf.ols(formula=formula, data=Train).fit()
print(lm.summary())

Train['PredictedY']=lm.predict(Train)
Test['PredictedY']=lm.predict(Test)

plt.scatter(Train['spy'], Train['PredictedY'])
#plt.show()

from evaluate_fns import adjustedMetric, assessTable

print(assessTable(Test, Train, lm, 9, 'spy'))
