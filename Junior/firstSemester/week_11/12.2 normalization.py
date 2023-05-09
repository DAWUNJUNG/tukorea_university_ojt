import pandas as pd

ary = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
data = pd.DataFrame(ary, columns=['수온', '상온'])

#1. Simple Feature Scaling
data['수온'] = data['수온'] / data['수온'].max()
data['상온'] = data['상온'] / data['상온'].max()
print('1. Simple Feature Scaling')
print(data)

print("\n\n")

#2. Min-Max
data = pd.DataFrame(ary, columns=['수온', '상온'])
data['수온'] = (data['수온'] - data['수온'].min()) / (data['수온'].max() - data['수온'].min())
data['상온'] = (data['상온'] - data['상온'].min()) / (data['상온'].max() - data['상온'].min())
print('2. Min-Max')
print(data)