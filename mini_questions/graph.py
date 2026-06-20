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

    def hasPath(self, start:int, end:int, visited = None):
        if visited is None:
            visited = set()

        if start not in self.nodes or end not in self.nodes:
            return False
        if start == end:
            return True
        if start in visited:
            return False
        
        visited.add(start)

        for n in self.nodes[start].neighbours:
            if self.hasPath(n, end, visited):
                return True
        return False

if __name__ == "__main__":
    graph1 = Graph()

    graph1.addVertex(1)
    graph1.addVertex(2)
    graph1.addVertex(3)
    graph1.addVertex(4)

    graph1.addEdge(1, 2)
    graph1.addEdge(2, 3)
    graph1.addEdge(3, 1)
    print(graph1)

    print(graph1.hasPath(1,4))