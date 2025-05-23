import networkx as nx
from FundamentalAlgorithms.src.topological_sort.topological_sort import topological_sort

def single_source_longest_path_by_negating(G, start):
    # Create a new graph with negated weights
    neg_G = nx.DiGraph()
    for u, v, data in G.edges(data=True):
        weight = data.get('weight', 1)
        neg_G.add_edge(u, v, weight=-weight)

    # Topological sort
    topo_order = topological_sort(neg_G)

    # Step 3: Initialize distances and predecessors
    shortest_paths = {node: float('inf') for node in neg_G.nodes()}
    shortest_paths[start] = 0
    predecessors = {node: None for node in neg_G.nodes()}

    # Relax edges in topological order (DAG shortest path algo)
    for u in topo_order:
        if shortest_paths[u] != float('inf'):
            for v in neg_G.neighbors(u):
                weight = neg_G[u][v]['weight']
                if shortest_paths[u] + weight < shortest_paths[v]:
                    shortest_paths[v] = shortest_paths[u] + weight
                    predecessors[v] = u

    # Convert back to longest path by negating the results
    longest_paths = {node: -dist if dist != float('inf') else float('-inf') for node, dist in shortest_paths.items()}

    return longest_paths, predecessors

def get_path(start, end, predecessors):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    return path if path[0] == start else []

# Example usage
G = nx.DiGraph()
G.add_weighted_edges_from([
    (0, 1, 5), (0, 2, 3), (1, 3, 6), (1, 2, 2),
    (2, 3, 7), (3, 4, 2), (2, 4, 4), (0, 4, 8)
])

longest_paths, predecessors = single_source_longest_path_by_negating(G, 0)
print("Longest Paths:", longest_paths)
print("Predecessors:", predecessors)

path = get_path(0, 4, predecessors)
print("Longest Path from 0 to 4:", path)
