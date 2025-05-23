import networkx as nx
import matplotlib.pyplot as plt
from bfs import BFS

class BFSVisualizer:
    def __init__(self, graph: nx.Graph):
        self.G = graph
        self.pos = nx.spring_layout(self.G)  # Precompute positions for stability

    def visualize_traversal(self, start, target=None):
        bfs_solver = BFS(self.G)
        path, visited = bfs_solver.traverse(start, target)

        plt.figure(figsize=(8, 6))
        plt.ion()  # Enable interactive mode

        for i in range(len(path)):
            self._update_visualization(path[:i+1])
            plt.pause(0.5)  # Ensure each step is visible

        plt.ioff()  # Disable interactive mode after completion
        plt.show()  # Show final visualization

        return path, visited

    def _update_visualization(self, path):
        plt.clf()
        nx.draw(
            self.G,
            self.pos,
            with_labels=True,
            node_color=['red' if node in path else 'lightblue' for node in self.G.nodes()],
            edge_color='gray'
        )
        plt.draw()
