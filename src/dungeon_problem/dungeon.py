import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from src.bfs.bfs import BFS


def bfs_shortest_path(dungeon):
    rows, cols = len(dungeon), len(dungeon[0])
    graph = nx.Graph()
    start, goal = None, None
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    # Convert dungeon to graph representation
    for x in range(rows):
        for y in range(cols):
            if dungeon[x][y] == 'S':
                start = (x, y)
            elif dungeon[x][y] == 'E':
                goal = (x, y)

            if dungeon[x][y] != '#':
                for dx, dy in directions:
                    nx_, ny_ = x + dx, y + dy
                    if 0 <= nx_ < rows and 0 <= ny_ < cols and dungeon[nx_][ny_] != '#':
                        graph.add_edge((x, y), (nx_, ny_))

    bfs = BFS(graph)
    path, visited = bfs.traverse(start, goal)

    return path if path[-1] == goal else []  # Return path from start to goal

dungeon = [
    ['S', '.', '.', '#', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', 'E', '#']
]


path = bfs_shortest_path(dungeon)

for row in dungeon:
    print(' '.join(row))
print("Shortest path:", path)
