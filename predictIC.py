import pandas as pd
import matplotlib.pyplot as plt

# 원본데이터와 예측한 데이터 비교

preIncheon = pd.read_csv('./predict_IC.csv', header=0, names=['years', 'pre_Incheon'])
Incheon = pd.read_csv('./estateIC.csv', header=0, names=['years', 'Incheon'])
i = 33
while i <39:
    Incheon.loc[i] = None
    i+=1

# print(preIncheon)
print(Incheon)
# preIncheon.index=preIncheon['years']


preIncheon.index = preIncheon['years']
preIncheon.set_index('years', inplace=True)  # index로 변환
# preIncheon['years'] = pd.to_datetime(preIncheon['years']) #str to pandas Timestamp


print(preIncheon)
print(preIncheon.index)

# 시각화
plt.plot(preIncheon.index, preIncheon['pre_Incheon'], label='predict Incheon')
plt.plot(preIncheon.index, Incheon['Incheon'], label='Incheon')
plt.legend()
plt.xticks(rotation=270) #x레이블 돌려주는 메소드
plt.show()

# df=pd.DataFrame(index=preIncheon['years'], columns=[a,b]) #columns에 문제가 있음
# df.plot()
# plt.show()
