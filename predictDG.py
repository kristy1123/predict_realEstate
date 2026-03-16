import pandas as pd
import matplotlib.pyplot as plt

# 원본데이터와 예측한 데이터 비교

preDaegu = pd.read_csv('./predictDG.csv', header=0, names=['years', 'pre_Daegu'])
Daegu = pd.read_csv('./estateDG.csv', header=0, names=['years', 'Daegu'])

i = 33
while i < 39:
    Daegu.loc[i] = None
    i += 1

# print(prePrice)
print(Daegu)
# prePrice.index=prePrice['years']


preDaegu.index = preDaegu['years']
preDaegu.set_index('years', inplace=True)  # index로 변환
# prePrice['years'] = pd.to_datetime(prePrice['years']) #str to pandas Timestamp

#시각화
plt.plot(preDaegu.index, preDaegu['pre_Daegu'], label='predict price')
plt.plot(preDaegu.index, Daegu['Daegu'], label='price')
plt.legend()
plt.xticks(rotation=270)
plt.show()
