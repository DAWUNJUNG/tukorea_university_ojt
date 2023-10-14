import random
bigdata=[]
nodata=[]
for i in range(100):
    bigdata.append(random.randint(1, 33))
print(bigdata)
nodata = [i for i in range(1, 34) if i not in bigdata]
print('존재하지 않는 값(들):', nodata)