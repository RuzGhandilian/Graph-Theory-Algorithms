import networkx as nx
from collections import deque

class BFS:
    def __init__(self, graph: nx.Graph):
        self.G = graph

    def traverse(self, start, target=None):
        q = deque([start])
        visited = set([start])
        path = []

        while q:
            u = q.popleft()
            path.append(u)

            if u == target:  # Early termination if target found
                break

            for neighbor in self.G.neighbors(u):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        return path, visited
