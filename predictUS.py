import pandas as pd
import matplotlib.pyplot as plt

# 원본데이터와 예측한 데이터 비교

preUlsan = pd.read_csv('./predict_US.csv', header=0, names=['years', 'pre_Ulsan'])
Ulsan = pd.read_csv('./estateUS.csv', header=0, names=['years', 'Ulsan'])

i = 33
while i <39:
    Ulsan.loc[i] = None
    i+=1

# print(prePrice)
print(preUlsan)
# prePrice.index=prePrice['years']


preUlsan.index = preUlsan['years']
preUlsan.set_index('years', inplace=True)  # index로 변환
# prePrice['years'] = pd.to_datetime(prePrice['years']) #str to pandas Timestamp


print(preUlsan)
print(preUlsan.index)

# 시각화
plt.plot(preUlsan.index, preUlsan['pre_Ulsan'], label='predict Ulsan')
plt.plot(preUlsan.index, Ulsan['Ulsan'], label='Ulsan')
plt.legend()
plt.xticks(rotation=270)
plt.show()

# df=pd.DataFrame(index=prePrice['years'], columns=[a,b]) #columns에 문제가 있음
# df.plot()
# plt.show()
