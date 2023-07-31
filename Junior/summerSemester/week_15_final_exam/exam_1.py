import pandas as pd
import matplotlib.pyplot as plt

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
plt.scatter(ns_book7['번호'], ns_book7['대출건수'])

plt.show()