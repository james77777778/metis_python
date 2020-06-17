import matplotlib.pyplot as plt
import networkx as nx
import python_metis as metis


G = metis.example_networkx()
(edgecuts, parts) = metis.part_graph(G, 3)
colors = ['red', 'blue', 'green']
color_map = []
for i, p in enumerate(parts):
    color_map.append(colors[p])

nx.draw(G, node_color=color_map)
plt.show()
