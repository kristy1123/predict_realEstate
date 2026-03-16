import warnings
import pandas as pd
import matplotlib.pyplot as plt
# import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import predict

warnings.filterwarnings("ignore")
warnings.filterwarnings(action='ignore')

#물가지수

#물가의 데이터를 가져옴
Price = pd.read_csv('./price.csv', header=0, names=['years', 'price'])

Price['years'] = pd.to_datetime(Price['years']) #str to pandas Timestamp

#인덱스를 열로 삽입
Price.index = Price['years']
Price.set_index('years', inplace=True) #index로 변환

print(Price.tail()) #끝에서 5개의 데이터를 보여줌.


#훈련세트 테스트세트 분리
train= Price[0:57]
# test= Price[14:]

#함수 정의.

#평균, 분산, 표준편차 구하는 함수
#interval에 차분을 진행한 횟수를 넣음.
def plot_rolling(data, interval):
    rolmean = data.rolling(interval).mean()
    rolvar=data.rolling(interval).var()
    rolstd = data.rolling(interval).std()

    # Plot rolling statistics:
    plt.figure(figsize=(10, 6))
    plt.xlabel('Years')
    orig = plt.plot(data, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    var = plt.plot(rolvar, color='green', label='Rolling Var')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')  #범례
    plt.show()

# plot_rolling(Price, 1)

from statsmodels.tsa.stattools import kpss


#관측값, 추세, 계절, 불규칙요인
from statsmodels.tsa.seasonal import seasonal_decompose
plt.rcParams['figure.figsize'] = [12, 14]

result = seasonal_decompose(Price, model='additive')
result.plot()
plt.show()


#ACF, PACF 그리기
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plt.rcParams['figure.figsize'] = [9, 6]

plot_acf(Price)
plot_pacf(Price, lags=27)
plt.show()

#차분

diff_1= Price.diff(periods=1).iloc[1:] #차분1
diff_1.plot()
plot_rolling(diff_1, 2)
plot_acf(diff_1)
plot_pacf(diff_1,lags=27)
plt.show()

#정상시계열 검증방법
#p value가 1.0에 가까울 수록 귀무가설(비정상 데이터)일 확률이 높아진다
#p value가 0에 가까울 수록 대립가설(정상 데이터)일 확률이 높아진다.
from statsmodels.tsa.stattools import adfuller
result = adfuller(Price)
print(f'원 데이터 ADF Statistic: {result[0]:.3f}')
print(f'원 데이터 p-value: {result[1]:.3f}')

result = adfuller(diff_1)
print(f'1차 차분 ADF Statistic: {result[0]:.3f}')
print(f'1차 차분 p-value: {result[1]:.10f}')




#ARIMA 모델


res=ARIMA(train, order=(1,1,0)).fit()
arima_model = ARIMA(train, order=(1,1,0))
model = arima_model.fit()
# print(model.summary())

fig=plt.subplots()
ax1=plt.subplots()
ax1=train.loc['1965' :].plot(ax=ax1)
fig=res.predict('2020','2025', dynamic=True, ax=ax1, plot_insample=False)

plt.show()
#
model.predict(dynamic=False)
plt.show()

#예측
y_predict=pd.Series(model.forecast(14)[0], index=Price.value[14:0].index)
y_true=Price.value[14:0]    #범위 이게 맞나?