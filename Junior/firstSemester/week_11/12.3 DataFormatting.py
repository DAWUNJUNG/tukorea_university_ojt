import numpy as np
import pandas as pd

price = np.random.randint(100, size=8) * 10000
cars = pd.DataFrame(price, columns=['price'])
print('데이터프레임 정의')
print(cars)

print("\n")

group_names = ['저급', '중급', '고급']
cars['Level'], mybin = pd.cut(cars['price'], 3, labels=group_names, retbins=True)
print('수치값 카테고리값으로 변환')
print(cars)

print("\n")

print('mybin 출력')
print(mybin)

print("\n")

ary = [[1, 1.1, '손'], [2, 2.2, '날개'], [3, 3.3, '손']]
data = pd.DataFrame(ary, columns=['수온', '상온', 'hand'])
print_data = pd.get_dummies(data['hand'])
print('카테고리 값을 수치값으로 변환하기')
print(print_data)

print("\n")

data = pd.concat([data, pd.get_dummies(data['hand'])], axis=1, sort=False)
print('가공하여 원본데이터에 추가하기')
print(data)

print("\n")

data.drop(['hand'], axis=1, inplace=True)
print('hand 컬럼 drop 하기')
print(data)