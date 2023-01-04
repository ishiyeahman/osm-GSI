import osmnx as ox
import matplotlib.pyplot as plt 
import networkx as nx

place = {'city' : 'Kumamoto','state' : 'Kumamoto', 'country' : 'Japan'}


# ox.plot_graph(ox.graph_from_place(place))
# plt.show()

G = ox.graph_from_place(place, network_type='drive')
# ox.plot_graph(G)
nx.draw(G)
plt.show()