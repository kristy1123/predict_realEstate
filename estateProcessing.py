#4번째로 실행해야하는 파일
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")
warnings.filterwarnings(action='ignore')

np.set_printoptions(formatter={'float_kind':'{:f}'.format})
sns.set(rc={'figure.figsize':(8,6)})


data=pd.read_csv("./부동산 지수.csv")   #데이터 삽입

data=data.transpose()   #행 열 전환
data.rename(columns=data.iloc[0], inplace=True)

#null데이터는 버릴거임. ,,,,이 부분들임.
data = data.drop(data.index[0])
data = data.drop(data.index[33:]) #인덱싱할 숫자 값은 보유한 데이터 규격에 맞춰서. 숫자는 엑셀에서 파일 오픈했을 때 마지막 열숫자-1
#print(data)

#csv 데이터의 column name이 전부 영어명이어야함.
#열 하나씩 슬라이싱
Seoul_data = data[['Seoul']]
Gyeonggi_data = data[['Gyeonggi']]
Incheon_data = data[['Incheon']]
Busan_data = data[['Busan']]
Daegu_data = data[['Daegu']]
Gwangju_data = data[['Gwangju']]
Daejeon_data = data[['Daejeon']]
Ulsan_data = data[['Ulsan']]

#인덱스의 값을 열로 넣을 거임. (년도)
#년도는 어차피 모든 데이터가 똑같이 공유하기 때문에 한개만 생성해도 ok
y = Seoul_data.index.values  #csv에서 인덱스 값을 y에 저장
Seoul_data.insert(0, column='years',value=y) #0번째에 years라는 열이름으로 y삽입

y = Gyeonggi_data.index.values  #csv에서 인덱스 값을 y에 저장
Gyeonggi_data.insert(0, column='years',value=y)

y = Incheon_data.index.values  #csv에서 인덱스 값을 y에 저장
Incheon_data.insert(0, column='years',value=y)

y = Busan_data.index.values  #csv에서 인덱스 값을 y에 저장
Busan_data.insert(0, column='years',value=y)

y = Daegu_data.index.values  #csv에서 인덱스 값을 y에 저장
Daegu_data.insert(0, column='years',value=y)

y = Gwangju_data.index.values  #csv에서 인덱스 값을 y에 저장
Gwangju_data.insert(0, column='years',value=y)

y = Daejeon_data.index.values  #csv에서 인덱스 값을 y에 저장
Daejeon_data.insert(0, column='years',value=y)

y = Ulsan_data.index.values  #csv에서 인덱스 값을 y에 저장
Ulsan_data.insert(0, column='years',value=y)



# ##############################데이터가공
#슬라이싱한 열을 각각 하나의 파일로 저장.
Seoul_data.to_csv('estateSL.csv')
Gyeonggi_data.to_csv('estateGG.csv')
Incheon_data.to_csv('estateIC.csv')
Busan_data.to_csv('estateBS.csv')
Daegu_data.to_csv('estateDG.csv')
Gwangju_data.to_csv('estateGJ.csv')
Daejeon_data.to_csv('estateDJ.csv')
Ulsan_data.to_csv('estateUS.csv')