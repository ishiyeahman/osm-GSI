import osmnx as ox
import matplotlib.pyplot as plt 
import networkx as nx

place  = "Chuo-Ku,Kumamoto-shi,Japan"


# ox.plot_graph(ox.graph_from_place(place))
# plt.show()

G = ox.graph_from_place(place, network_type='drive')
nn = G.number_of_nodes()

node_colors = ["red"]*nn


ox.plot_graph(G, node_color=node_colors)
# nx.draw(G)
plt.show()