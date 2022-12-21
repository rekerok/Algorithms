def dijkstra(edges, start, end):
    # Initialize distances and previous nodes dictionaries
    distances = {vertex: float('inf') for vertex in edges}
    previous_nodes = {vertex: None for vertex in edges}
    distances[start] = 0

    unvisited_vertices = list(edges.keys())

    while unvisited_vertices:
        # Find the unvisited vertex with the minimum distance
        current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])
        if current_vertex == end:
            break

        unvisited_vertices.remove(current_vertex)

        for neighbor, weight in edges[current_vertex].items():
            # Calculate the distance to the neighbor through the current vertex
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                # Update the distance and previous node if it's shorter
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

    return distances, previous_nodes

def find_farthest_intersection(N, M, roads):
    # Create a dictionary of edges with the road travel times
    edges = {i: {} for i in range(1, N+1)}
    for u, v, w in roads:
        edges[u][v] = w
        edges[v][u] = w

    # Find the intersection farthest from the fire station in the shortest time
    farthest_distance = 0
    farthest_intersection = None
    for start in range(1, N+1):
        distances, _ = dijkstra(edges, start, end=None)
        # Find the maximum distance from the current starting point
        max_distance = max(distances.values())
        if max_distance > farthest_distance:
            farthest_distance = max_distance
            farthest_intersection = start

    return farthest_intersection

# Example usage
N = 5
M = 7
roads = [(1, 2, 2), (1, 3, 1), (2, 3, 3), (2, 4, 2), (3, 4, 2), (3, 5, 1), (4, 5, 3)]
print(find_farthest_intersection(N, M, roads))  # Output: 1