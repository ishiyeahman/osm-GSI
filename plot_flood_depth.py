import json 
import gsi.gsi as gsi

# need to set cache path
from  src.system.meta.paths import jpath_a

import matplotlib.pyplot as plt

json_open = open(jpath_a, 'r')
geo_data = json.load(json_open)

coord = geo_data['elements']


lons , lats = [], []
for n in coord:
    if n['type'] == "node":
        lons += [ n['lon'] ]
        lats += [ n['lat'] ]
        
depths = gsi.get_max_depth_multi_thread(lons, lats, "Depth")

print(depths)

depth_index = 0
for n in coord:
    if n['type'] == "node":
        a = n['lon']
        b = n['lat']
        # print(f"lon:{a}, lat{b}")
        d = depths[depth_index]
        depth_index += 1
        
        if d is None:
            plt.plot(b, a,marker='.', color = (0.0, 0.5, 0.0, 0.3 ))
        else:
            # exist depth data
            if d > 1.0:
                if d > 2.0:
                    plt.plot(b, a,marker='.', color = (1.0, 0.0, 0.0 ,1.0 ))
                else:
                    plt.plot(b, a,marker='.', color = (1.0, 0.0, 0.0 , d - 1.0 ))
                
            else:
                plt.plot(b, a,marker='.', color = (0.0, 0.0, 0.5 ,d ))
        
        # if d is not None:
        #     break

plt.show()