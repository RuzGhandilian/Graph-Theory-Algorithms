import heapq
import networkx as nx

# Dijkstra's algorithm to find the shortest path
def dijkstra(graph, start, end):
    pq = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph.nodes()}
    previous_nodes = {node: None for node in graph.nodes()}  # Track the path
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        for neighbor in graph.neighbors(current_node):
            edge_data = graph[current_node][neighbor]
            new_distance = current_distance + edge_data['weight']

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (new_distance, neighbor))

    # Reconstruct the shortest path from start to end directly
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]

    path.reverse()  # Reverse to get path from start to end
    return path

# Create the graph
G = nx.DiGraph()
G.add_weighted_edges_from([
    (0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7),
    (2, 3, 3), (3, 4, 1), (2, 4, 5)
])

# Get the shortest path from node 0 to node 4
path = dijkstra(G, start=0, end=4)

# Output the shortest path
print("Shortest Path from 0 to 4:", path)
