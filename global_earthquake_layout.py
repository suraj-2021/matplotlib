import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
     eq_data = json.load(f)

eq_dicts = eq_data['features']
mags,lats,lons = [],[],[]
for eq_dict in eq_dicts:
    mag = eq_dict['properties']['mag']
    lat = eq_dict['geometry'] ['coordinates'] [0]
    lon = eq_dict['geometry'] ['coordinates'] [1]
    mags.append(mag)
    lats.append(lat)
    lons.append(lon)

#Make the world Map
for x in mags:
  if x<0:
     mags.remove(x)
for y in lats:
  if y<0:
     lats.remove(y)
for z in lons:
  if z<0:
     lons.remove(z)

data = [{
  'type':'scattergeo',
  'lon': lons,
  'lat':lats,
  'marker': {
    'size': [5*mag for mag in mags],
    },
}]

my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes1.html')
