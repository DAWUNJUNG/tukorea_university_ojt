import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_nodes_from([1, 'P', 'Hi', 2, 3, 4, 5])

G.add_edges_from([(1, 'P'), (1, 'Hi'), (1, 2), (1, 3), (1, 4), (1, 5), (4, 5)])
nx.draw(G, with_labels=True, node_color='yellow', edge_color='red')

plt.show()