import networkx as nx
from src.topological_sort.topological_sort import topological_sort

def longest_path(G, start):
    topo_order = topological_sort(G)
    longest_paths = {node: float('-inf') for node in G.nodes()}
    longest_paths[start] = 0
    predecessors = {node: None for node in G.nodes()}
    for u in topo_order:
        if longest_paths[u] != float('-inf'):
            for v in G.neighbors(u):
                weight = G[u][v].get('weight', 1)
                if longest_paths[u] + weight > longest_paths[v]:
                    longest_paths[v] = longest_paths[u] + weight
                    predecessors[v] = u
    return longest_paths, predecessors

def get_path(start, end, predecessors):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    return path if path[0] == start else []

G = nx.DiGraph()
G.add_weighted_edges_from([
    (0, 1, 5), (0, 2, 3), (1, 3, 6), (1, 2, 2),
    (2, 3, 7), (3, 4, 2), (2, 4, 4), (0, 4, 8)
])

longest_paths, predecessors = longest_path(G, 0)
print("Longest Paths:", longest_paths)
print("Predecessors:", predecessors)

path = get_path(0, 4, predecessors)
print("Longest Path from 0 to 4:", path)
