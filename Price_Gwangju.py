import pandas as pd
import matplotlib.pyplot as plt

# 원본데이터와 예측한 데이터 비교

preGwangju = pd.read_csv('./predict_GJ.csv', header=0, names=['years', 'pre_Gwangju'])
Gwangju = pd.read_csv('./estateGJ.csv', header=0, names=['years', 'Gwangju'])

i = 33
while i <39:
    Gwangju.loc[i] = None
    i+=1

# print(prePrice)
print(preGwangju)
# prePrice.index=prePrice['years']


preGwangju.index = preGwangju['years']
preGwangju.set_index('years', inplace=True)  # index로 변환
# prePrice['years'] = pd.to_datetime(prePrice['years']) #str to pandas Timestamp


print(preGwangju)
print(preGwangju.index)

# 시각화
plt.plot(preGwangju.index, preGwangju['pre_Gwangju'], label='predict Gwangju')
plt.plot(preGwangju.index, Gwangju['Gwangju'], label='Gwangju')
plt.legend()
plt.xticks(rotation=270)
plt.show()

# df=pd.DataFrame(index=prePrice['years'], columns=[a,b]) #columns에 문제가 있음
# df.plot()
# plt.show()
