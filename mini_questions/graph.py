class Node:
    def __init__(self, data):
        self.data = data
        self.neighbours = []
    def addNeighbour(self, nNode:"Node"):
        self.neighbours.append(nNode.data)
        nNode.neighbours.append(self.data)

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def __repr__(self):
        graph = []
        for k,v in self.nodes.items():
            graph.append(f"{k}: {v.neighbours}")
        return "\n".join(graph)

    def addVertex(self, data):
        newNode = Node(data)
        if data not in self.nodes:
            self.nodes[data] = newNode
    
    def addEdge(self, data1, data2):
        try:
            node1 = self.nodes[data1]
            node2 = self.nodes[data2]

            node1.addNeighbour(node2)
        except KeyError:
            print("Key not found!")
            
    def removeEdge(self, data1, data2):
        try:
            node1 = self.nodes[data1]
            node2 = self.nodes[data2]
            node1.neighbours.remove(data2)
            node2.neighbours.remove(data1)
        except ValueError:
            print("The edge doesn't exist!")

    def removeVertex(self, data):
        if data not in self.nodes:
            print("The vertex doesn't exist!")
            return
        for i in self.nodes.values():
            if i != data:
                if data in i.neighbours:
                    i.neighbours.remove(data)
        
        del self.nodes[data]

    def hasPath(self, start:int, end:int):
        try:
            first = self.nodes[start]
            last = self.nodes[end]
        except KeyError:
            return "The node doesn't exist!"

        if first.data not in self.nodes:
            return False
        if last.data in first.neighbours:
            return True
        
        for n in first.neighbours:
            if self.hasPath(self.nodes[n].data, last.data):
                return True
        return False


graph1 = Graph()

graph1.addVertex(1)
graph1.addVertex(2)
graph1.addVertex(3)
graph1.addVertex(4)

graph1.addEdge(1, 2)
graph1.addEdge(1, 3)
graph1.addEdge(4, 2)
print(graph1)

print(graph1.hasPath(1,4))