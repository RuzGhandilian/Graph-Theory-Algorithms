# Problem 4: Find if Path Exists in Graph

def valid_path(n, edges, source, destination):
    # create graph as adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n

    def dfs(node):
        # mark node as visited
        if node == destination:
            return True
        visited[node] = True
        for nei in graph[node]:
            if not visited[nei]:
                if dfs(nei):
                    return True
        return False

    return dfs(source)
