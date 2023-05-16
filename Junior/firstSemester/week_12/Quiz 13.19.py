import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

K = np.loadtxt("social2.csv", delimiter=",")
G = nx. to_networkx_graph(K)

maxG = max((G.subgraph(c) for c in nx.connected_components(G)), key=len)
nx.draw(maxG, with_labels=True, node_color='yellow', edge_color='red')
plt.show()