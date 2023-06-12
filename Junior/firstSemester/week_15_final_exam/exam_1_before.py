import networkx as nx
import matplotlib.pyplot as plt

nx_graph = nx.Graph()
nx_graph.add_nodes_from([1, 2, 3, 4, 5])
nx_graph.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (4, 5)])

nx.draw(nx_graph, with_labels=True)
plt.show()