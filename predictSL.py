import pandas as pd
import matplotlib.pyplot as plt

# 원본데이터와 예측한 데이터 비교

preSeoul = pd.read_csv('./Predict_SL.csv', header=0, names=['years', 'pre_Seoul'])
Seoul = pd.read_csv('./estateSL.csv', header=0, names=['years', 'Seoul'])
i = 33
while i <39:
    Seoul.loc[i] = None
    i+=1


# print(preSeoul)
print(Seoul)
# preSeoul.index=preSeoul['years']


preSeoul.index = preSeoul['years']
preSeoul.set_index('years', inplace=True)  # index로 변환
# preSeoul['years'] = pd.to_datetime(preSeoul['years']) #str to pandas Timestamp

print(preSeoul)
print(preSeoul.index)

# 시각화
plt.plot(preSeoul.index, preSeoul['pre_Seoul'], label='predict Seoul')
plt.plot(preSeoul.index, Seoul['Seoul'], label='Seoul')

plt.legend()
plt.xticks(rotation=270) #x레이블 돌려주는 메소드
plt.show()

# df=pd.DataFrame(index=preSeoul['years'], columns=[a,b]) #columns에 문제가 있음
# df.plot()
# plt.show()

