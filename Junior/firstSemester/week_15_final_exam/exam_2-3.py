import pandas as pd
import matplotlib.pyplot as plt

bird_data = pd.read_csv('bird_tracking.csv')

ix = (bird_data.bird_name == 'Eric')
x, y = bird_data.longitude[ix], bird_data.latitude[ix]

plt.figure(figsize=(7, 7))
plt.plot(x, y, '.')

plt.show()