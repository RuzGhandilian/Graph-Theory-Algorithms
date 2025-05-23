import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from ( ["A","B", "C", "D", "E"])
edges =  [("A","B",2), ("A","C",5), ("B","C",7), ("B","D",1), ("C","D",3), ("D","E",2)]
G.add_weighted_edges_from(edges)
edge_labels = {(u,v):d ['weight'] for u,v,d in G.edges(data = True)}
plt.figure(figsize=(10,8))
pos = nx.spring_layout(G)
nx.draw(G,pos, with_labels=True, node_color = "pink", edge_color = "gray",node_size = 2000, font_size = 12, font_weight = "bold", width = [G[u][v]['weight'] for u ,v in G.edges()])
nx.draw_networkx_edge_labels(G, pos,  edge_labels = edge_labels, font_size = 14)
plt.show()