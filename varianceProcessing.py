#세번째로 돌려야할 파일
#예측한 물가지수 데이터를 변동률으로 가공.
#variance.csv가 생성됨

import pandas as pd

vari = pd.read_csv('./predict_price.csv', header=0,names=['years','price'])
vari2 = pd.read_csv('./predict_price.csv', header=0,names=['years','price'])

for i in range(1,61):
    vari2.price[i]=vari.price[i]-vari.price[i-1]
print()
variance=vari2[41:] #인덱스를 열로 삽입
variance.index = variance['years']
variance.set_index('years', inplace=True) #index로 변환
for i in range(0,20):
    (100+variance.price[i])/100
variance.to_csv('variance.csv')















