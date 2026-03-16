##예측한 파일을 시각화 해줌
##plot_predict메소드가 삭제되어 대체 파일 생성한 것.

import pandas as pd
import matplotlib.pyplot as plt

#원본데이터와 예측한 데이터 비교

prePrice = pd.read_csv('./predict_price.csv', header=0,names=['years','pre_price'])
Price=pd.read_csv('./price.csv', header=0, names=['years', 'price'])

# print(prePrice)
print(Price)
# prePrice.index=prePrice['years']


prePrice.index = prePrice['years']
prePrice.set_index('years', inplace=True) #index로 변환
# prePrice['years'] = pd.to_datetime(prePrice['years']) #str to pandas Timestamp


print(prePrice)
print(prePrice.index)


#원형데이터와 예측데이터의 달라진 x축을 맞춰주기 위해서 2025년도까지 none값으로 채워준다.
i = len(Price)
end=len(Price)+4
print(i)
while i <end:
    Price.loc[i] = None
    i+=1


#시각화
plt.plot(prePrice.index, prePrice['pre_price'], label='predict price')
plt.plot(prePrice.index, Price['price'], label='price')
plt.legend()
plt.xticks(rotation=270)
plt.show()





