import networkx as nx
import matplotlib.pyplot as plt
from dfs import DFS

class DFSVisualizer:
    def __init__(self, graph: nx.Graph):
        self.G = graph
        self.pos = nx.spring_layout(self.G)  # Precompute positions for stability

    def visualize_traversal(self, start, target=None):
        dfs_solver = DFS(self.G)
        path, visited = dfs_solver.traverse(start, target)

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
        # Highlight traversal path edges
        if len(path) > 1:
            edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)
                     if self.G.has_edge(path[i], path[i + 1])]
            nx.draw_networkx_edges(self.G, self.pos, edgelist=edges, width=2, edge_color='red')
        plt.draw()
