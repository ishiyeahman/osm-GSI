import osmnx as ox
import matplotlib.pyplot as plt 
import networkx as nx
from  src.system.meta.paths import path_chuo_kumamoto as data_path
import json
import gsi.gsi as gsi

place  = "Chuo-Ku,Kumamoto-shi,Japan"

# ox.plot_graph(ox.graph_from_place(place))
# plt.show()

G = ox.graph_from_place(place, network_type='drive')
nn = G.number_of_nodes()

node_colors = ["blue"]*nn
node_alphas = []


# """
json_open = open(data_path, 'r')
geo_data = json.load(json_open)

coord = geo_data['elements']
lons , lats = [], []
for n in coord:
    if n['type'] == "node":
        lons += [ n['lon'] ]
        lats += [ n['lat'] ]
        
depths = gsi.get_max_depth_multi_thread(lons, lats, "Depth")
# """

depth_values = list(filter(None, depths))
max_depth = max(depth_values)

for i in range(nn):
    if depths[i] is None:
        node_alphas.append(0)
    else : 
        node_alphas.append( depths[i] / max_depth)

ox.plot_graph(G, node_color=node_colors, node_alpha=node_alphas, bgcolor="dimgray")
# nx.draw(G)
plt.show()