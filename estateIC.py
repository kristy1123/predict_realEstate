import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('./estateIC.csv', header=0, names=['years','Incheon']) #헤더가 0이면 첫번째 열을 이름으로 읽음
print(f"Total samples length : {len(df)}")

df['years']=pd.to_datetime(df['years'])  #년도의 string형을 timestamp형으로 바꾸어 저장.

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


plot_acf(df.Incheon)#레퍼런스코드

#차분
# f=plt.figure()
# ax1=f.add_subplot(121)   #왜 121?
# ax1.set_title('1st dif')
# dif_1=ax1.plot(df.Incheon.diff())
#
# ax2=f.add_subplot(122) #왜 122?
# plot_acf(df.Incheon.diff().dropna(), ax=ax2)
# plt.show()
#
#차분 2번째
#차분 2번째
f2=plt.figure()
ax3=f2.add_subplot(121)   #왜 121?
ax3.set_title('2nd dif')
ax3.plot(df.Incheon.diff().diff())

ax4=f2.add_subplot(122) #왜 122?
plot_acf(df.Incheon.diff().diff().dropna(), ax=ax4)
plt.show()
#
# #차분 3번째
# f3=plt.figure()
# ax5=f3.add_subplot(121)   #왜 121?
# ax5.set_title('3rd dif')
# ax5.plot(df.Incheon.diff().diff().diff())
#
# ax6=f3.add_subplot(122) #왜 122?
# plot_acf(df.Incheon.diff().diff().diff().dropna(), ax=ax6)
# plt.show()

# #차분 10번째
# f4=plt.figure()
# ax7=f4.add_subplot(121)   #왜 121?s
# ax7.set_title('10th dif')
# ax7.plot(df.Incheon.diff().diff().diff().diff().diff().diff().diff().diff().diff().diff())
#
# ax8=f4.add_subplot(122) #왜 122?
# plot_acf(df.Incheon.diff().diff().diff().diff().diff().diff().diff().diff().diff().diff().dropna(), ax=ax8)
# plt.show()
#===> 이거는 줄일 수 있지 않을까?? 한번 알아볼 것

from statsmodels.tsa.stattools import adfuller
# result=adfuller(df.Incheon.dropna())
# print('p-value : ', result[1])
#
result_dif1=adfuller(df.Incheon.diff().dropna())
print('차분 1번한 p-value : ', result_dif1[1])

result_dif2=adfuller(df.Incheon.diff().diff().dropna())
print('차분 2번한 p-value : ', result_dif2[1])

result_dif3=adfuller(df.Incheon.diff().diff().diff().dropna())
print('차분 3번한 p-value : ', result_dif3[1])

#세번째 차분부터 p값이 확 떨어짐.
#보통 p값은 5%==0.05를 임계값 기준으로 삼는다. (1%, 5%, 10% 중 여기서는 5%를 채택. 데이터 양과 관련.)

#PACF

# f=plt.figure()
# ax1=f.add_subplot(121)   #왜 121?
# ax1.set_title('1st Order Differecing')
# dif_1=ax1.plot(df.Incheon.diff())
#
# ax2=f.add_subplot(122) #왜 122?
# plot_pacf(df.Incheon.diff().dropna(), ax=ax2)
# plt.show()

#ARIMA(p,d,q)
#p= pacf에서 가장 안정적이었던숫자 선택. 2번이었음. p=2
#q= acf에서 가장 안정적이었던 숫자 선택. 1과 2가 비슷했음. 일단 1을 선택하고 후에 값을 바꿔볼 것
#q=1
#d= p값이 임계를 넘기 전 값으로 설정. 2번이었음. d=2

#ARIMA(2,2,1)

#AIC 얻기
#Akaike Information Critera (AIC)는 모델이 수학적으로 얼마나 적합한지 테스트하기 위한 측정값
#AIC는 모델을 훈련하고 일반화하여 손실된 정보의 양을 측정한다. ==> 낮을 수록 좋음
#AIC낮추는 방법 : 1. p,d,q 값 변경. 2. k-교차 검증 등을 수행.
#여기서 q를 바꿔볼 것. p와 q값을 최적으로 설정하는데 도움을 줌.
# from statsmodels.tsa.arima_model import ARIMA #=> arima_model은 이제 없음.
from statsmodels.tsa.arima.model import ARIMA   # arima.model을 사용해야함함arima_model=ARIMA(df.price, order=(2,2,1))
arima_model=ARIMA(df.Incheon, order=(2,1,1))
# 1,2,1 AIC=156.36 => 이게 가장 값이 낮음
model=arima_model.fit()
print(model.summary())
#Log-likelihood : 가능도, 우도 - 사건이 일어날 가능성

a=model.get_prediction()
model.plot_diagnostics(figsize=(10,8))
plt.show()
startYear=pd.to_datetime('2006-01-01')
endYear=pd.to_datetime('2025-01-01')
predict=model.predict(start=startYear, end=endYear )#2025년도에서 끝날 수 있도록 값 설정.
print(predict)

#csv파일로 만듦
predict.to_csv('predictIC.csv')