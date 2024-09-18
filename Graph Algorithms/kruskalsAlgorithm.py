def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    
    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

def kruskal_sort_edges(adj_matrix):
    edges = []
    n = len(adj_matrix)
    for i in range(n):
        for j in range(i + 1, n):   # i + 1, ensures that each edge is considered only once, since bidirectional edges, hence check only upper triangle of adjMatrix
            if adj_matrix[i][j] != 0:
                edges.append((adj_matrix[i][j], i, j))
    
    edges.sort(key=lambda x: x[0])
    return edges

def kruskal_mst(adj_matrix):
    sorted_edges = kruskal_sort_edges(adj_matrix)
    n = len(adj_matrix)
    
    parent = list(range(n))
    rank = [0] * n
    
    mst_edges = []
    mst_cost = 0
    
    for weight, u, v in sorted_edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_edges.append((weight, u, v))
            mst_cost += weight
    
    return mst_edges, mst_cost

def get_graph_input():
    num_nodes = int(input("Enter the number of nodes: "))
    graph = []
    
    print("Enter the adjacency matrix row by row (use space to separate values):")
    for i in range(num_nodes):
        row = list(map(int, input().split()))
        graph.append(row)
    
    return graph

graph = get_graph_input()
mst_edges, mst_cost = kruskal_mst(graph)

print("MST edges (weight, u, v):")
for edge in mst_edges:
    print(edge)

print(f"Total cost of the Minimum Spanning Tree: {mst_cost}")