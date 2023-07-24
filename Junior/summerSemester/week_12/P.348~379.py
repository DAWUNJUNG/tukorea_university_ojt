import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = "NanumGothic"

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)

fig, axes = plt.subplots(2, 2 ,figsize=(20, 16))

# 산점도
top30_pubs = ns_book7['출판사'].value_counts()[:30]
top30_pubs_idx = ns_book7['출판사'].isin(top30_pubs.index)

ns_book8 = ns_book7[top30_pubs_idx].sample(1000, random_state=43)
sc = axes[0, 0].scatter(ns_book8['발행년도'], ns_book8['출판사'],
                        linewidths=0.5, edgecolors='k', alpha=0.3,
                        s=ns_book8['대출건수'], c=ns_book8['대출건수'],
                        cmap='jet')
axes[0, 0].set_title('출판사별 발행 도서')
fig.colorbar(sc, ax=axes[0, 0])

# 스택 영역 그래프
ns_book9 = ns_book7[top30_pubs_idx][['출판사','발행년도','대출건수']]
ns_book9 = ns_book9.groupby(by=['출판사','발행년도']).sum()
ns_book9 = ns_book9.reset_index()

ns_book10 = ns_book9.pivot_table(index='출판사',columns='발행년도')
top10_pubs = top30_pubs.index[:10]
year_cols = ns_book10.columns.get_level_values(1)

axes[0, 1].stackplot(year_cols, ns_book10.loc[top10_pubs].fillna(0), labels=top10_pubs)
axes[0, 1].set_title('연도별 대출건수')
axes[0, 1].legend(loc='upper left')
axes[0, 1].set_xlim(1985, 2025)

# 스택 막대 그래프
ns_book12 = ns_book10.loc[top10_pubs].cumsum()
for i in reversed(range(len(ns_book12))):
    bar = ns_book12.iloc[i]
    label = ns_book12.index[i]
    axes[1, 0].bar(year_cols, bar, label=label)

axes[1, 0].set_title('연도별 대출건수')
axes[1, 0].legend(loc='upper left')
axes[1, 0].set_xlim(1985, 2025)

# 원 그래프
data = top30_pubs[:10]
labels = top30_pubs.index[:10]
axes[1, 1].pie(data, labels=labels, startangle=90,
               autopct='%.1f%%', explode=[0.1] + [0] * 9)
axes[1, 1].set_title('출판사 도서 비율')

fig.savefig('all_in_one.png')
fig.show()