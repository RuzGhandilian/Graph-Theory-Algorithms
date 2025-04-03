import networkx as nx

# Bellman-Ford algorithm to find shortest paths from start node
def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0

    for _ in range(len(graph.nodes()) - 1):
        for u, v, weight in graph.edges(data='weight'):
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    return distances

G = nx.DiGraph()
G.add_weighted_edges_from([
    (0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2),
    (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)
])

start_node = 0

distances = bellman_ford(G, start_node)

print(f"Shortest distances from node {start_node}:")
for node, dist in distances.items():
    print(f"{start_node} -> {node}: {dist}")
