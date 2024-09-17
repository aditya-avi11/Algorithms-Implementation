import sys

class Graph:
    def _init_(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, dist, sptSet):
        min_dist = sys.maxsize
        min_index = -1
        for u in range(self.V):
            if dist[u] < min_dist and not sptSet[u]:
                min_dist = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for _ in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 and not sptSet[y] and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.printSolution(dist)

def get_graph_input():
    num_nodes = int(input("Enter the number of nodes: "))
    graph = []
    print("Enter the adjacency matrix row by row (use space to separate values, use 0 for no edge):")
    for _ in range(num_nodes):
        row = list(map(int, input().split()))
        graph.append(row)
    return graph, num_nodes

graph, num_nodes = get_graph_input()
g = Graph(num_nodes)
g.graph = graph
start_node = int(input("Enter the starting node (0-indexed): "))
g.dijkstra(start_node)