import networkx as nx
from bfs import BFS
from bfs_visualizer import BFSVisualizer

G = nx.Graph()
G.add_edges_from([
    (0, 7), (0, 11), (0, 9), (3, 2), (3, 4), (6, 5),
    (7, 3), (7, 6), (7, 11), (8, 1), (8, 12),
    (9, 8), (9, 10), (10, 1), (12, 2)
])

# Using BFS without visualization
bfs_solver = BFS(G)
path, visited = bfs_solver.traverse(start=0)
print("BFS Path:", path)
print("Visited Nodes:", visited)

# Using BFS with visualization
visualizer = BFSVisualizer(G)
path, visited = visualizer.visualize_traversal(start=0)
