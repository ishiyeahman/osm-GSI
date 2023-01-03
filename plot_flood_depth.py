import json 
import gsi.gsi as gsi

# need to set cache path
from  src.system.meta.paths import jpath_a

import matplotlib.pyplot as plt

json_open = open(jpath_a, 'r')
geo_data = json.load(json_open)

coord = geo_data['elements']

cnt = 0
for n in coord:
    cnt += 1
    if n['type'] == "node":
        a = float(n['lon'])
        b = float(n['lat'])
        # print(f"lon:{a}, lat{b}")
        d =  gsi.get_max_depth(a, b, "Depth")
        
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