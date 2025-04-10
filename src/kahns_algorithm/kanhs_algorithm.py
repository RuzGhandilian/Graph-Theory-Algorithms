import networkx as nx
from collections import deque


def kahn_topological_sort(G):
    in_degree = {node: 0 for node in G.nodes()}

    for u in G.nodes():
        for v in G.successors(u):
            in_degree[v] += 1

    queue = deque([node for node in G.nodes() if in_degree[node] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in G.successors(node):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != len(G.nodes()):
        raise ValueError("Graph has a cycle. Topological sort not possible.")

    return topo_order


G = nx.DiGraph()
G.add_edges_from([
    (5, 0), (5, 2), (4, 0), (4, 1),
    (2, 3), (3, 1)
])

order = kahn_topological_sort(G)
print("Topological Sort (Kahn's Algorithm):", order)
