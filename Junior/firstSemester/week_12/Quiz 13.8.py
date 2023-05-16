import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

def erdosGraph (N, p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    listG = list(G.nodes())
    for i, node1 in enumerate(listG):
        for node2 in listG[i+1:]:
            if (bernoulli.rvs(p=p)):
                G.add_edge(node1, node2)

    return G

nx.draw(erdosGraph(20, 0.18))
plt.show()