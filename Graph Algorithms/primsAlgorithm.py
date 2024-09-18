def prims_algorithm(graph):
    num_nodes = len(graph)
    V_T = set()   # A set that will store the vertices included in the MST
    E_T = []      # A list that will store the edges (with their weights) that are part of the MST
    
    # Start from vertex 0
    V_T.add(0)
    
    while len(V_T) < num_nodes:
        min_edge = float('inf')
        v_star = u_star = -1
        
        for v in V_T:
            for u in range(num_nodes):
                if u not in V_T and graph[v][u] != 0:
                    if graph[v][u] < min_edge:
                        min_edge = graph[v][u]
                        v_star, u_star = v, u
        
        V_T.add(u_star)
        E_T.append((v_star, u_star, min_edge))
    
    return E_T

def get_graph_input():
    num_nodes = int(input("Enter the number of nodes: "))
    graph = []
    
    print("Enter the adjacency matrix row by row (use space to separate values):")
    for i in range(num_nodes):
        row = list(map(int, input().split()))
        graph.append(row)
    
    return graph

graph = get_graph_input()


mst_edges = prims_algorithm(graph)


print("Minimum Spanning Tree Edges (u, v, weight):")
for edge in mst_edges:
    print(edge)

total_cost = sum(edge[2] for edge in mst_edges)
print(f"Total cost of the Minimum Spanning Tree: {total_cost}")