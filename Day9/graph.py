class Graph:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for i in range(size)] for j in range(size)]

    # Add edge for undirected graph
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    # Add edge for directed weighted graph
    def add_directed_weighted_edge(self, u, v, w):
        self.matrix[u][v] = w

    # Add edge for undirected weighted graph
    def add_undirected_weighted_edge(self, u, v, w):
        self.matrix[u][v] = w
        self.matrix[v][u] = w

    # Delete edge
    def delete_edge(self, u, v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    # Print graph
    def print_graph(self):
        print("\nAdjacency Matrix:")
        for row in self.matrix:
            print(row)


if __name__ == '__main__':

    size = int(input("Enter number of nodes: "))
    obj = Graph(size)

    while True:

        print("\n1. Add edge using adjacency matrix")
        print("2. Add undirected weighted edge")
        print("3. Add directed weighted edge")
        print("4. Print graph")
        print("5. Delete edge")
        print("0. Exit")

        n = int(input("Enter your choice: "))

        # Add normal edge
        if n == 1:
            u = int(input("Enter source node: "))
            v = int(input("Enter destination node: "))
            obj.add_edge(u, v)

        # Add undirected weighted edge
        elif n == 2:
            u = int(input("Enter source node: "))
            v = int(input("Enter destination node: "))
            w = int(input("Enter weight: "))
            obj.add_undirected_weighted_edge(u, v, w)

        # Add directed weighted edge
        elif n == 3:
            u = int(input("Enter source node: "))
            v = int(input("Enter destination node: "))
            w = int(input("Enter weight: "))
            obj.add_directed_weighted_edge(u, v, w)

        # Print graph
        elif n == 4:
            obj.print_graph()

        # Delete edge
        elif n == 5:
            u = int(input("Enter source node: "))
            v = int(input("Enter destination node: "))
            obj.delete_edge(u, v)

        # Exit
        elif n == 0:
            print("Program exited")
            break

        else:
            print("Invalid choice")