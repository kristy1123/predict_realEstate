import pandas as pd
import matplotlib.pyplot as plt

# 원본데이터와 예측한 데이터 비교

preGyeonggi = pd.read_csv('./predictGG.csv', header=0, names=['years', 'pre_Gyeonggi'])
Gyeonggi = pd.read_csv('./EstateGG.csv', header=0, names=['years', 'Gyeonggi'])
i = 33
while i <39:
    Gyeonggi.loc[i] = None
    i+=1

# print(preGyeonggi)
print(Gyeonggi)
# preGyeonggi.index=preGyeonggi['years']


preGyeonggi.index = preGyeonggi['years']
preGyeonggi.set_index('years', inplace=True)  # index로 변환
# preGyeonggi['years'] = pd.to_datetime(preGyeonggi['years']) #str to pandas Timestamp


print(preGyeonggi)
print(preGyeonggi.index)

# 시각화
plt.plot(preGyeonggi.index, preGyeonggi['pre_Gyeonggi'], label='predict Gyeonggi')
plt.plot(preGyeonggi.index, Gyeonggi['Gyeonggi'], label='Gyeonggi')
plt.legend()
plt.xticks(rotation=270) #x레이블 돌려주는 메소드
plt.show()

# df=pd.DataFrame(index=preGyeonggi['years'], columns=[a,b]) #columns에 문제가 있음
# df.plot()
# plt.show()
