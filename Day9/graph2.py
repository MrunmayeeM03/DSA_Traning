# Graphs
import sys
class Graphs:
    def _init_(self):
        self.nodes = []
        self.graph = []
        self.nodeCount = 0
    def addNode(self, v):
        if v in self.nodes:
            print(v, "is already present")
        else:
            self.nodeCount += 1
            self.nodes.append(v)
            for row in self.graph:
                row.append(0)
            temp = []
            for i in range(self.nodeCount):
                temp.append(0)
            self.graph.append(temp)
            print(v, "is added")
    def addEdge_Undirected_Unweighted(self):
        pass
    def addEdge_Undirected_Weighted(self):
        pass
    def addEdge_Directed_Weighted(self):
        pass
    def printGraph(self):
        if self.nodeCount == 0:
            print("Graph is empty")
            return
        print("\nAdjacency Matrix:\n")
        print("  ", end=" ")
        for node in self.nodes:
            print(node, end=" ")
        print()
        for i in range(self.nodeCount):
            print(self.nodes[i], end=" ")
            for j in range(self.nodeCount):
                print(self.graph[i][j], end=" ")
            print()
    def deleteGraph(self):
        pass


if __name__ == '_main_':
    obj = Graphs()
    while True:
        print("\n1. Add Node")
        print("2. Add Edge Undirected Unweighted")
        print("3. Add Edge Undirected Weighted")
        print("4. Add Edge Directed Weighted")
        print("5. Print Graph")
        print("6. Delete Graph")
        print("0. Exit\n")
        n = int(input("Enter any choice: "))
        if n == 1:
            v = input("Enter vertex: ")
            obj.addNode(v)
        elif n == 2:
            obj.addEdge_Undirected_Unweighted()
        elif n == 3:
            obj.addEdge_Undirected_Weighted()
        elif n == 4:
            obj.addEdge_Directed_Weighted()
        elif n == 5:
            obj.printGraph()
        elif n == 6:
            obj.deleteGraph()
        elif n == 0:
            sys.exit(0)
        else:
            print("Invalid Choice")