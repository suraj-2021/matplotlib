import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
     eq_data = json.load(f)

eq_dicts = eq_data['features']
mags = []
for eq_dict in eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
print(mags)
