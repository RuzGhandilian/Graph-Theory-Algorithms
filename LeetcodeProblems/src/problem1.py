# Problem 1: Redundant Connection

def find_redundant_connection(edges):
    # each node starts as its own parent
    parent = [i for i in range(len(edges) + 1)]

    def find(x):
        # find the root parent
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        # try to join two sets
        px = find(x)
        py = find(y)
        if px == py:
            return False
        parent[px] = py
        return True

    for u, v in edges:
        if not union(u, v):
            return [u, v]
    return []
