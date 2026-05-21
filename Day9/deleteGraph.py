import sys
class Graphs:
    def _init_(self):
        self.nodes = []
        self.graphs = []
        self.nodeCount = 0

    def addNode(self, v):
        if v in self.nodes:
            print(v, "node already exists")
        else:
            self.nodeCount += 1
            self.nodes.append(v)

            for x in self.graphs:
                x.append(0)

            temp = []
            for x in range(self.nodeCount):
                temp.append(0)

            self.graphs.append(temp)
            print(v, "is added")

    def addEdge_Undirected_Unweighted(self):
        v1 = input("Enter first vertex: ")
        v2 = input("Enter second vertex: ")

        if v1 not in self.nodes or v2 not in self.nodes:
            print("One or both vertices not found")
        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)

            self.graphs[index1][index2] = 1
            self.graphs[index2][index1] = 1

            print("Edge added successfully")

    def addEdge_directed_weighted(self):
        v1 = input("Enter source vertex: ")
        v2 = input("Enter destination vertex: ")
        w = int(input("Enter weight: "))

        if v1 not in self.nodes or v2 not in self.nodes:
            print("One or both vertices not found")
        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)

            self.graphs[index1][index2] = w

            print("Directed weighted edge added")

    def addEdge_Undirected_weighted(self):
        v1 = input("Enter first vertex: ")
        v2 = input("Enter second vertex: ")
        w = int(input("Enter weight: "))

        if v1 not in self.nodes or v2 not in self.nodes:
            print("One or both vertices not found")
        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)

            self.graphs[index1][index2] = w
            self.graphs[index2][index1] = w

            print("Undirected weighted edge added")

    def deleteGraph(self,v):
        if v not in self.nodes:
            print(v,"not present")
        else:
            self.nodeCount=-1
            index1=nodes.pop(index1)
            self.graph.pop(index1)
            for x in self.graph:
                x.pop(index1)
                print(v,"is deleted")