import random

pw = str()
chars = '한글우수'
for i in range(5):
    pw = pw + random.choice(chars)
print(pw)