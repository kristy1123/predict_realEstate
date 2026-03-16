import pandas as pd
import matplotlib.pyplot as plt

# 원본데이터와 예측한 데이터 비교

preDaejeon = pd.read_csv('./predict_DJ.csv', header=0, names=['years', 'pre_Daejeon'])
Daejeon = pd.read_csv('./estateDJ.csv', header=0, names=['years', 'Daejeon'])

i = 33
while i <39:
    Daejeon.loc[i] = None
    i+=1

# print(prePrice)
print(preDaejeon)
# prePrice.index=prePrice['years']


preDaejeon.index = preDaejeon['years']
preDaejeon.set_index('years', inplace=True)  # index로 변환
# prePrice['years'] = pd.to_datetime(prePrice['years']) #str to pandas Timestamp


print(preDaejeon)
print(preDaejeon.index)

# 시각화
plt.plot(preDaejeon.index, preDaejeon['pre_Daejeon'], label='predict Daejeon')
plt.plot(preDaejeon.index, Daejeon['Daejeon'], label='Daejeon')
plt.legend()
plt.xticks(rotation=270)
plt.show()

# df=pd.DataFrame(index=prePrice['years'], columns=[a,b]) #columns에 문제가 있음
# df.plot()
# plt.show()

