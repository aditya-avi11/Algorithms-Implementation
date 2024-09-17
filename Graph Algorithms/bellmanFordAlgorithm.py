import sys

def bellman_ford(adj_matrix, src):
    num_nodes = len(adj_matrix)
    dist = [float('inf')] * num_nodes
    dist[src] = 0
    
    for _ in range(num_nodes - 1):
        for u in range(num_nodes):
            for v in range(num_nodes):
                if adj_matrix[u][v] != 0 and dist[u] != float('inf') and dist[u] + adj_matrix[u][v] < dist[v]:
                    dist[v] = dist[u] + adj_matrix[u][v]
    
    for u in range(num_nodes):
        for v in range(num_nodes):
            if adj_matrix[u][v] != 0 and dist[u] != float('inf') and dist[u] + adj_matrix[u][v] < dist[v]:
                print("Graph contains negative weight cycle")
                return None
    
    return dist

def get_graph_input():
    num_nodes = int(input("Enter the number of nodes: "))
    adj_matrix = []
    
    print("Enter the adjacency matrix row by row (use space to separate values, use 0 for no edge):")
    for _ in range(num_nodes):
        row = list(map(int, input().split()))
        adj_matrix.append(row)
    
    return adj_matrix, num_nodes

adj_matrix, num_nodes = get_graph_input()
start_node = int(input("Enter the starting node (0-indexed): "))
distances = bellman_ford(adj_matrix, start_node)

if distances is not None:
    print("Vertex \tDistance from Source")
    for node in range(num_nodes):
        print(node, "\t", distances[node])