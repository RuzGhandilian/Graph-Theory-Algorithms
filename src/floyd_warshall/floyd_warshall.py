import networkx as nx

def floyd_warshall(graph):
    nodes = list(graph.nodes())
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}
    next_node = {u: {v: None for v in nodes} for u in nodes}

    for u in nodes:
        dist[u][u] = 0
    for u, v, w in graph.edges(data='weight'):
        dist[u][v] = w
        next_node[u][v] = v

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node

def get_path(start, end, next_node):
    path = []
    if next_node[start][end] is None:
        return path
    while start != end:
        path.append(start)
        start = next_node[start][end]
    path.append(end)
    return path


G = nx.DiGraph()
G.add_weighted_edges_from([
    (0, 1, 3), (0, 2, 8), (1, 2, -2), (1, 3, 5),
    (2, 3, 2), (3, 0, 1)
])

distances, next_node = floyd_warshall(G)

path = get_path(0, 3, next_node)
print("Shortest Path from 0 to 3:", path)
