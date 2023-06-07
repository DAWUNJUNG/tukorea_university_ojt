import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import platform

# 운영체제별 한글 폰트 설정
if platform.system() == 'Darwin': # Mac 환경 폰트 설정
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows': # Windows 환경 폰트 설정
    plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False) # 마이너스 폰트 설정

#csv파일 호출 및 데이터 정제
data = pd.read_csv('right_turn_blind_spot_facility.csv')
df = pd.DataFrame(data)
df.drop(['연번', '관리번호', '세부위치', '위도', '경도', '데이터기준일자', '이미지명', '비고'], axis=1, inplace=True)

df['시군구명'] = df['시군구명'] + ' ' + df['법정동명']
df.drop(['시도명', '법정동명'], axis=1, inplace=True)

df.drop_duplicates(subset='시설물명', keep='first', inplace=True, ignore_index=False)

# column 이름 변경 및 index 지정
df.rename(columns={'시군구명': 'place'}, inplace=True)
df.rename(columns={'시설물명': 'facility'}, inplace=True)
df.set_index('place')

# 지역 중복 제거
df2 = df.drop_duplicates(subset='place', keep='first', inplace=False, ignore_index=False)
df2 = df2.reset_index(drop=True)

# 경기도 성남시 지역 전체 네트워크
nx_graph = nx.Graph()
nx_graph.add_nodes_from(df2['place'])
nx_graph = nx.from_pandas_edgelist(df, 'place', 'facility')
nx_graph.add_node('경기도')
for place in df2['place']:
    nx_graph.add_edge('경기도', place)

nx.draw(nx_graph, with_labels=True, node_color='lightblue', edge_color='grey', font_family='AppleGothic',
        font_size=10)
plt.savefig('경기도 성남시 전체')
plt.clf()

# 경기도 성남시 지역별 네트워크
for i in range(len(df2['place'])):
    nx_graph = nx.Graph()
    nx_graph.add_nodes_from(df2['place'][i])
    nx_graph = nx.from_pandas_edgelist(df[df['place'].str.contains(df2['place'][i])], 'place', 'facility')

    nx.draw(nx_graph, with_labels=True, node_color='lightblue', edge_color='grey', font_family='AppleGothic',
            font_size=10)
    plt.savefig('경기도 ' + df2['place'][i])
    plt.clf()