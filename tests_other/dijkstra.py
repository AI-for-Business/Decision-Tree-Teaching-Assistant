# https://www.section.io/engineering-education/dijkstra-python/

class Graph:
    # A constructor to initialize the values
    def __init__(self, nodes):
        # distance array initialization
        self.distArray = [0 for i in range(nodes)]
        # visited nodes initialization
        self.visited_set = [0 for i in range(nodes)]
        # initializing the number of nodes
        self.V = nodes
        # initializing the infinity value
        self.INF = 1000000
        # initializing the graph matrix
        self.graph = [[0 for column in range(nodes)]
                      for row in range(nodes)]

    def dijkstra(self, src_node):
        for i in range(self.V):
            # initialise the distances to infinity first
            self.distArray[i] = self.INF
            # set the visited nodes set to false for each node
            self.visited_set[i] = False
        # initialise the first distance to 0
        self.distArray[src_node] = 0
        for i in range(self.V):

            # Pick the minimum distance node from  
            # the set of nodes not yet processed.  
            # u is always equal to srcNode in first iteration 
            u = self.min_distance(self.distArray, self.visited_set)

            # Put the minimum distance node in the  
            # visited nodes set
            self.visited_set[u] = True

            # Update dist[v] only if is not in visited_set, there is an edge from
            # u to v, and total weight of path from src to  v through u is 
            # smaller than current value of dist[v]
            for v in range(self.V):
                if self.graph[u][v] > 0 and not self.visited_set[v] and self.distArray[v] > self.distArray[u] + \
                        self.graph[u][v]:
                    self.distArray[v] = self.distArray[u] + self.graph[u][v]

        self.print_solution(self.distArray)

    # A utility function to find the node with minimum distance value, from
    # the set of nodes not yet included in shortest path tree 
    def min_distance(self, dist_array, visited_set):

        # Initialize minimum distance for next node
        min_dist = self.INF

        # Search not nearest node not in the  
        # unvisited nodes
        for v in range(self.V):
            if dist_array[v] < min_dist and not visited_set[v]:
                min_dist = dist_array[v]
                min_index = v

        return min_index

    def print_solution(self, dist_array):
        print("Node \tDistance from 0")
        for i in range(self.V):
            print(i, "\t", dist_array[i])


# Display our table
ourGraph = Graph(7)
ourGraph.graph = [[0, 2, 6, 0, 0, 0, 0],
                  [2, 0, 0, 5, 0, 0, 0],
                  [6, 6, 0, 8, 0, 0, 0],
                  [0, 0, 8, 0, 10, 15, 0],
                  [0, 0, 0, 10, 0, 6, 2],
                  [0, 0, 0, 15, 6, 0, 6],
                  [0, 0, 0, 0, 2, 6, 0],
                  ]

ourGraph.dijkstra(0)
