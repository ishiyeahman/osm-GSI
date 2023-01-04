import json 
from  meta.paths import jpath_a

import matplotlib.pyplot as plt

json_open = open(jpath_a, 'r')
geo_data = json.load(json_open)

coord = geo_data['elements']

for n in coord:
    if n['type'] == "node":
        a = n['lon']
        b = n['lat']
        print(f"lon:{a}, lat{b}")
        plt.plot(b, a,marker='.', color = "green")
    

plt.show()