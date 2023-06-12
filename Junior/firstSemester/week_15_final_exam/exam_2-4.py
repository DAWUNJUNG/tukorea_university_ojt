import pandas as pd
import matplotlib.pyplot as plt
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

bird_data = pd.read_csv('bird_tracking.csv')
bird_names = pd.unique(bird_data.bird_name)

ix = (bird_data['bird_name'] == 'Eric')
x, y = bird_data.longitude[ix], bird_data.latitude[ix]

ax.plot(x[0:17000], y[0:17000], '.', transform=ccrs.Geodetic())
ax.plot(x[17101:18600], y[17101:18600], '.', transform=ccrs.Geodetic())

plt.show()