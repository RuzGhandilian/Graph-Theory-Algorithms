import networkx as nx
from collections import deque



G = nx.Graph()
G.add_edges_from(
    [(0, 7), (0, 11), (0, 9), (3, 2), (3, 4), (6, 5), (7, 3), (7, 6), (7, 11), (8, 1), (8, 12), (9, 8), (9, 10),
     (10, 1), (12, 2)])



def bfs(start):
    q = deque()
    q.append(start)

    n = G.number_of_nodes()
    visited = [False] * n
    visited[start] = True

    path = []

    while q:
        u = q.popleft()
        path.append(u)



        for neighbor in G.neighbors(u):
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

    return path  # Return the full BFS traversal path


# Example usage:
start_node = 0
path = bfs(start_node)
print("BFS traversal path:", path)
