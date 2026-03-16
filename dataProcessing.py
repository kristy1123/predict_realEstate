#첫번째 실행 파일
#원형데이터인 priceData.csv가 필요함.
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

np.set_printoptions(formatter={'float_kind':'{:f}'.format})
sns.set(rc={'figure.figsize':(8,6)})

warnings.filterwarnings("ignore")
warnings.filterwarnings(action='ignore')

data = pd.read_csv("./priceData.csv")   #데이터 삽입

data=data.transpose()   #행 열 전환
data.rename(columns=data.iloc[0], inplace=True)

#null데이터는 버릴거임. ,,,,이 부분들임.
data = data.drop(data.index[0])
data = data.drop(data.index[57:]) #인덱싱할 숫자 값은 보유한 데이터 규격에 맞춰서. 숫자는 엑셀에서 파일 오픈했을 때 마지막 열숫자-1

#csv 데이터의 column name이 전부 영어명이어야함.
#열 하나씩 슬라이싱
price_data = data[['price']]

#인덱스의 값을 열로 넣을 거임. (년도)
#년도는 어차피 모든 데이터가 똑같이 공유하기 때문에 한개만 생성해도 ok
y = price_data.index.values  #csv에서 인덱스 값을 y에 저장
price_data.insert(0, column='years', value=y) #0번째에 years라는 열이름으로 y삽입

# ##############################데이터가공
#슬라이싱한 열을 각각 하나의 파일로 저장.
price_data.to_csv('price.csv')
