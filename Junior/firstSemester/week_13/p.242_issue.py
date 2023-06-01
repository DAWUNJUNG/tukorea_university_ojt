#해당 파일은 interpreter를 conda로 셋팅 해야함 (cartopy가 conda에서만 동작)
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance
import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator()
plt.figure(figsize=(10, 10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

def euc(a, b):
    return distance.euclidean(a,b)

birdata = pd.read_csv('bird_tracking.csv')
bird_names = pd.unique(birdata.bird_name)
sindex = 2500
eindex = 7500
ix = birdata['bird_name'] == 'Eric'
x, y = birdata.longitude[ix], birdata.latitude[ix]
i = [x[sindex], y[sindex]]
j = [x[eindex], y[eindex]]
ax.plot(x[sindex:eindex], y[sindex:eindex], '.', transform=ccrs.Geodetic())
print('Eric', euc(i, j))

ix = birdata['bird_name'] == 'Nico'
x, y = birdata.longitude[ix], birdata.latitude[ix]
start = len(x)
dest = len(y)
i = [x[start+sindex], y[start+sindex]]
j = [x[dest+eindex], y[dest+eindex]]
ax.plot(x[sindex:eindex], y[sindex:eindex], '.', transform=ccrs.Geodetic())
print('Nico', euc(i, j))

ix = birdata['bird_name'] == 'Sanne'
x, y = birdata.longitude[ix], birdata.latitude[ix]
start = start + len(x)
dest = dest + len(y)
i = [x[start+sindex], y[start+sindex]]
j = [x[dest+eindex], y[dest+eindex]]
ax.plot(x[sindex:eindex], y[sindex:eindex], '.', transform=ccrs.Geodetic())
print('Sanne', euc(i, j))

plt.show()
