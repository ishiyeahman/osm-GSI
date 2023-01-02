# plot deo data from cache

import json 
from  meta.paths import jpath
import matplotlib.pyplot as plt

json_open = open(jpath, 'r')
geo_data = json.load(json_open)

lon_lat = geo_data[0]['geojson']['coordinates']


for a , b in lon_lat[0]:
    print(f"lon:{a}, lat{b}")
    plt.plot(b, a,marker='.', color = "green")
    


plt.show()