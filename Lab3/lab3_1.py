def find_connectivity_components(graph):
    # Initialize a list to store the connectivity components
    connectivity_components = []

    # Initialize a list to keep track of which vertices have been visited
    visited = {}
    for vertex in graph:
        visited[vertex] = False

    # Iterate through each vertex in the graph
    for v in graph:
        # If the vertex has not been visited, perform a DFS from that vertex
        if not visited[v]:
            # Initialize a new connectivity component
            component = []

            # Perform a DFS from the vertex
            dfs(v, visited, component, graph)

            # Add the connectivity component to the list
            connectivity_components.append(component)

    return connectivity_components


def dfs(v, visited, component, graph):
    # Mark the vertex as visited
    visited[v] = True

    # Add the vertex to the connectivity component
    component.append(v)

    # Iterate through the adjacency list of the vertex
    for neighbor in graph[v]:
        # If the neighbor has not been visited, perform a DFS from the neighbor
        if not visited[neighbor]:
            dfs(neighbor, visited, component, graph)


# Example usage
graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}
connectivity_components = find_connectivity_components(graph)
print(connectivity_components)  # [['A', 'B', 'D', 'C']]
