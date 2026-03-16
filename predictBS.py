import pandas as pd
import matplotlib.pyplot as plt

# 원본데이터와 예측한 데이터 비교

preBusan = pd.read_csv('./predictBS.csv', header=0, names=['years', 'pre_Busan'])
Busan = pd.read_csv('./EstateBS.csv', header=0, names=['years', 'Busan'])

i = 33
while i < 39:
    Busan.loc[i] = None
    i += 1

# print(prePrice)
print(Busan)
# prePrice.index=prePrice['years']


preBusan.index = preBusan['years']
preBusan.set_index('years', inplace=True)  # index로 변환
# prePrice['years'] = pd.to_datetime(prePrice['years']) #str to pandas Timestamp


print(preBusan)
print(preBusan.index)

# 시각화
plt.plot(preBusan.index, preBusan['pre_Busan'], label='predict Busan')
plt.plot(preBusan.index, Busan['Busan'], label='Busan')
plt.legend()
plt.xticks(rotation=270)
plt.show()

# df=pd.DataFrame(index=prePrice['years'], columns=[a,b]) #columns에 문제가 있음
# df.plot()
# plt.show()