import networkx as nx
from FundamentalAlgorithms.src.dfs.dfs import DFS

def topological_sort(graph):
    # Check if the graph is a DAG
    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("Graph is not a DAG. Topological sorting is not possible.")

    dfs_solver = DFS(graph)
    visited = set()
    stack = []

    # Function to process each node by adding it to the stack
    def process_node(node):
        stack.append(node)

    # Run DFS on all unvisited nodes
    for node in graph.nodes():
        if node not in visited:
            _, component_nodes = dfs_solver.traverse(start=node)
            visited.update(component_nodes)
            for n in component_nodes:
                process_node(n)

    return stack[::-1]

G = nx.DiGraph()
G.add_edges_from([
    (5, 0), (5, 2), (4, 0), (4, 1),
    (2, 3), (3, 1)
])

order = topological_sort(G)

print("Topological Sort Order:", order)
