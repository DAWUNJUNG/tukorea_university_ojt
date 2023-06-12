import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd

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

for name in bird_names:
    ix = (bird_data['bird_name'] == name)
    x, y = bird_data.longitude[ix], bird_data.latitude[ix]
    ax.plot(x, y, '.', transform=ccrs.Geodetic(), label=name)

plt.legend(loc='upper left')

plt.show()