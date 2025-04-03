import networkx as nx
from src.dfs.dfs import DFS


def find_connected_components(graph):
    visited = set()
    components = []

    for node in graph.nodes():
        if node not in visited:
            dfs_solver = DFS(graph)
            path, component_nodes = dfs_solver.traverse(start=node)

            components.append(path)
            visited.update(component_nodes)

    return components


G = nx.Graph()
G.add_edges_from([
    (0, 1), (1, 2), (2, 3),  # Component 1
    (4, 5), (5, 6),          # Component 2
    (7, 8), (8, 9), (9, 7)   # Component 3 (Cycle)
])

components = find_connected_components(G)

print("Connected Components:")
for i, component in enumerate(components):
    print(f"Component {i + 1}: {component}")
