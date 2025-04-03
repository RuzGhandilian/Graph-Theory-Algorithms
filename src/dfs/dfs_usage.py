import networkx as nx
from dfs import DFS
from dfs_visualizer import DFSVisualizer

G = nx.Graph()
G.add_edges_from([
    (0, 7), (0, 11), (0, 9), (3, 2), (3, 4), (6, 5),
    (7, 3), (7, 6), (7, 11), (8, 1), (8, 12),
    (9, 8), (9, 10), (10, 1), (12, 2)
])

# Using DFS without visualization
dfs_solver = DFS(G)
path, visited = dfs_solver.traverse(start=0)
print("DFS Path:", path)
print("Visited Nodes:", visited)

# Using DFS with visualization
visualizer = DFSVisualizer(G)
path, visited = visualizer.visualize_traversal(start=0)
