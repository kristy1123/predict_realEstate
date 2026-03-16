import os #provides functions for interacting with the operating system
import numpy as np
import pandas as pd
import seaborn as sns
from math import sqrt

from numpy import concatenate
from matplotlib import pyplot as plt
from pandas import read_csv
from pandas import DataFrame
from pandas import concat

# To change scientific numbers to float
np.set_printoptions(formatter={'float_kind':'{:f}'.format})

# Increases the size of sns plots
sns.set(rc={'figure.figsize':(8,6)})

import itertools
import warnings

import datetime
from datetime import datetime
from pandas import to_datetime
warnings.filterwarnings("ignore")
warnings.filterwarnings(action='ignore')


import matplotlib.pyplot as plt


from datetime import date
from datetime import datetime

from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn import linear_model

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

import itertools
import warnings
import datetime
from datetime import datetime

import pmdarima as pm
from pmdarima.model_selection import train_test_split



#GG


# csvList=['.csv']
# countryList=['Seoul','',]
Gwangju = pd.read_csv('./estateGJ.csv', header=0, names=['years','Gwangju'])
Gwangju['years'] = pd.to_datetime(Gwangju['years']) #str to pandas Timestamp
Gwangju.index = Gwangju['years']
Gwangju.set_index('years',inplace=True) #index로 변환

#print(Seoul)
#print(Seoul.tail()) #끝에서 5개의 데이터를 보여줌.

#함수 정의.
#평균, 분산, 표준편차 구할 거임.
def plot_rolling(data, interval):
    rolmean = data.rolling(interval).mean()
    rolvar=data.rolling(interval).var()
    rolstd = data.rolling(interval).std()

    # Plot rolling statistics:
    plt.figure(figsize=(5, 5))
    plt.xlabel('Years')
    orig = plt.plot(data, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    var = plt.plot(rolvar, color='green', label='Rolling Var')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.show()


#plot_rolling(Seoul, 2)

# 관측값, 추세, 계절, 불규칙요인
from statsmodels.tsa.seasonal import seasonal_decompose

plt.rcParams['figure.figsize'] = [5, 5]

result = seasonal_decompose(Gwangju, model='additive')

#result.plot()
#plt.show()

from statsmodels.tsa.stattools import kpss


def kpss_test(Gwangju, **kw):
    statistic, p_value, n_lags, critical_values = kpss(Gwangju, **kw)

    # Format Output
    print(f'KPSS Statistic: {statistic}')
    print(f'p-value: {p_value}')
    print(f'num lags: {n_lags}')
    print('Critial Values:')

    for key, value in critical_values.items():
        print(f'   {key} : {value}')
    print(f'Result: The Gwangju is {"not " if p_value < 0.05 else ""} stationary')


#kpss_test(Seoul)
#KPSS를 먼저 살펴본 결과, pvalue가 0.01수준이므로 귀무가설을 기각하고, 비정상 시계열이라는 대립 가설을 채택한다.


from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
# plt.rcParams['figure.figsize'] = [5, 5]
# plot_acf(Seoul)
# plot_pacf(Seoul, lags=15)
#plt.show()


diff_1=Gwangju.diff(periods=1).iloc[1:] #차분1

print(kpss_test(diff_1))
print("-------------------------")
diff_1.plot()

plot_rolling(diff_1, 2)

plot_acf(diff_1)
plot_pacf(diff_1, lags=15)
plt.show()








# GG = pd.read_csv('GG.csv', header=0, names=['years','Seoul'])
# GG['years'] = pd.to_datetime(GG['years']) #str to pandas Timestamp
# f = Forecaster(y=GG['Seoul'], current_dates=GG['years'])
# f.plot()
# f.plot_acf()
# f.plot_pacf()
# plt.show()

#훈련

# GG = Seoul_data.sort_values(by='years')
# train = GG[1:7]
# test = GG[7:33]
# plt.plot(train['years'], train['Seoul'])
# plt.show()