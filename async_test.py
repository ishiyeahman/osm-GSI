import json 
import gsi.gsi as gsi
import asyncio

# need to set cache path
from  src.system.meta.paths import jpath

import matplotlib.pyplot as plt

json_open = open(jpath, 'r')
geo_data = json.load(json_open)
lon_lat = geo_data[0]['geojson']['coordinates']

lons , lats = [], []

for a , b in lon_lat[0]:
    # print(f"lon:{a}, lat{b}")
    lons  += [a]
    lats  += [b]
    
x = gsi.get_max_depth_multi_thread(lons, lats)
print(x)
    