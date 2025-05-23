import networkx as nx

class DFS:
    def __init__(self, graph: nx.Graph):
        self.G = graph

    def traverse(self, start, target=None):
        stack = [start]
        visited = set([start])
        path = []

        while stack:
            u = stack.pop()
            path.append(u)

            if u == target:  # Early termination
                break

            # Process neighbors in reversed sorted order (for consistent output)
            for neighbor in reversed(sorted(self.G.neighbors(u))):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return path, visited
