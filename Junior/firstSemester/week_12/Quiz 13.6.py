import networkx as nx

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (4, 5)])

G.remove_node(4)

print('No. nodes:', G.number_of_nodes())
print('No. edges:', G.number_of_edges())